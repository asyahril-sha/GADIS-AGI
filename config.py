"""
KONFIGURASI BOT - Semua pengaturan dalam satu tempat
"""

import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

class Config:
    """Konfigurasi bot ultimate"""
    
    # ===== TOKEN & API =====
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
    
    # ===== LEVELING SYSTEM =====
    START_LEVEL = 1
    TARGET_LEVEL = 12
    RESET_LEVEL_AFTER_12 = 7
    MESSAGES_PER_LEVEL = 10  # 10 pesan = naik 1 level
    
    # ===== 9 ROLE PREMIUM =====
    ROLES = [
        "ipar",              # Saudara ipar
        "teman_kantor",      # Rekan kerja
        "janda",             # Janda muda
        "pelakor",           # Perebut laki orang
        "istri_orang",       # Istri orang lain
        "pdkt",              # Pendekatan
        "sepupu",            # Hubungan keluarga
        "mantan",            # Mantan pacar
        "teman_sma"          # Teman SMA
    ]
    
    # ===== DOMINANCE LEVELS =====
    DOMINANCE_LEVELS = {
        1: "Patuh - Manut, menurut",
        2: "Switch - Bisa dua arah",
        3: "Dominan - Memegang kendali",
        4: "Sangat Dominan - Kontrol penuh",
        5: "Agresif - Kasar, BDSM"
    }
    
    # ===== PUBLIC SEX LOCATIONS =====
    PUBLIC_LOCATIONS = [
        "toilet umum",
        "mobil",
        "taman kota",
        "bioskop",
        "pantai",
        "lift",
        "tangga darurat",
        "balkon hotel",
        "kamar mandi pesawat",
        "belakang gedung"
    ]

    # ===== AI INFRA SETTINGS =====
    REQUEST_QUEUE_MAX_CONCURRENT = int(os.getenv("REQUEST_QUEUE_MAX_CONCURRENT", "3"))
    EMOTIONAL_UPDATE_INTERVAL = int(os.getenv("EMOTIONAL_UPDATE_INTERVAL", "300"))  # 5 menit
    MEMORY_CONSOLIDATION_INTERVAL = int(os.getenv("MEMORY_CONSOLIDATION_INTERVAL", "3600"))  # 1 jam
    STATE_SAVE_INTERVAL = int(os.getenv("STATE_SAVE_INTERVAL", "1800"))  # 30 menit
    
    @classmethod
    def validate(cls):
        """Validasi konfigurasi penting"""
        if not cls.TELEGRAM_TOKEN:
            print("❌ ERROR: TELEGRAM_TOKEN tidak ditemukan di .env")
            return False
        if not cls.DEEPSEEK_API_KEY:
            print("❌ ERROR: DEEPSEEK_API_KEY tidak ditemukan di .env")
            return False
        return True
    
    @classmethod
    def create_dirs(cls):
        """Buat folder yang diperlukan"""
        Path("data").mkdir(exist_ok=True)
        Path("logs").mkdir(exist_ok=True)
        Path("memory").mkdir(exist_ok=True)
        print("✅ Folders created")
