#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GADIS AGI ULTIMATE V3 - PRODUCTION MAIN
Native PTB Webhook Architecture
"""

import os
import sys
import logging
import asyncio
from datetime import datetime
from pathlib import Path

from telegram import Update
from telegram.ext import Application, ContextTypes
from telegram.request import HTTPXRequest

from config import Config
from database import Database
from systems.hts_fwb_system import HTSFWBSystem, RankingSystem
from tg_bot.handlers import TelegramHandlers


# ================= LOGGING =================
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO
)
logger = logging.getLogger("GADIS_MAIN")

Config.create_dirs()


# ================= BOT CORE =================
class GadisUltimateBot:

    def __init__(self):
        self.start_time = datetime.now()
        self.config = Config
        self.application = None

        if not self.config.validate():
            raise RuntimeError("Config validation failed")

        logger.info("Initializing systems...")

        self.db = Database(Config.DB_PATH)
        self.hts_system = HTSFWBSystem(self.db)
        self.ranking = RankingSystem(self.db)
        self.handlers = TelegramHandlers(self)

        logger.info("Core systems initialized")

    async def build_app(self):
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

        await self.handlers.setup(self.application)

        self.application.add_error_handler(self.error_handler)

        logger.info("Application built")

    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE):
        """Global error handler"""
        logger.error(f"Unhandled exception: {context.error}", exc_info=context.error)
        
        # Optional: notify admin
        if self.config.ADMIN_ID:
            try:
                await context.bot.send_message(
                    chat_id=self.config.ADMIN_ID,
                    text=f"⚠️ Bot Error: {str(context.error)[:200]}"
                )
            except:
                pass

    async def run(self):
        try:
            await self.build_app()

            railway_url = os.getenv("RAILWAY_PUBLIC_DOMAIN") or os.getenv("RAILWAY_STATIC_URL")
            if not railway_url:
                raise RuntimeError("RAILWAY_PUBLIC_DOMAIN not set")

            webhook_url = f"https://{railway_url}/webhook"
            port = int(os.getenv("PORT", 8080))

            logger.info(f"Starting webhook server on port {port}")
            logger.info(f"Webhook URL: {webhook_url}")

            # Start webhook
            await self.application.run_webhook(
                listen="0.0.0.0",
                port=port,
                url_path="webhook",
                webhook_url=webhook_url,
                allowed_updates=["message", "callback_query", "channel_post"]
            )

        except Exception as e:
            logger.error(f"Fatal error in run: {e}")
            await self.shutdown()
            raise

    async def shutdown(self):
        logger.info("Shutdown initiated")
        if self.application:
            await self.application.stop()
            await self.application.shutdown()
        logger.info("Shutdown complete")


# ================= MAIN =================
async def main():
    bot = GadisUltimateBot()
    try:
        await bot.run()
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt")
        await bot.shutdown()
    except Exception as e:
        logger.critical(f"Fatal error: {e}")
        await bot.shutdown()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
