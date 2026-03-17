#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GADIS AGI ULTIMATE V3 - PRODUCTION READY
Arsitektur Sederhana untuk Single Admin
FULL VERSION dengan logging lengkap
"""

import os
import sys
import asyncio
import logging
from datetime import datetime
from pathlib import Path

from telegram import Update
from telegram.ext import Application, ContextTypes
from telegram.request import HTTPXRequest

from config import Config
from database import Database
from systems.hts_fwb_system import HTSFWBSystem, RankingSystem
from tg_bot.handlers import TelegramHandlers

# Setup logging
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO
)
logger = logging.getLogger("GADIS_MAIN")

# Buat folder yang diperlukan
Config.create_dirs()


class SimpleBot:
    """Bot sederhana untuk single admin"""
    
    def __init__(self):
        self.config = Config
        self.start_time = datetime.now()
        self.application = None
        self.is_ready = False
        self._shutdown_event = asyncio.Event()
        
        # Validasi konfigurasi
        if not self.config.validate():
            logger.error("❌ Config validation failed")
            sys.exit(1)
        
        try:
            # Initialize database
            logger.info("📦 Initializing database...")
            self.db = Database(Config.DB_PATH)
            logger.info("✅ Database initialized")
            
            # Initialize systems
            logger.info("⚙️ Initializing HTS/FWB system...")
            self.hts_system = HTSFWBSystem(self.db)
            self.ranking = RankingSystem(self.db)
            logger.info("✅ Systems initialized")
            
            # Initialize handlers
            logger.info("🎯 Initializing handlers...")
            self.handlers = TelegramHandlers(self)
            logger.info("✅ Handlers initialized")
            
            logger.info("✅ Bot initialized successfully")
            
        except Exception as e:
            logger.error(f"❌ Failed to initialize bot: {e}")
            sys.exit(1)
    
    async def build_app(self):
        """Build Telegram application"""
        try:
            logger.info("🔧 Building application...")
            
            request = HTTPXRequest(
                connection_pool_size=10,
                connect_timeout=30,
                read_timeout=30
            )
            
            self.application = (
                Application.builder()
                .token(self.config.TELEGRAM_TOKEN)
                .request(request)
                .build()
            )
            
            # Setup handlers
            logger.info("🔧 Registering handlers...")
            await self.handlers.setup(self.application)
            
            # Add error handler
            self.application.add_error_handler(self.error_handler)
            
            # Initialize
            logger.info("🔧 Initializing application...")
            await self.application.initialize()
            
            logger.info("✅ Application built successfully")
            
        except Exception as e:
            logger.error(f"❌ Failed to build application: {e}")
            sys.exit(1)
    
    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE):
        """Global error handler"""
        logger.error(f"❌ Error: {context.error}", exc_info=True)
        
        # Log update yang menyebabkan error
        if update:
            logger.error(f"Update that caused error: {update}")
        
        # Notify admin if configured
        if self.config.ADMIN_ID:
            try:
                await context.bot.send_message(
                    chat_id=self.config.ADMIN_ID,
                    text=f"⚠️ Bot Error: {str(context.error)[:200]}"
                )
            except Exception as e:
                logger.error(f"Failed to send error notification: {e}")
    
    async def start(self):
        """Start bot"""
        try:
            logger.info("🚀 Starting bot...")
            
            logger.info("🔨 Step 1: Building app...")
            await self.build_app()
            
            # Get Railway URL
            railway_url = os.getenv("RAILWAY_PUBLIC_DOMAIN") or os.getenv("RAILWAY_STATIC_URL")
            logger.info(f"🔨 Step 2: Railway URL = {railway_url}")
            
            if not railway_url:
                logger.error("❌ RAILWAY_PUBLIC_DOMAIN not set")
                sys.exit(1)
            
            webhook_url = f"https://{railway_url}/webhook"
            port = int(os.getenv("PORT", 8080))
            
            logger.info(f"🔨 Step 3: Setting webhook to {webhook_url}")
            
            # Set webhook
            result = await self.application.bot.set_webhook(
                url=webhook_url,
                allowed_updates=["message", "callback_query"],
                max_connections=40
            )
            logger.info(f"🔨 Step 4: Webhook set result = {result}")
            
            if not result:
                logger.error("❌ Failed to set webhook")
                sys.exit(1)
            
            logger.info("🔨 Step 5: Starting application...")
            await self.application.start()
            logger.info("✅ Step 6: Application started successfully!")
            
            self.is_ready = True
            
            # Print banner
            self._print_banner(webhook_url, port)
            
            logger.info("✅ Bot is now running and ready to receive updates")
            
            # Keep running until shutdown event
            await self._shutdown_event.wait()
            
        except Exception as e:
            logger.error(f"❌ FATAL ERROR in start(): {e}", exc_info=True)
            await self.shutdown()
            sys.exit(1)
    
    def _print_banner(self, webhook_url: str, port: int):
        """Print startup banner"""
        print("\n" + "="*70)
        print("🚀 GADIS AGI ULTIMATE V3.0")
        print("="*70)
        print(f"🌐 Webhook URL: {webhook_url}")
        print(f"📡 Port: {port}")
        print(f"👤 Admin ID: {self.config.ADMIN_ID}")
        print(f"⏰ Started at: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("\n✅ Bot is running!")
        print("="*70 + "\n")
    
    async def shutdown(self):
        """Graceful shutdown"""
        logger.info("🔄 Shutting down...")
        
        # Set shutdown event to break the main loop
        self._shutdown_event.set()
        
        if self.application:
            try:
                logger.info("🔄 Stopping application...")
                await self.application.stop()
                logger.info("🔄 Shutting down application...")
                await self.application.shutdown()
                logger.info("✅ Application stopped")
            except Exception as e:
                logger.error(f"❌ Error stopping application: {e}")
        
        logger.info("✅ Shutdown complete")
    
    def get_uptime(self) -> str:
        """Get bot uptime"""
        delta = datetime.now() - self.start_time
        hours = delta.total_seconds() / 3600
        minutes = (delta.total_seconds() / 60) % 60
        
        if hours < 1:
            return f"{int(minutes)} menit"
        return f"{hours:.1f} jam"


# ================= MAIN =================
async def main():
    """Main entry point"""
    logger.info("="*50)
    logger.info("🚀 STARTING GADIS AGI BOT")
    logger.info("="*50)
    
    bot = SimpleBot()
    
    try:
        await bot.start()
    except KeyboardInterrupt:
        logger.info("📟 Received keyboard interrupt")
        await bot.shutdown()
    except Exception as e:
        logger.critical(f"💥 Fatal error: {e}", exc_info=True)
        await bot.shutdown()
        sys.exit(1)
    finally:
        logger.info("="*50)
        logger.info("🏁 BOT STOPPED")
        logger.info("="*50)


if __name__ == "__main__":
    asyncio.run(main())
