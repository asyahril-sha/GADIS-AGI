#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GADIS AGI ULTIMATE V3.0 - MAIN ENTRY POINT
9 Role + MANTAN + TEMAN SMA dengan HTS/FWB System
"""

import os
import sys
import asyncio
import logging
from datetime import datetime
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from flask import Flask, request, jsonify
from telegram import Update
from telegram.ext import Application
from telegram.request import HTTPXRequest

from config import Config
from database import Database
from systems.hts_fwb_system import HTSFWBSystem, RankingSystem
from tg_bot.handlers import TelegramHandlers
from tg_bot.commands import AdditionalCommands

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

Config.create_dirs()

flask_app = Flask(__name__)


class GadisUltimateBot:
    """Main bot class"""
    
    def __init__(self):
        self.config = Config
        self.start_time = datetime.now()
        
        if not self.config.validate():
            sys.exit(1)
        
        self.db = Database(Config.DB_PATH)
        self.hts_system = HTSFWBSystem(self.db)
        self.ranking = RankingSystem(self.db)
        self.handlers = TelegramHandlers(self)
        self.app = None
        self.is_ready = False
        
        logger.info("✅ Bot initialized")
    
    async def initialize(self):
        """Initialize bot application"""
        request = HTTPXRequest(
            connection_pool_size=20,
            connect_timeout=60,
            read_timeout=60,
            write_timeout=60
        )
        
        self.app = (
            Application.builder()
            .token(self.config.TELEGRAM_TOKEN)
            .request(request)
            .build()
        )
        
        await self.handlers.setup(self.app)
        await self.app.initialize()
        self.is_ready = True
        
        logger.info("✅ Application initialized")
        return self.app


bot = GadisUltimateBot()


# ===== FLASK ROUTES =====

@flask_app.route('/webhook', methods=['POST'])
def webhook():
    """Webhook endpoint untuk Telegram"""
    if not bot.is_ready:
        return jsonify({'error': 'Bot not ready'}), 503
    
    try:
        update_data = request.get_json(force=True)
        update = Update.de_json(update_data, bot.app.bot)
        
        asyncio.run_coroutine_threadsafe(
            bot.app.process_update(update),
            asyncio.get_event_loop()
        )
        
        return 'OK', 200
    except Exception as e:
        logger.error(f"Webhook error: {e}")
        return jsonify({'error': str(e)}), 500


@flask_app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'bot_ready': bot.is_ready,
        'version': '3.0',
        'timestamp': datetime.now().isoformat()
    })


@flask_app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'GADIS AGI ULTIMATE V3.0 is running!',
        'version': '3.0',
        'features': [
            '9 Role (termasuk MANTAN dan TEMAN SMA)',
            'HTS/FWB System dengan Unique ID',
            'TOP 10 Ranking',
            'Level 1-12 + Reset ke 7'
        ],
        'endpoints': ['/health', '/webhook']
    })


# ===== MAIN =====

async def setup():
    """Setup bot dan webhook"""
    global bot
    
    await bot.initialize()
    
    railway_url = os.getenv('RAILWAY_PUBLIC_DOMAIN') or os.getenv('RAILWAY_STATIC_URL')
    if railway_url:
        webhook_url = f"https://{railway_url}/webhook"
        await bot.app.bot.set_webhook(url=webhook_url)
        logger.info(f"✅ Webhook set to {webhook_url}")
    
    return bot


def run():
    """Run the bot"""
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
    print("\n" + "="*60)
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(setup())
    
    port = int(os.getenv('PORT', 8080))
    print(f"\n🌐 Starting web server on port {port}")
    print(f"📡 Webhook endpoint: /webhook")
    print(f"💚 Health check: /health")
    print("\n" + "="*60)
    print("✅ Bot is running!")
    print("="*60 + "\n")
    
    flask_app.run(host='0.0.0.0', port=port, debug=False)


if __name__ == "__main__":
    run()
