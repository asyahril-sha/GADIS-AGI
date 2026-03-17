import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class Config:
    """Konfigurasi bot ultimate"""
    
    # ===== TOKENS =====
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
    ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
    
    # ===== DATABASE =====
    DB_PATH = os.getenv("DB_PATH", "data/gadis.db")
    MEMORY_DB_PATH = os.getenv("MEMORY_DB_PATH", "data/memory.db")
    
    # ===== AI SETTINGS =====
    AI_TEMPERATURE = float(os.getenv("AI_TEMPERATURE", "0.95"))
    AI_MAX_TOKENS = int(os.getenv("AI_MAX_TOKENS", "600"))
    AI_TIMEOUT = int(os.getenv("AI_TIMEOUT", "30"))
    
    # ===== RATE LIMIT =====
    MAX_MESSAGES_PER_MINUTE = int(os.getenv("MAX_MESSAGES_PER_MINUTE", "15"))
    
    # ===== LEVELING =====
    START_LEVEL = 1
    TARGET_LEVEL = 12
    RESET_LEVEL_AFTER_12 = 7
    MESSAGES_PER_LEVEL = 10
    
    # ===== ROLE COUNT =====
    ROLES = [
        "ipar", "teman_kantor", "janda", "pelakor", 
        "istri_orang", "pdkt", "sepupu", "mantan", "teman_sma"
    ]
    
    @classmethod
    def validate(cls):
        if not cls.TELEGRAM_TOKEN:
            print("❌ TELEGRAM_TOKEN tidak ditemukan")
            return False
        if not cls.DEEPSEEK_API_KEY:
            print("❌ DEEPSEEK_API_KEY tidak ditemukan")
            return False
        return True
    
    @classmethod
    def create_dirs(cls):
        Path("data").mkdir(exist_ok=True)
        Path("logs").mkdir(exist_ok=True)
        Path("memory").mkdir(exist_ok=True)
