#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GADIS AGI ULTIMATE V3 - PRODUCTION MAIN
Dengan AI Infra lengkap dan semua bug fixes
"""

import os
import sys
import asyncio
import logging
import signal
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

from telegram import Update
from telegram.ext import Application, ContextTypes
from telegram.request import HTTPXRequest

from config import Config
from database import Database
from systems.hts_fwb_system import HTSFWBSystem, RankingSystem
from tg_bot.handlers import TelegramHandlers

# AI Infra imports
from infra.request_queue import RequestQueue
from infra.lifecycle import LifecycleManager
from infra.background_tasks import BackgroundTaskManager
from infra.emotional_scheduler import EmotionalScheduler
from infra.state_manager import AIStateManager

# Setup logging
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO
)
logger = logging.getLogger("GADIS_MAIN")

Config.create_dirs()


class GadisUltimateBot:
    """Main bot class dengan AI Infra lengkap"""
    
    def __init__(self):
        self.start_time = datetime.now()
        self.config = Config
        self.application = None
        self.brain = None  # Akan diisi oleh handlers setelah role dipilih
        
        # Thread pool untuk blocking operations
        self.thread_pool = ThreadPoolExecutor(max_workers=2)
        
        # AI Infra components
        self.request_queue = RequestQueue(max_concurrent=Config.REQUEST_QUEUE_MAX_CONCURRENT)
        self.lifecycle = LifecycleManager()
        self.background_tasks = BackgroundTaskManager()
        self.state_manager = None  # Akan diisi setelah brain ready
        self.emotional_scheduler = None
        
        # Task monitoring
        self.active_tasks = set()
        
        if not self.config.validate():
            raise RuntimeError("Config validation failed")
        
        logger.info("Initializing systems...")
        
        self.db = Database(Config.DB_PATH)
        self.hts_system = HTSFWBSystem(self.db)
        self.ranking = RankingSystem(self.db)
        self.handlers = TelegramHandlers(self)
        
        logger.info("Core systems initialized")
        
        # Register shutdown hook
        self.lifecycle.register_shutdown_hook(self.shutdown)
    
    async def build_app(self):
        """Build Telegram application"""
        request = HTTPXRequest(
            connection_pool_size=20,
            connect_timeout=30,
            read_timeout=30,
            write_timeout=30
        )
        
        self.application = (
            Application.builder()
            .token(self.config.TELEGRAM_TOKEN)
            .request(request)
            .build()
        )
        
        # Setup handlers
        await self.handlers.setup(self.application)
        
        self.application.add_error_handler(self.error_handler)
        
        logger.info("Application built")
    
    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE):
        """Global error handler"""
        logger.error(f"Unhandled exception: {context.error}", exc_info=context.error)
        
        # Notify admin (dengan rate limiting sederhana)
        if self.config.ADMIN_ID and hasattr(self, '_last_error_time'):
            now = datetime.now()
            if (now - self._last_error_time).total_seconds() > 60:  # Max 1 per menit
                try:
                    await context.bot.send_message(
                        chat_id=self.config.ADMIN_ID,
                        text=f"⚠️ Bot Error: {str(context.error)[:200]}"
                    )
                    self._last_error_time = now
                except:
                    pass
        elif self.config.ADMIN_ID:
            self._last_error_time = datetime.now()
    
    async def set_brain(self, brain):
        """Set brain instance setelah role dipilih (dipanggil dari handlers)"""
        self.brain = brain
        logger.info(f"Brain set for user {brain.user_id}")
        
        # Setup state manager untuk admin
        if brain.user_id == self.config.ADMIN_ID:
            self.state_manager = AIStateManager(self.db, self.config.ADMIN_ID)
            await self._load_initial_state()
            
            # Restart background tasks dengan brain baru
            await self._restart_background_tasks()
    
    async def _load_initial_state(self):
        """Load initial state untuk admin"""
        if self.state_manager and self.brain:
            await self.state_manager.load_state(self.brain)
            logger.info("Initial state loaded for admin")
    
    async def _restart_background_tasks(self):
        """Restart background tasks dengan brain baru"""
        # Cancel existing tasks
        await self.background_tasks.stop_all()
        
        # Start new tasks
        await self._start_background_tasks()
    
    async def _start_background_tasks(self):
        """Start semua background tasks (internal)"""
        if not self.brain:
            logger.warning("Brain not ready, skipping background tasks")
            return
        
        # Emotional scheduler - gunakan public method
        self.emotional_scheduler = EmotionalScheduler(self.brain.emotion)
        await self.background_tasks.start_periodic(
            "emotional_scheduler",
            Config.EMOTIONAL_UPDATE_INTERVAL,
            self._emotional_tick_wrapper
        )
        
        # Memory consolidation - jalankan di thread pool agar tidak block
        await self.background_tasks.start_periodic(
            "memory_consolidation",
            Config.MEMORY_CONSOLIDATION_INTERVAL,
            self._memory_consolidation_wrapper
        )
        
        # State saving (khusus admin)
        if self.state_manager and self.brain.user_id == self.config.ADMIN_ID:
            await self.background_tasks.start_periodic(
                "state_saving",
                Config.STATE_SAVE_INTERVAL,
                self._save_state_periodic
            )
        
        logger.info("Background tasks started")
    
    async def _emotional_tick_wrapper(self):
        """Wrapper untuk emotional scheduler tick"""
        if self.emotional_scheduler:
            await self.emotional_scheduler.tick()  # Pakai public method
    
    async def _memory_consolidation_wrapper(self):
        """Wrapper untuk memory consolidation di thread pool"""
        if self.brain:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(
                self.thread_pool,
                self.brain.memory.consolidate
            )
    
    async def _save_state_periodic(self):
        """Periodic state saving"""
        if self.state_manager and self.brain:
            await self.state_manager.save_state(self.brain)
    
    def _setup_signal_handlers(self):
        """Setup signal handlers dengan aman"""
        try:
            loop = asyncio.get_running_loop()
            for sig in (signal.SIGTERM, signal.SIGINT):
                try:
                    loop.add_signal_handler(sig, self.lifecycle.request_shutdown)
                except NotImplementedError:
                    # Fallback untuk Windows
                    logger.warning(f"Signal handler not implemented for {sig}")
                    pass
        except Exception as e:
            logger.warning(f"Could not setup signal handlers: {e}")
    
    async def run(self):
        """Main run loop"""
        try:
            # Build app dulu
            await self.build_app()
            
            # Setup lifecycle (tapi belum start)
            self.lifecycle.start_time = datetime.now()
            
            # Get Railway URL
            railway_url = os.getenv("RAILWAY_PUBLIC_DOMAIN") or os.getenv("RAILWAY_STATIC_URL")
            if not railway_url:
                raise RuntimeError("RAILWAY_PUBLIC_DOMAIN not set")
            
            webhook_url = f"https://{railway_url}/webhook"
            port = int(os.getenv("PORT", 8080))
            
            logger.info(f"Starting webhook server on port {port}")
            logger.info(f"Webhook URL: {webhook_url}")
            
            # Setup signal handlers dengan aman
            self._setup_signal_handlers()
            
            # Print startup banner
            self._print_banner(port, railway_url)
            
            # Start lifecycle
            await self.lifecycle.start(self)
            
            # Start webhook (this blocks until shutdown)
            await self.application.run_webhook(
                listen="0.0.0.0",
                port=port,
                url_path="webhook",
                webhook_url=webhook_url,
                allowed_updates=["message", "callback_query"]  # Hapus channel_post
            )
            
        except Exception as e:
            logger.error(f"Fatal error in run: {e}")
            await self.shutdown()
            raise
    
    def _print_banner(self, port: int, url: str):
        """Print startup banner"""
        print("\n" + "="*60)
        print("🚀 GADIS AGI ULTIMATE V3.0")
        print("="*60)
        print("\n📋 Features:")
        print("  • 9 Role (termasuk MANTAN & TEMAN SMA)")
        print("  • HTS/FWB System dengan Unique ID")
        print("  • TOP 10 Ranking")
        print("  • Level 1-12 + Reset ke 7")
        print("  • Memory System")
        print("  • Emotional Engine")
        print("  • Consciousness Loop")
        print("  • AI Infra: Queue, Lifecycle, Background Tasks")
        print("\n" + "="*60)
        print(f"🌐 Webhook URL: https://{url}/webhook")
        print(f"📡 Port: {port}")
        print("\n✅ Bot is running!")
        print("="*60 + "\n")
    
    async def shutdown(self):
        """Graceful shutdown"""
        logger.info("🔄 Graceful shutdown initiated")
        
        # Set lifecycle status
        self.lifecycle.health_status = "shutting_down"
        
        # Save final state untuk admin
        if self.state_manager and self.brain and self.brain.user_id == self.config.ADMIN_ID:
            try:
                await self.state_manager.save_state(self.brain)
                logger.info("Final state saved")
            except Exception as e:
                logger.error(f"Error saving final state: {e}")
        
        # Stop background tasks
        await self.background_tasks.stop_all()
        
        # Stop application
        if self.application:
            try:
                await self.application.stop()
                await self.application.shutdown()
            except Exception as e:
                logger.error(f"Error stopping application: {e}")
        
        # Shutdown thread pool
        self.thread_pool.shutdown(wait=False)
        
        # Stop lifecycle
        await self.lifecycle.shutdown()
        
        logger.info("✅ Shutdown complete")


# ================= MAIN =================
async def main():
    """Main entry point"""
    bot = GadisUltimateBot()
    
    try:
        await bot.run()
    except KeyboardInterrupt:
        logger.info("📟 Received keyboard interrupt")
        await bot.shutdown()
    except Exception as e:
        logger.critical(f"💥 Fatal error: {e}")
        await bot.shutdown()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
