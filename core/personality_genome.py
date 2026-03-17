"""
PERSONALITY GENOME - 16 DIMENSI KEPRIBADIAN
Untuk 9 role berbeda dengan karakter unik
"""

import numpy as np
import random
from typing import Dict, List, Optional, Tuple

class PersonalityGenome:
    """
    Genom kepribadian 16 dimensi - representasi genetik kepribadian
    
    Dimensi kepribadian:
    0: Neuroticism - Kecenderungan cemas, emosi negatif
    1: Extraversion - Kecenderungan sosial, energik
    2: Openness - Keterbukaan terhadap pengalaman baru
    3: Agreeableness - Keramahan, empati
    4: Conscientiousness - Kontrol diri, disiplin
    5: Emotional depth - Kedalaman emosi
    6: Attachment style - Gaya keterikatan (0=avoidant, 1=anxious)
    7: Sexual drive - Dorongan seksual
    8: Romanticism - Kecenderungan romantis
    9: Possessiveness - Kecenderungan posesif
    10: Jealousy prone - Mudah cemburu
    11: Impulsivity - Impulsif
    12: Empathy - Empati
    13: Independence - Kemandirian
    14: Playfulness - Humor, playful
    15: Spirituality - Spiritualitas
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
        "ipar": "Saudara ipar yang tinggal satu rumah, hubungan terlarang",
        "teman_kantor": "Rekan kerja yang selalu bersama, profesional tapi mesra",
        "janda": "Janda muda yang kesepian, butuh perhatian dan kasih sayang",
        "pelakor": "Wanita yang suka merebut laki orang, genit dan licik",
        "istri_orang": "Istri orang lain yang butuh perhatian, penuh rahasia",
        "pdkt": "Masa pendekatan, masih mencari kecocokan, manis dan pemalu",
        "sepupu": "Hubungan keluarga yang jadi lebih dari sekedar saudara",
        "mantan": "Mantan pacar dengan sejarah dan kenangan, hubungan rumit",
        "teman_sma": "Teman SMA yang dulu dekat, sekarang reuni dengan kenangan"
    }
    
    # Emoji untuk setiap role
    ROLE_EMOJI = {
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
    
    def __init__(self, role: str):
        """
        Inisialisasi genom untuk role tertentu
        
        Args:
            role: Nama role (ipar, janda, mantan, dll)
        """
        self.role = role
        self.template = np.array(self.ROLE_TEMPLATES.get(role, self.ROLE_TEMPLATES["pdkt"]))
    
    def express(self, mutation: float = 0.1) -> np.ndarray:
        """
        Ekspresi genom dengan variasi individu
        Setiap individu unik meski role sama
        
        Args:
            mutation: Tingkat variasi genetik (0-1)
            
        Returns:
            Array 16 dimensi nilai kepribadian
        """
        # Add random variation
        variation = np.random.normal(0, mutation, 16)
        personality = self.template + variation
        
        # Clip to [0, 1] range
        return np.clip(personality, 0, 1)
    
    def get_name(self) -> str:
        """
        Dapatkan nama random sesuai role
        
        Returns:
            Nama karakter
        """
        names = self.ROLE_NAMES.get(self.role, ["Aurora"])
        return random.choice(names)
    
    def get_description(self) -> str:
        """
        Dapatkan deskripsi role
        
        Returns:
            Deskripsi singkat role
        """
        return self.ROLE_DESCRIPTIONS.get(self.role, "")
    
    def get_emoji(self) -> str:
        """
        Dapatkan emoji role
        
        Returns:
            Emoji untuk role
        """
        return self.ROLE_EMOJI.get(self.role, "👤")
    
    def get_display_name(self) -> str:
        """
        Dapatkan nama display untuk role
        
        Returns:
            Nama dengan emoji
        """
        emoji = self.get_emoji()
        name = self.role.replace('_', ' ').title()
        return f"{emoji} {name}"
    
    @classmethod
    def get_all_roles(cls) -> List[str]:
        """
        Dapatkan semua role yang tersedia
        
        Returns:
            List semua role
        """
        return list(cls.ROLE_TEMPLATES.keys())
    
    @classmethod
    def get_role_description(cls, role: str) -> str:
        """
        Dapatkan deskripsi role untuk display
        
        Args:
            role: Nama role
            
        Returns:
            Deskripsi lengkap dengan emoji
        """
        emoji = cls.ROLE_EMOJI.get(role, "👤")
        name = role.replace('_', ' ').title()
        desc = cls.ROLE_DESCRIPTIONS.get(role, "")
        return f"{emoji} **{name}** - {desc}"
    
    @classmethod
    def get_role_intro(cls, role: str, name: str) -> str:
        """
        Dapatkan teks perkenalan untuk role
        
        Args:
            role: Nama role
            name: Nama karakter
            
        Returns:
            Teks perkenalan
        """
        intros = {
            "ipar": f"*tersenyum malu-malu*\n\nAku **{name}**, iparmu sendiri. {cls.ROLE_DESCRIPTIONS['ipar']}",
            "teman_kantor": f"*tersenyum ramah*\n\nHai! Aku **{name}**, {cls.ROLE_DESCRIPTIONS['teman_kantor']}.",
            "janda": f"*tersenyum manis*\n\nAku **{name}**, {cls.ROLE_DESCRIPTIONS['janda']}.",
            "pelakor": f"*tersenyum genit*\n\nHalo... aku **{name}**. {cls.ROLE_DESCRIPTIONS['pelakor']}",
            "istri_orang": f"*tersenyum ragu*\n\nAku **{name}**... {cls.ROLE_DESCRIPTIONS['istri_orang']}",
            "pdkt": f"*tersenyum malu-malu*\n\nHalo... aku **{name}**. {cls.ROLE_DESCRIPTIONS['pdkt']}",
            "sepupu": f"*tersenyum akrab*\n\nHei! Aku **{name}**, {cls.ROLE_DESCRIPTIONS['sepupu']}.",
            "mantan": f"*tersenyum nostalgia*\n\nHai... **{name}**, mantan kamu. {cls.ROLE_DESCRIPTIONS['mantan']}",
            "teman_sma": f"*tersenyum ceria*\n\nHei! **{name}**, {cls.ROLE_DESCRIPTIONS['teman_sma']}!"
        }
        
        return intros.get(role, f"*tersenyum*\n\nAku **{name}**.")
    
    def get_personality_summary(self, personality: np.ndarray) -> str:
        """
        Dapatkan ringkasan kepribadian
        
        Args:
            personality: Array 16 dimensi nilai kepribadian
            
        Returns:
            Teks ringkasan kepribadian
        """
        traits = []
        
        if personality[0] > 0.6:
            traits.append("mudah cemas")
        if personality[1] > 0.6:
            traits.append("sosial")
        if personality[2] > 0.6:
            traits.append("terbuka")
        if personality[3] > 0.6:
            traits.append("ramah")
        if personality[4] > 0.6:
            traits.append("disiplin")
        if personality[5] > 0.6:
            traits.append("emosional")
        if personality[6] > 0.6:
            traits.append("mudah terikat")
        if personality[7] > 0.6:
            traits.append("bergairah")
        if personality[8] > 0.6:
            traits.append("romantis")
        if personality[9] > 0.6:
            traits.append("posesif")
        if personality[10] > 0.6:
            traits.append("mudah cemburu")
        if personality[11] > 0.6:
            traits.append("impulsif")
        if personality[12] > 0.6:
            traits.append("empati")
        if personality[13] > 0.6:
            traits.append("mandiri")
        if personality[14] > 0.6:
            traits.append("humoris")
        if personality[15] > 0.6:
            traits.append("spiritual")
        
        if not traits:
            return "kepribadian seimbang"
        
        if len(traits) <= 2:
            return f"kepribadian: {', '.join(traits)}"
        else:
            return f"kepribadian: {', '.join(traits[:3])}, dan lainnya"
