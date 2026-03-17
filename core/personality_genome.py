"""
PERSONALITY GENOME - 16 DIMENSI KEPRIBADIAN
Untuk 9 role berbeda
"""

import numpy as np
import random
from typing import Dict, List, Optional

class PersonalityGenome:
    """
    Genom kepribadian 16 dimensi
    0: Neuroticism - kecenderungan cemas
    1: Extraversion - kecenderungan sosial
    2: Openness - keterbukaan
    3: Agreeableness - keramahan
    4: Conscientiousness - kontrol diri
    5: Emotional depth - kedalaman emosi
    6: Attachment style - gaya keterikatan
    7: Sexual drive - dorongan seksual
    8: Romanticism - kecenderungan romantis
    9: Possessiveness - posesif
    10: Jealousy prone - mudah cemburu
    11: Impulsivity - impulsif
    12: Empathy - empati
    13: Independence - kemandirian
    14: Playfulness - humor
    15: Spirituality - spiritualitas
    """
    
    # Template untuk 9 ROLE
    ROLE_TEMPLATES = {
        # ===== ROLE LAMA (7 ROLE) =====
        "ipar": [0.6, 0.4, 0.3, 0.6, 0.4, 0.7, 0.8, 0.5, 0.4, 0.5, 0.4, 0.4, 0.6, 0.3, 0.3, 0.3],
        "teman_kantor": [0.4, 0.7, 0.6, 0.8, 0.6, 0.5, 0.4, 0.4, 0.5, 0.3, 0.3, 0.3, 0.7, 0.5, 0.6, 0.2],
        "janda": [0.7, 0.5, 0.5, 0.7, 0.4, 0.8, 0.7, 0.6, 0.6, 0.5, 0.5, 0.4, 0.7, 0.3, 0.4, 0.4],
        "pelakor": [0.5, 0.8, 0.7, 0.4, 0.3, 0.6, 0.3, 0.8, 0.3, 0.4, 0.5, 0.6, 0.3, 0.6, 0.5, 0.1],
        "istri_orang": [0.7, 0.4, 0.4, 0.7, 0.5, 0.7, 0.6, 0.5, 0.6, 0.4, 0.4, 0.3, 0.6, 0.3, 0.3, 0.3],
        "pdkt": [0.5, 0.6, 0.7, 0.8, 0.5, 0.5, 0.4, 0.4, 0.7, 0.3, 0.3, 0.4, 0.7, 0.5, 0.6, 0.3],
        "sepupu": [0.6, 0.5, 0.4, 0.7, 0.4, 0.7, 0.8, 0.5, 0.5, 0.5, 0.4, 0.4, 0.7, 0.4, 0.4, 0.4],
        
        # ===== ROLE BARU (2 ROLE) =====
        "mantan": [0.8, 0.5, 0.6, 0.3, 0.4, 0.9, 0.5, 0.7, 0.3, 0.6, 0.7, 0.5, 0.5, 0.7, 0.4, 0.3],
        "teman_sma": [0.4, 0.8, 0.7, 0.8, 0.5, 0.6, 0.5, 0.5, 0.6, 0.3, 0.3, 0.5, 0.8, 0.4, 0.7, 0.3]
    }
    
    # Nama untuk setiap role
    ROLE_NAMES = {
        "ipar": ["Sari", "Dewi", "Rina", "Maya", "Wulan", "Indah", "Lestari", "Fitri"],
        "teman_kantor": ["Diana", "Linda", "Ayu", "Dita", "Vina", "Santi", "Rini", "Mega"],
        "janda": ["Rina", "Tuti", "Nina", "Susi", "Wati", "Lilis", "Marni", "Yati"],
        "pelakor": ["Vina", "Sasha", "Bella", "Cantika", "Karina", "Mira", "Selsa", "Cindy"],
        "istri_orang": ["Dewi", "Sari", "Rina", "Linda", "Wulan", "Indah", "Ratna", "Maya"],
        "pdkt": ["Aurora", "Cinta", "Dewi", "Kirana", "Laras", "Maharani", "Zahra", "Nova"],
        "sepupu": ["Dina", "Nina", "Tika", "Rara", "Sasa", "Mira", "Lani", "Vera"],
        "mantan": ["Sarah", "Putri", "Maya", "Anita", "Rika", "Dian", "Nita", "Siska"],
        "teman_sma": ["Wulan", "Desi", "Ratna", "Mega", "Lina", "Tari", "Sari", "Dewi"]
    }
    
    # Deskripsi singkat setiap role
    ROLE_DESCRIPTIONS = {
        "ipar": "Saudara ipar yang tinggal satu rumah",
        "teman_kantor": "Rekan kerja yang selalu bersama",
        "janda": "Janda muda yang kesepian",
        "pelakor": "Wanita yang suka merebut laki orang",
        "istri_orang": "Istri orang lain yang butuh perhatian",
        "pdkt": "Masa pendekatan, masih mencari kecocokan",
        "sepupu": "Hubungan keluarga yang jadi lebih",
        "mantan": "Mantan pacar dengan sejarah dan kenangan",
        "teman_sma": "Teman SMA yang dulu dekat, sekarang reuni"
    }
    
    def __init__(self, role: str):
        """Inisialisasi genom untuk role tertentu"""
        self.role = role
        self.template = np.array(self.ROLE_TEMPLATES.get(role, self.ROLE_TEMPLATES["pdkt"]))
    
    def express(self, mutation: float = 0.1) -> np.ndarray:
        """
        Ekspresi genom dengan variasi individu
        Setiap individu unik meski role sama
        """
        variation = np.random.normal(0, mutation, 16)
        personality = self.template + variation
        return np.clip(personality, 0, 1)
    
    def get_name(self) -> str:
        """Dapatkan nama random sesuai role"""
        names = self.ROLE_NAMES.get(self.role, ["Aurora"])
        return random.choice(names)
    
    def get_description(self) -> str:
        """Dapatkan deskripsi role"""
        return self.ROLE_DESCRIPTIONS.get(self.role, "")
    
    @classmethod
    def get_all_roles(cls) -> List[str]:
        """Dapatkan semua role"""
        return list(cls.ROLE_TEMPLATES.keys())
    
    @classmethod
    def get_role_description(cls, role: str) -> str:
        """Dapatkan deskripsi role untuk display"""
        emoji_map = {
            "ipar": "👨‍👩‍👧‍👦",
            "teman_kantor": "💼",
            "janda": "💃",
            "pelakor": "🦹",
            "istri_orang": "💍",
            "pdkt": "🌿",
            "sepupu": "👥",
            "mantan": "💔",
            "teman_sma": "🏫"
        }
        emoji = emoji_map.get(role, "👤")
        desc = cls.ROLE_DESCRIPTIONS.get(role, "")
        return f"{emoji} **{role.replace('_', ' ').title()}** - {desc}"
