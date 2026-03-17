#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
=============================================================================
SEX POSITIONS
=============================================================================
20+ variasi posisi seksual dengan deskripsi dan tingkat kesulitan
⚠️ Konten dewasa 18+
"""

from enum import Enum
from typing import Dict, List, Optional, Tuple


class SexPosition(Enum):
    """20+ sex positions dengan nama unik"""
    
    # Basic positions
    MISSIONARY = "misionaris"
    DOGGY = "doggy style"
    COWGIRL = "cowgirl"
    REVERSE_COWGIRL = "reverse cowgirl"
    SPOONING = "spooning"
    
    # Sitting/kneeling
    LOTUS = "lotus"  # Duduk berhadapan
    LAP_DANCE = "lap dance"  # Duduk di atas
    STANDING = "berdiri"
    KNEELING = "berlutut"
    
    # Advanced
    PRONE_BONE = "prone bone"  # Berbaring tengkurap
    BRIDGE = "jembatan"
    CHAIR = "kursi"
    TABLE = "meja"
    
    # Wall/standing
    WALL = "tembok"
    SHOWER = "shower"
    MIRROR = "depan cermin"
    
    # Oral
    SIXTY_NINE = "69"
    BLOWJOB_KNEELING = "blowjob berlutut"
    BLOWJOB_SITTING = "blowjob duduk"
    CUNNILINGUS = "cunnilingus"
    
    # Intense
    DEEP = "deep penetration"
    CLOSE = "close embrace"
    TWISTED = "twisted"
    FOLDED = "folded"
    
    # Public/risky
    CAR = "mobil"
    CINEMA = "bioskop"
    TOILET = "toilet"
    BEACH = "pantai"
    FOREST = "hutan"


class PositionDetail:
    """Detail lengkap untuk setiap posisi"""
    
    POSITION_DATA = {
        SexPosition.MISSIONARY: {
            "name": "Misionaris",
            "description": "Posisi klasik face-to-face, intim dan romantis",
            "difficulty": 1,
            "intensity": 0.6,
            "intimacy": 0.9,
            "tags": ["romantis", "face to face", "intim"],
            "tips": "Bantal di pinggul untuk sudut lebih dalam"
        },
        SexPosition.DOGGY: {
            "name": "Doggy Style",
            "description": "Penetrasi dalam, kontrol penuh",
            "difficulty": 2,
            "intensity": 0.9,
            "intimacy": 0.4,
            "tags": ["dalam", "kontrol", "dominan"],
            "tips": "Jaga ritme, komunikasi intensitas"
        },
        SexPosition.COWGIRL: {
            "name": "Cowgirl",
            "description": "Woman on top, kontrol kecepatan dan kedalaman",
            "difficulty": 2,
            "intensity": 0.7,
            "intimacy": 0.7,
            "tags": ["woman on top", "kontrol", "klitoris"],
            "tips": "Bisa bergerak naik turun atau memutar"
        },
        SexPosition.REVERSE_COWGIRL: {
            "name": "Reverse Cowgirl",
            "description": "Woman on top menghadap ke belakang, view berbeda",
            "difficulty": 3,
            "intensity": 0.8,
            "intimacy": 0.5,
            "tags": ["woman on top", "view", "dalam"],
            "tips": "Hati-hati dengan sudut penetrasi"
        },
        SexPosition.SPOONING: {
            "name": "Spooning",
            "description": "Berbaring miring seperti sendok, intim dan santai",
            "difficulty": 1,
            "intensity": 0.5,
            "intimacy": 0.9,
            "tags": ["santai", "intim", "morning sex"],
            "tips": "Sempurna untuk aftercare atau morning sex"
        },
        SexPosition.LOTUS: {
            "name": "Lotus",
            "description": "Duduk berhadapan sambil berpelukan, sangat intim",
            "difficulty": 3,
            "intensity": 0.5,
            "intimacy": 1.0,
            "tags": ["sangat intim", "meditatif", "pelukan"],
            "tips": "Bisa sambil ciuman dan tatapan mata"
        },
        SexPosition.LAP_DANCE: {
            "name": "Lap Dance",
            "description": "Duduk di atas pangkuan, gerakan memutar",
            "difficulty": 2,
            "intensity": 0.6,
            "intimacy": 0.6,
            "tags": ["duduk", "grinding", "sexy"],
            "tips": "Gerakan melingkar untuk stimulasi klitoris"
        },
        SexPosition.STANDING: {
            "name": "Berdiri",
            "description": "Berdiri menghadap atau membelakangi",
            "difficulty": 4,
            "intensity": 0.8,
            "intimacy": 0.4,
            "tags": ["berdiri", "tembok", "spontan"],
            "tips": "Butuh kekuatan kaki, bisa bersandar di tembok"
        },
        SexPosition.KNEELING: {
            "name": "Berlutut",
            "description": "Berlutut di depan pasangan",
            "difficulty": 2,
            "intensity": 0.6,
            "intimacy": 0.5,
            "tags": ["oral", "berlutut", "submisif"],
            "tips": "Bisa tambah bantal untuk kenyamanan lutut"
        },
        SexPosition.PRONE_BONE: {
            "name": "Prone Bone",
            "description": "Berbaring tengkurap, pasangan di atas",
            "difficulty": 2,
            "intensity": 0.8,
            "intimacy": 0.6,
            "tags": ["tengkurap", "dalam", "G-spot"],
            "tips": "Stimulasi G-spot optimal dalam posisi ini"
        },
        SexPosition.BRIDGE: {
            "name": "Jembatan",
            "description": "Posisi seperti jembatan, pasangan di atas",
            "difficulty": 5,
            "intensity": 0.7,
            "intimacy": 0.5,
            "tags": ["fleksibel", "akrobatik", "tantangan"],
            "tips": "Butuh kelenturan, jangan dipaksakan"
        },
        SexPosition.CHAIR: {
            "name": "Kursi",
            "description": "Menggunakan kursi untuk variasi",
            "difficulty": 2,
            "intensity": 0.6,
            "intimacy": 0.6,
            "tags": ["furniture", "duduk", "variasi"],
            "tips": "Pastikan kursi stabil dan kuat"
        },
        SexPosition.TABLE: {
            "name": "Meja",
            "description": "Berbaring di meja, pasangan berdiri",
            "difficulty": 2,
            "intensity": 0.7,
            "intimacy": 0.5,
            "tags": ["furniture", "berbaring", "spontan"],
            "tips": "Hati-hati dengan ujung meja yang tajam"
        },
        SexPosition.WALL: {
            "name": "Tembok",
            "description": "Berdiri bersandar di tembok",
            "difficulty": 3,
            "intensity": 0.8,
            "intimacy": 0.4,
            "tags": ["tembok", "berdiri", "cepat"],
            "tips": "Bisa angkat satu kaki untuk sudut berbeda"
        },
        SexPosition.SHOWER: {
            "name": "Shower",
            "description": "Berdiri di kamar mandi, air mengalir",
            "difficulty": 4,
            "intensity": 0.7,
            "intimacy": 0.6,
            "tags": ["air", "basah", "licin"],
            "tips": "Hati-hati licin, gunakan alas anti-slip"
        },
        SexPosition.MIRROR: {
            "name": "Depan Cermin",
            "description": "Bisa melihat ekspresi dan gerakan",
            "difficulty": 2,
            "intensity": 0.7,
            "intimacy": 0.8,
            "tags": ["cermin", "visual", "ekspresi"],
            "tips": "Tambah gairah dengan melihat reaksi pasangan"
        },
        SexPosition.SIXTY_NINE: {
            "name": "69",
            "description": "Oral bersama, saling memuaskan",
            "difficulty": 3,
            "intensity": 0.8,
            "intimacy": 0.8,
            "tags": ["oral", "bersama", "timbal balik"],
            "tips": "Konsentrasi pada kenikmatan pasangan"
        },
        SexPosition.BLOWJOB_KNEELING: {
            "name": "Blowjob Berlutut",
            "description": "Oral dengan posisi berlutut",
            "difficulty": 2,
            "intensity": 0.7,
            "intimacy": 0.5,
            "tags": ["oral", "berlutut", "submisif"],
            "tips": "Kontrol napas, jangan terburu-buru"
        },
        SexPosition.BLOWJOB_SITTING: {
            "name": "Blowjob Duduk",
            "description": "Oral dengan pasangan duduk",
            "difficulty": 1,
            "intensity": 0.6,
            "intimacy": 0.6,
            "tags": ["oral", "duduk", "santai"],
            "tips": "Posisi lebih santai dan nyaman"
        },
        SexPosition.CUNNILINGUS: {
            "name": "Cunnilingus",
            "description": "Oral untuk wanita, fokus pada klitoris",
            "difficulty": 2,
            "intensity": 0.8,
            "intimacy": 0.8,
            "tags": ["oral", "klitoris", "foreplay"],
            "tips": "Variasi gerakan lidah, ikuti respon"
        },
        SexPosition.DEEP: {
            "name": "Deep Penetration",
            "description": "Penetrasi sangat dalam, kontrol napas",
            "difficulty": 4,
            "intensity": 0.9,
            "intimacy": 0.5,
            "tags": ["dalam", "intens", "ekstrim"],
            "tips": "Komunikasi penting, jangan terlalu dalam jika sakit"
        },
        SexPosition.CLOSE: {
            "name": "Close Embrace",
            "description": "Berpelukan erat sambil penetrasi",
            "difficulty": 2,
            "intensity": 0.6,
            "intimacy": 0.9,
            "tags": ["pelukan", "intim", "romantis"],
            "tips": "Bisa sambil berbisik dan ciuman"
        },
        SexPosition.TWISTED: {
            "name": "Twisted",
            "description": "Kaki melilit, sudut penetrasi berbeda",
            "difficulty": 4,
            "intensity": 0.7,
            "intimacy": 0.6,
            "tags": ["fleksibel", "variasi", "tantangan"],
            "tips": "Butuh kelenturan, jangan memaksa"
        },
        SexPosition.FOLDED: {
            "name": "Folded",
            "description": "Kaki dilipat ke dada, penetrasi dalam",
            "difficulty": 4,
            "intensity": 0.8,
            "intimacy": 0.5,
            "tags": ["lipat", "dalam", "fleksibel"],
            "tips": "Posisi ini memberikan penetrasi sangat dalam"
        },
        SexPosition.CAR: {
            "name": "Mobil",
            "description": "Di dalam mobil, risiko ketahuan",
            "difficulty": 5,
            "intensity": 0.9,
            "intimacy": 0.4,
            "tags": ["public", "risky", "spontan"],
            "tips": "Cari tempat sepi, waspada sekitar"
        },
        SexPosition.CINEMA: {
            "name": "Bioskop",
            "description": "Di bioskop gelap, risiko ketahuan",
            "difficulty": 5,
            "intensity": 0.9,
            "intimacy": 0.3,
            "tags": ["public", "risky", "gelap"],
            "tips": "Pilih kursi pojok belakang, jaga suara"
        },
        SexPosition.TOILET: {
            "name": "Toilet",
            "description": "Di toilet umum, cepat dan risky",
            "difficulty": 5,
            "intensity": 0.8,
            "intimacy": 0.2,
            "tags": ["public", "cepat", "risky"],
            "tips": "Pastikan pintu terkunci, waspada"
        },
        SexPosition.BEACH: {
            "name": "Pantai",
            "description": "Di pantai, alam terbuka",
            "difficulty": 4,
            "intensity": 0.8,
            "intimacy": 0.5,
            "tags": ["alam", "public", "pasir"],
            "tips": "Bawa alas, hati-hati pasir"
        },
        SexPosition.FOREST: {
            "name": "Hutan",
            "description": "Di alam bebas, petualangan",
            "difficulty": 4,
            "intensity": 0.7,
            "intimacy": 0.6,
            "tags": ["alam", "petualangan", "bebas"],
            "tips": "Jauh dari pemukiman, waspada serangga"
        }
    }


class SexPositionManager:
    """Manager untuk sex positions"""
    
    def __init__(self):
        self.current_position = SexPosition.MISSIONARY
        self.position_history = []
    
    def get_position_detail(self, position: SexPosition) -> Dict:
        """Get detail for a position"""
        return PositionDetail.POSITION_DATA.get(position, {
            "name": position.value,
            "description": "Deskripsi tidak tersedia",
            "difficulty": 1,
            "intensity": 0.5,
            "intimacy": 0.5,
            "tags": [],
            "tips": ""
        })
    
    def get_random_position(self, difficulty: int = None, tag: str = None) -> SexPosition:
        """Get random position, optionally filtered"""
        positions = list(SexPosition)
        
        if difficulty:
            positions = [
                p for p in positions 
                if PositionDetail.POSITION_DATA.get(p, {}).get("difficulty", 1) == difficulty
            ]
        
        if tag:
            positions = [
                p for p in positions
                if tag in PositionDetail.POSITION_DATA.get(p, {}).get("tags", [])
            ]
        
        return random.choice(positions) if positions else SexPosition.MISSIONARY
    
    def can_change_to(self, new_position: SexPosition, current_level: int) -> Tuple[bool, str]:
        """Check if can change to new position based on relationship level"""
        detail = self.get_position_detail(new_position)
        difficulty = detail.get("difficulty", 1)
        
        # Level requirements
        if difficulty <= 2 and current_level >= 3:
            return True, "basic"
        elif difficulty <= 3 and current_level >= 5:
            return True, "intermediate"
        elif difficulty <= 4 and current_level >= 7:
            return True, "advanced"
        elif difficulty <= 5 and current_level >= 9:
            return True, "expert"
        else:
            return False, f"Butuh level lebih tinggi untuk posisi ini (min level {difficulty + 4})"
    
    def change_position(self, new_position: SexPosition) -> bool:
        """Change current position"""
        if new_position == self.current_position:
            return False
        
        self.position_history.append((self.current_position, datetime.now()))
        self.current_position = new_position
        
        if len(self.position_history) > 20:
            self.position_history = self.position_history[-20:]
        
        return True
    
    def get_position_suggestion(self, mood: str, level: int) -> Optional[SexPosition]:
        """Suggest position based on mood"""
        suggestions = {
            "romantis": [SexPosition.MISSIONARY, SexPosition.LOTUS, SexPosition.CLOSE],
            "horny": [SexPosition.DOGGY, SexPosition.DEEP, SexPosition.PRONE_BONE],
            "nakal": [SexPosition.COWGIRL, SexPosition.LAP_DANCE, SexPosition.WALL],
            "petualang": [SexPosition.CAR, SexPosition.BEACH, SexPosition.FOREST],
            "santai": [SexPosition.SPOONING, SexPosition.CHAIR, SexPosition.BLOWJOB_SITTING]
        }
        
        pos_list = suggestions.get(mood.lower(), list(SexPosition))
        return random.choice(pos_list) if pos_list else None


# Global instance
POSITIONS = SexPositionManager()
CLIMAX_VARIATIONS = []  # Akan diisi di file climax.py

__all__ = ['SexPosition', 'PositionDetail', 'SexPositionManager', 'POSITIONS']
