#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GADIS AGI ULTIMATE V3 - PRODUCTION READY
VERSI AIOHTTP - PASTI JALAN DI RAILWAY
"""

import os
import sys
import asyncio
import logging
from datetime import datetime
from pathlib import Path

from aiohttp import web
from telegram import Update
from telegram.ext import Application, ContextTypes
from telegram.request import HTTPXRequest

from config import Config
from database import Database
from systems.hts_fwb_system import HTSFWBSystem, RankingSystem
from tg_bot.handlers import TelegramHandlers

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO
)
logger = logging.getLogger("GADIS_MAIN")

Config.create_dirs()

class SimpleBot:
    def __init__(self):
        self.config = Config
        self.start_time = datetime.now()
        self.application = None
        self.is_ready = False
        
        if not self.config.validate():
            sys.exit(1)
        
        logger.info("📦 Initializing database...")
        self.db = Database(Config.DB_PATH)
        
        logger.info("⚙️ Initializing HTS/FWB system...")
        self.hts_system = HTSFWBSystem(self.db)
        self.ranking = RankingSystem(self.db)
        
        logger.info("🎯 Initializing handlers...")
        self.handlers = TelegramHandlers(self)
        
        logger.info("✅ Bot initialized successfully")
    
    async def build_app(self):
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
        
        await self.handlers.setup(self.application)
        self.application.add_error_handler(self.error_handler)
        await self.application.initialize()
        
        logger.info("✅ Application built successfully")
    
    async def error_handler(self, update, context: ContextTypes.DEFAULT_TYPE):
        logger.error(f"❌ Error: {context.error}", exc_info=True)
    
    async def start(self):
        await self.build_app()
        
        railway_url = os.getenv("RAILWAY_PUBLIC_DOMAIN") or os.getenv("RAILWAY_STATIC_URL")
        if not railway_url:
            logger.error("❌ RAILWAY_PUBLIC_DOMAIN not set")
            sys.exit(1)
        
        webhook_url = f"https://{railway_url}/webhook"
        port = int(os.getenv("PORT", 8080))
        
        logger.info(f"📡 Setting webhook to {webhook_url}")
        await self.application.bot.delete_webhook(drop_pending_updates=True)
        
        result = await self.application.bot.set_webhook(
            url=webhook_url,
            allowed_updates=["message", "callback_query"],
            max_connections=40
        )
        logger.info(f"✅ Webhook set result: {result}")
        
        webhook_info = await self.application.bot.get_webhook_info()
        logger.info(f"📋 Webhook info: {webhook_info.url}")
        logger.info(f"📊 Pending updates: {webhook_info.pending_update_count}")
        
        await self.application.start()
        logger.info("✅ Application started")
        
        # ===== AIOHTTP SERVER =====
        async def webhook_handler(request):
            try:
                update_data = await request.json()
                logger.debug(f"📥 Webhook received")
                
                update = Update.de_json(update_data, self.application.bot)
                asyncio.create_task(self.application.process_update(update))
                
                return web.Response(text='OK')
            except Exception as e:
                logger.error(f"❌ Webhook error: {e}")
                return web.Response(status=500)
        
        app = web.Application()
        app.router.add_post('/webhook', webhook_handler)
        
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, '0.0.0.0', port)
        await site.start()
        
        logger.info(f"✅ AIOHTTP server running on port {port}")
        self.is_ready = True
        
        print("\n" + "="*70)
        print("🚀 GADIS AGI ULTIMATE V3.0")
        print("="*70)
        print(f"🌐 Webhook URL: {webhook_url}")
        print(f"📡 Port: {port}")
        print(f"👤 Admin ID: {self.config.ADMIN_ID}")
        print("\n✅ Bot is running!")
        print("="*70 + "\n")
        
        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            await self.shutdown()
    
    async def shutdown(self):
        logger.info("🔄 Shutting down...")
        if self.application:
            await self.application.stop()
            await self.application.shutdown()
        logger.info("✅ Shutdown complete")

async def main():
    bot = SimpleBot()
    try:
        await bot.start()
    except KeyboardInterrupt:
        await bot.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
