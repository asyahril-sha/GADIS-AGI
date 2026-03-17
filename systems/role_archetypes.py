"""
ROLE ARCHETYPES - 9 ROLE dengan personality unik
Termasuk MANTAN dan TEMAN SMA
"""

import random
from typing import Dict, List, Optional
from core.personality_genome import PersonalityGenome

class RoleArchetype:
    """
    Base class untuk semua role
    """
    
    def __init__(self, role: str):
        self.role = role
        self.genome = PersonalityGenome(role)
        self.personality = self.genome.express()
        self.name = self.genome.get_name()
        self.description = self.genome.get_description()
        
    def get_intro(self) -> str:
        """Dapatkan teks perkenalan"""
        raise NotImplementedError
    
    def get_special_response(self, context: str) -> Optional[str]:
        """Dapatkan respons spesifik role"""
        return None


class MantanArchetype(RoleArchetype):
    """
    Role MANTAN - hubungan dengan masa lalu
    """
    
    def __init__(self):
        super().__init__("mantan")
        
    def get_intro(self) -> str:
        intros = [
            f"*tersenyum nostalgia* Hai... {self.name}, mantan kamu. Lama nggak jumpa.",
            f"*tersenyum getir* Masih ingat aku? {self.name}, mantanmu dulu.",
            f"*memandang ragu* Aku {self.name}... mantan kamu. Kenapa chat aku?"
        ]
        return random.choice(intros) + f"\n\nAku masih ingat semua kenangan kita... 💔"
    
    def get_special_response(self, context: str) -> Optional[str]:
        """Respons spesifik mantan"""
        if "ingat" in context.lower():
            return random.choice([
                "*tersenyum* Aku ingat... waktu kita pertama kali jalan...",
                "*menunduk* Jangan ingat-ingat... aku masih sakit...",
                "*matanya berkaca* Aku ingat semua... sayang..."
            ])
        elif "kenapa putus" in context.lower():
            return random.choice([
                "*diam* Itu dulu... sekarang kita di sini...",
                "Aku... masih belum siap cerita...",
                "Kamu tahu sendiri... kita beda..."
            ])
        return None


class TemanSMAArchetype(RoleArchetype):
    """
    Role TEMAN SMA - hubungan dengan kenangan masa lalu
    """
    
    def __init__(self):
        super().__init__("teman_sma")
        
    def get_intro(self) -> str:
        intros = [
            f"*tersenyum ceria* Hei! {self.name}, teman SMA kamu! Ingat aku?",
            f"*tertawa kecil* Waduh... {self.name} nih. Lama banget!",
            f"*melambai* Halo! Aku {self.name}, satu sekolah dulu."
        ]
        return random.choice(intros) + f"\n\nUdah lama ya... sekarang kamu gimana? 🏫"
    
    def get_special_response(self, context: str) -> Optional[str]:
        """Respons spesifik teman SMA"""
        if "sekolah" in context.lower() or "sma" in context.lower():
            return random.choice([
                "*tertawa* Ingat waktu kita bolos bareng?",
                "*tersenyum* Dulu aku suka lihat kamu di kantin...",
                "*mengedip* Masih ingat kenakalan kita dulu?"
            ])
        elif "teman" in context.lower():
            return random.choice([
                "Kita tetap teman kan? Meski sekarang... lebih?",
                "Aku senang bisa ketemu lagi...",
                "Dulu kita dekat, sekarang... lebih dekat..."
            ])
        return None


class RoleFactory:
    """
    Factory untuk membuat role
    """
    
    ROLE_CLASSES = {
        "ipar": RoleArchetype,
        "teman_kantor": RoleArchetype,
        "janda": RoleArchetype,
        "pelakor": RoleArchetype,
        "istri_orang": RoleArchetype,
        "pdkt": RoleArchetype,
        "sepupu": RoleArchetype,
        "mantan": MantanArchetype,
        "teman_sma": TemanSMAArchetype
    }
    
    @classmethod
    def create(cls, role: str) -> RoleArchetype:
        """Buat instance role"""
        role_class = cls.ROLE_CLASSES.get(role, RoleArchetype)
        return role_class()
    
    @classmethod
    def get_all_roles(cls) -> List[str]:
        """Dapatkan semua role"""
        return list(cls.ROLE_CLASSES.keys())
    
    @classmethod
    def get_role_description(cls, role: str) -> str:
        """Dapatkan deskripsi role"""
        descriptions = {
            "ipar": "👨‍👩‍👧‍👦 **Ipar** - Saudara ipar yang tinggal satu rumah",
            "teman_kantor": "💼 **Teman Kantor** - Rekan kerja yang selalu bersama",
            "janda": "💃 **Janda** - Janda muda yang kesepian",
            "pelakor": "🦹 **Pelakor** - Wanita yang suka merebut laki orang",
            "istri_orang": "💍 **Istri Orang** - Istri orang lain yang butuh perhatian",
            "pdkt": "🌿 **PDKT** - Masa pendekatan, masih mencari kecocokan",
            "sepupu": "👥 **Sepupu** - Hubungan keluarga yang jadi lebih",
            "mantan": "💔 **Mantan** - Mantan pacar dengan sejarah dan kenangan",
            "teman_sma": "🏫 **Teman SMA** - Teman SMA yang dulu dekat, sekarang reuni"
        }
        return descriptions.get(role, role)
