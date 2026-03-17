"""
TELEGRAM PACKAGE - Inisialisasi semua handlers
"""

from tg_bot.handlers import TelegramHandlers
from tg_bot.commands import AdditionalCommands

__all__ = [
    'TelegramHandlers',
    'AdditionalCommands'
]
