#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GADIS AGI ULTIMATE V3 - PRODUCTION MAIN
Single Admin Version - Production Ready
"""

import os
import sys
import asyncio
import logging
import signal
import time
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from collections import deque
from typing import Optional, Dict, Any

from telegram import Update
from telegram.ext import Application, ContextTypes
from telegram.request import HTTPXRequest

from config import Config
from database import Database
from systems.hts_fwb_system import HTSFWBSystem, RankingSystem
from tg_bot.handlers import TelegramHandlers
from core.brain import Brain

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


class RateLimiter:
    """Simple rate limiter untuk error handler"""
    
    def __init__(self, max_per_minute: int = 3):
        self.window = deque(maxlen=max_per_minute)
        self.max_per_minute = max_per_minute
    
    def can_send(self) -> bool:
        now = time.time()
        # Hapus yang lebih dari 60 detik
        while self.window and now - self.window[0] > 60:
            self.window.popleft()
        
        if len(self.window) < self.max_per_minute:
            self.window.append(now)
            return True
        return False


class TaskSupervisor:
    """Supervisor untuk background tasks dengan auto-restart"""
    
    def __init__(self, max_retries: int = 3):
        self.tasks: Dict[str, asyncio.Task] = {}
        self.max_retries = max_retries
        self.running = True
    
    async def supervise(self, name: str, coro_func, *args, **kwargs):
        """Supervise a task with auto-restart"""
        retries = 0
        
        while retries < self.max_retries and self.running:
            try:
                task = asyncio.create_task(coro_func(*args, **kwargs), name=name)
                self.tasks[name] = task
                await task
                break  # Success, exit loop
            except asyncio.CancelledError:
                logger.info(f"Task {name} cancelled")
                break
            except Exception as e:
                retries += 1
                logger.error(f"Task {name} failed ({retries}/{self.max_retries}): {e}")
                
                if retries < self.max_retries:
                    # Exponential backoff
                    wait_time = 2 ** retries
                    logger.info(f"Restarting {name} in {wait_time}s...")
                    await asyncio.sleep(wait_time)
        
        if name in self.tasks:
            del self.tasks[name]
    
    async def stop_all(self):
        """Stop all supervised tasks"""
        self.running = False
        for name, task in list(self.tasks.items()):
            if not task.done():
                task.cancel()
        
        if self.tasks:
            await asyncio.gather(*self.tasks.values(), return_exceptions=True)
            self.tasks.clear()


class GadisUltimateBot:
    """Main bot class - Single Admin Version"""
    
    def __init__(self):
        self.start_time = datetime.now()
        self.config = Config
        self.application = None
        self.brain: Optional[Brain] = None
        self.admin_id = self.config.ADMIN_ID
        
        # Thread pool untuk blocking operations
        self.thread_pool = ThreadPoolExecutor(max_workers=2)
        
        # Rate limiter untuk error handler
        self.error_rate_limiter = RateLimiter(max_per_minute=3)
        
        # AI Infra components
        self.request_queue = RequestQueue(max_concurrent=Config.REQUEST_QUEUE_MAX_CONCURRENT)
        self.lifecycle = LifecycleManager()
        self.background_tasks = BackgroundTaskManager()
        self.task_supervisor = TaskSupervisor(max_retries=3)
        self.state_manager: Optional[AIStateManager] = None
        self.emotional_scheduler: Optional[EmotionalScheduler] = None
        
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
        """Global error handler dengan rate limiting"""
        logger.error(f"Unhandled exception: {context.error}", exc_info=context.error)
        
        # Notify admin dengan rate limiting
        if self.admin_id and self.error_rate_limiter.can_send():
            try:
                await context.bot.send_message(
                    chat_id=self.admin_id,
                    text=f"⚠️ Bot Error: {str(context.error)[:200]}"
                )
            except Exception as e:
                logger.error(f"Failed to send error notification: {e}")
    
    async def set_brain(self, brain: Brain):
        """Set brain instance dengan cleanup brain lama"""
        # Stop brain lama jika berbeda
        if self.brain and self.brain.user_id != brain.user_id:
            logger.info(f"Stopping old brain for user {self.brain.user_id}")
            await self.brain.stop()
        
        self.brain = brain
        logger.info(f"Brain set for user {brain.user_id}")
        
        # Setup state manager untuk admin
        if brain.user_id == self.admin_id:
            self.state_manager = AIStateManager(self.db, self.admin_id)
            await self._load_initial_state()
            
            # Restart background tasks dengan brain baru
            await self._restart_background_tasks()
    
    async def _load_initial_state(self):
        """Load initial state untuk admin"""
        if self.state_manager and self.brain:
            await self.state_manager.load_state(self.brain)
            logger.info("Initial state loaded for admin")
    
    async def _restart_background_tasks(self):
        """Restart background tasks dengan aman"""
        # Stop existing tasks dengan timeout
        try:
            await asyncio.wait_for(self.background_tasks.stop_all(), timeout=5.0)
        except asyncio.TimeoutError:
            logger.warning("Timeout stopping background tasks, forcing cancel")
        
        await self.task_supervisor.stop_all()
        await self._start_background_tasks()
    
    async def _start_background_tasks(self):
        """Start semua background tasks dengan supervisor"""
        if not self.brain:
            logger.warning("Brain not ready, skipping background tasks")
            return
        
        # Emotional scheduler
        self.emotional_scheduler = EmotionalScheduler(self.brain.emotion)
        self.task_supervisor.supervise(
            "emotional_scheduler",
            self._run_emotional_scheduler
        )
        
        # Memory consolidation - di thread pool
        self.task_supervisor.supervise(
            "memory_consolidation",
            self._run_memory_consolidation
        )
        
        # State saving (khusus admin)
        if self.state_manager and self.brain.user_id == self.admin_id:
            self.task_supervisor.supervise(
                "state_saving",
                self._run_state_saving
            )
        
        logger.info("Background tasks started with supervisor")
    
    async def _run_emotional_scheduler(self):
        """Run emotional scheduler dengan interval"""
        while True:
            try:
                await asyncio.sleep(Config.EMOTIONAL_UPDATE_INTERVAL)
                if self.emotional_scheduler:
                    await self.emotional_scheduler.tick()
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Emotional scheduler error: {e}")
    
    async def _run_memory_consolidation(self):
        """Run memory consolidation di thread pool"""
        while True:
            try:
                await asyncio.sleep(Config.MEMORY_CONSOLIDATION_INTERVAL)
                if self.brain:
                    loop = asyncio.get_running_loop()
                    await loop.run_in_executor(
                        self.thread_pool,
                        self.brain.memory.consolidate
                    )
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Memory consolidation error: {e}")
    
    async def _run_state_saving(self):
        """Run periodic state saving"""
        while True:
            try:
                await asyncio.sleep(Config.STATE_SAVE_INTERVAL)
                if self.state_manager and self.brain:
                    await self.state_manager.save_state(self.brain)
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"State saving error: {e}")
    
    def _setup_signal_handlers(self):
        """Setup signal handlers dengan aman"""
        try:
            loop = asyncio.get_running_loop()
            for sig in (signal.SIGTERM, signal.SIGINT):
                try:
                    loop.add_signal_handler(sig, self.lifecycle.request_shutdown)
                except NotImplementedError:
                    logger.warning(f"Signal handler not implemented for {sig}")
        except Exception as e:
            logger.warning(f"Could not setup signal handlers: {e}")
    
    async def run(self):
        """Main run loop"""
        try:
            # Build app
            await self.build_app()
            
            # Setup lifecycle
            self.lifecycle.start_time = datetime.now()
            
            # Get Railway URL
            railway_url = os.getenv("RAILWAY_PUBLIC_DOMAIN") or os.getenv("RAILWAY_STATIC_URL")
            if not railway_url:
                raise RuntimeError("RAILWAY_PUBLIC_DOMAIN not set")
            
            webhook_url = f"https://{railway_url}/webhook"
            port = int(os.getenv("PORT", 8080))
            
            logger.info(f"Starting webhook server on port {port}")
            logger.info(f"Webhook URL: {webhook_url}")
            
            # Setup signal handlers
            self._setup_signal_handlers()
            
            # Print startup banner
            self._print_banner(port, railway_url)
            
            # Start lifecycle
            await self.lifecycle.start(self)
            
            # Start webhook (blocks)
            await self.application.run_webhook(
                listen="0.0.0.0",
                port=port,
                url_path="webhook",
                webhook_url=webhook_url,
                allowed_updates=["message", "callback_query"]
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
        print("  • AI Infra: Queue, Lifecycle, Supervisor")
        print("\n" + "="*60)
        print(f"🌐 Webhook URL: https://{url}/webhook")
        print(f"📡 Port: {port}")
        print(f"👤 Admin ID: {self.admin_id}")
        print("\n✅ Bot is running!")
        print("="*60 + "\n")
    
    async def shutdown(self):
        """Graceful shutdown"""
        logger.info("🔄 Graceful shutdown initiated")
        
        # Save final state untuk admin
        if self.state_manager and self.brain and self.brain.user_id == self.admin_id:
            try:
                await self.state_manager.save_state(self.brain)
                logger.info("Final state saved")
            except Exception as e:
                logger.error(f"Error saving final state: {e}")
        
        # Stop task supervisor
        await self.task_supervisor.stop_all()
        
        # Stop background tasks
        await self.background_tasks.stop_all()
        
        # Stop brain
        if self.brain:
            await self.brain.stop()
        
        # Stop application
        if self.application:
            try:
                await self.application.stop()
                await self.application.shutdown()
            except Exception as e:
                logger.error(f"Error stopping application: {e}")
        
        # Shutdown thread pool
        self.thread_pool.shutdown(wait=True)  # Wait for pending tasks
        
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
