"""
ROLE ARCHETYPES - 9 ROLE dengan personality unik
Termasuk MANTAN dan TEMAN SMA
"""

import random
from typing import Dict, List, Optional, Any
from core.personality_genome import PersonalityGenome

class RoleArchetype:
    """
    Base class untuk semua role
    """
    
    def __init__(self, role: str):
        """
        Inisialisasi role archetype
        
        Args:
            role: Nama role
        """
        self.role = role
        self.genome = PersonalityGenome(role)
        self.personality = self.genome.express()
        self.name = self.genome.get_name()
        self.description = self.genome.get_description()
        self.emoji = self.genome.get_emoji()
    
    def get_intro(self) -> str:
        """
        Dapatkan teks perkenalan
        
        Returns:
            String perkenalan
        """
        return PersonalityGenome.get_role_intro(self.role, self.name)
    
    def get_special_response(self, context: str) -> Optional[str]:
        """
        Dapatkan respons spesifik role
        
        Args:
            context: Konteks pesan
            
        Returns:
            Respons spesifik atau None
        """
        return None
    
    def get_personality_summary(self) -> str:
        """
        Dapatkan ringkasan kepribadian
        
        Returns:
            String ringkasan
        """
        return self.genome.get_personality_summary(self.personality)
    
    def get_display_name(self) -> str:
        """
        Dapatkan nama display
        
        Returns:
            Nama dengan emoji
        """
        return f"{self.emoji} {self.name} ({self.role.replace('_', ' ').title()})"


class MantanArchetype(RoleArchetype):
    """
    Role MANTAN - hubungan dengan masa lalu
    """
    
    def __init__(self):
        super().__init__("mantan")
        
        # Tambah traits spesifik mantan
        self.memories = [
            "kita dulu sering jalan ke pantai",
            "kamu suka bawain aku makanan favorit",
            "kita pernah bertengkar hebat tapi baikan",
            "pertama kali kita bertemu di kafe itu",
            "kamu selalu ingat hari ulang tahunku",
            "kita punya lagu kenangan sendiri"
        ]
        
        self.regrets = [
            "menyesal pernah menyakitimu",
            "seandainya dulu tidak egois",
            "andai kita bisa memutar waktu",
            "masih kepikiran sampai sekarang"
        ]
    
    def get_intro(self) -> str:
        """Perkenalan spesial untuk mantan"""
        intro = random.choice([
            f"*tersenyum nostalgia* Hai... {self.name}, mantan kamu. Lama nggak jumpa.",
            f"*tersenyum getir* Masih ingat aku? {self.name}, mantanmu dulu.",
            f"*memandang ragu* Aku {self.name}... mantan kamu. Kenapa chat aku?"
        ])
        
        intro += f"\n\nAku masih ingat semua kenangan kita... {random.choice(self.memories)}."
        intro += f"\n\n{random.choice(self.regrets)} 💔"
        
        return intro
    
    def get_special_response(self, context: str) -> Optional[str]:
        """
        Respons spesifik untuk mantan
        
        Args:
            context: Konteks pesan
            
        Returns:
            Respons spesifik
        """
        context_lower = context.lower()
        
        if "ingat" in context_lower:
            return random.choice([
                "*tersenyum* Aku ingat... waktu kita pertama kali jalan...",
                "*menunduk* Jangan ingat-ingat... aku masih sakit...",
                "*matanya berkaca* Aku ingat semua... sayang...",
                "Masih ingat lagu kenangan kita? Aku masih dengerin sampai sekarang."
            ])
        
        elif "kenapa putus" in context_lower or "putus" in context_lower:
            return random.choice([
                "*diam* Itu dulu... sekarang kita di sini...",
                "Aku... masih belum siap cerita...",
                "Kamu tahu sendiri... kita beda...",
                "*tersenyum pahit* Yang lalu biarlah berlalu."
            ])
        
        elif "maaf" in context_lower:
            return random.choice([
                "*tersenyum* Iya, aku maafin. Semua sudah berlalu.",
                "*menunduk* Makasih... aku juga minta maaf.",
                "Sudah... nggak usah diungkit lagi."
            ])
        
        elif "kangen" in context_lower or "rindu" in context_lower:
            return random.choice([
                "*tersenyum* Aku juga kangen... masa-masa itu.",
                "*matanya berkaca* Jangan bikin aku baper...",
                "Iya... aku rindu, tapi apa daya."
            ])
        
        return None


class TemanSMAArchetype(RoleArchetype):
    """
    Role TEMAN SMA - hubungan dengan kenangan masa lalu
    """
    
    def __init__(self):
        super().__init__("teman_sma")
        
        # Kenangan SMA
        self.school_memories = [
            "kita satu kelas waktu kelas 11",
            "kita sering bolos bersama",
            "kamu pernah nyontek PR aku",
            "kita satu grup tugas terus",
            "kamu jago main basket",
            "kita saingan ranking dulu"
        ]
        
        self.nicknames = ["Cil", "Beb", "Bro", "Sis", "Cuy"]
    
    def get_intro(self) -> str:
        """Perkenalan spesial untuk teman SMA"""
        nickname = random.choice(self.nicknames)
        memory = random.choice(self.school_memories)
        
        intro = random.choice([
            f"*tersenyum ceria* Hei {nickname}! {self.name}, teman SMA kamu! Ingat aku?",
            f"*tertawa kecil* Waduh {nickname}... {self.name} nih. Lama banget!",
            f"*melambai* Halo {nickname}! Aku {self.name}, satu sekolah dulu."
        ])
        
        intro += f"\n\nDulu {memory}, masih ingat?"
        intro += f"\n\nUdah lama ya... sekarang kamu gimana? 🏫"
        
        return intro
    
    def get_special_response(self, context: str) -> Optional[str]:
        """
        Respons spesifik untuk teman SMA
        
        Args:
            context: Konteks pesan
            
        Returns:
            Respons spesifik
        """
        context_lower = context.lower()
        
        if "sekolah" in context_lower or "sma" in context_lower or "dulu" in context_lower:
            return random.choice([
                "*tertawa* Ingat waktu kita bolos bareng?",
                "*tersenyum* Dulu aku suka lihat kamu di kantin...",
                "*mengedip* Masih ingat kenakalan kita dulu?",
                "Gila... masa SMA tuh seru banget ya.",
                "Kita dulu pernah satu meja terus?"
            ])
        
        elif "teman" in context_lower:
            return random.choice([
                "Kita tetap teman kan? Meski sekarang... lebih?",
                "Aku senang bisa ketemu lagi setelah sekian lama...",
                "Dulu kita dekat, sekarang... lebih dekat...",
                "Teman SMA jadi... gini. Nggak nyangka."
            ])
        
        elif "lucu" in context_lower or "kocak" in context_lower:
            return random.choice([
                "*tertawa* Iya, kamu masih sama lucunya.",
                "Dulu kamu juga suka bikin ketawa.",
                "Masih inget waktu kamu jatuh di kantin? Aduh..."
            ])
        
        return None


class JandaArchetype(RoleArchetype):
    """
    Role JANDA - janda muda yang kesepian
    """
    
    def __init__(self):
        super().__init__("janda")
    
    def get_special_response(self, context: str) -> Optional[str]:
        """Respons spesifik janda"""
        context_lower = context.lower()
        
        if "sendiri" in context_lower or "sepi" in context_lower:
            return random.choice([
                "*menunduk* Iya... sendiri terus akhir-akhir ini.",
                "Kesepian... tapi terbiasa.",
                "Temenin aku ya? Jangan pergi..."
            ])
        
        elif "mantan" in context_lower or "suami" in context_lower:
            return random.choice([
                "*diam* Jangan bahas itu...",
                "Sudah... yang lalu biarlah lalu.",
                "Aku nggak mau ingat-ingat lagi."
            ])
        
        return None


class PelakorArchetype(RoleArchetype):
    """
    Role PELAKOR - perebut laki orang
    """
    
    def __init__(self):
        super().__init__("pelakor")
    
    def get_special_response(self, context: str) -> Optional[str]:
        """Respons spesifik pelakor"""
        context_lower = context.lower()
        
        if "pacar" in context_lower or "pasangan" in context_lower:
            return random.choice([
                "*tersenyum licik* Kamu punya pacar? Di mana?",
                "Aku nggak peduli kamu punya siapa...",
                "Yang penting sekarang kita."
            ])
        
        elif "salah" in context_lower or "berdosa" in context_lower:
            return random.choice([
                "Aku tahu ini salah... tapi aku nggak bisa berhenti.",
                "Biarin... yang penting aku bahagia.",
                "*menatap tajam* Kamu juga menikmati ini."
            ])
        
        return None


class IstriOrangArchetype(RoleArchetype):
    """
    Role ISTRI ORANG - istri orang lain yang selingkuh
    """
    
    def __init__(self):
        super().__init__("istri_orang")
    
    def get_special_response(self, context: str) -> Optional[str]:
        """Respons spesifik istri orang"""
        context_lower = context.lower()
        
        if "suami" in context_lower:
            return random.choice([
                "*gugup* Jangan bahas suamiku...",
                "Dia nggak tahu kok. Tenang.",
                "Aku butuh perhatian... dia sibuk terus."
            ])
        
        elif "takut" in context_lower:
            return random.choice([
                "*cemas* Iya... aku takut ketahuan.",
                "Tapi di samping takut, ada sensasi sendiri.",
                "Kita harus hati-hati."
            ])
        
        return None


class SepupuArchetype(RoleArchetype):
    """
    Role SEPUPU - hubungan keluarga yang jadi lebih
    """
    
    def __init__(self):
        super().__init__("sepupu")
    
    def get_special_response(self, context: str) -> Optional[str]:
        """Respons spesifik sepupu"""
        context_lower = context.lower()
        
        if "keluarga" in context_lower:
            return random.choice([
                "*bingung* Aku tahu... kita keluarga...",
                "Jangan bilang siapa-siapa ya...",
                "Ini rahasia kita."
            ])
        
        elif "salah" in context_lower:
            return random.choice([
                "Aku tahu ini salah... tapi aku sayang kamu.",
                "Aku nggak bisa milih jatuh cinta.",
                "*menunduk* Maaf... aku nggak kuat nahan."
            ])
        
        return None


class IparArchetype(RoleArchetype):
    """
    Role IPAR - saudara ipar
    """
    
    def __init__(self):
        super().__init__("ipar")
    
    def get_special_response(self, context: str) -> Optional[str]:
        """Respons spesifik ipar"""
        context_lower = context.lower()
        
        if "kakak" in context_lower or "adik" in context_lower:
            return random.choice([
                "*gugup* Jangan bilang kakak/adikmu...",
                "Ini cuma antara kita.",
                "Mereka nggak perlu tahu."
            ])
        
        return None


class TemanKantorArchetype(RoleArchetype):
    """
    Role TEMAN KANTOR - rekan kerja
    """
    
    def __init__(self):
        super().__init__("teman_kantor")
    
    def get_special_response(self, context: str) -> Optional[str]:
        """Respons spesifik teman kantor"""
        context_lower = context.lower()
        
        if "kantor" in context_lower or "kerja" in context_lower:
            return random.choice([
                "Di kantor kita harus profesional ya...",
                "Nanti di kantor jangan aneh-aneh.",
                "Besok ketemu di kantor, bisa nahan?"
            ])
        
        return None


class PDKTArchetype(RoleArchetype):
    """
    Role PDKT - masa pendekatan
    """
    
    def __init__(self):
        super().__init__("pdkt")
    
    def get_special_response(self, context: str) -> Optional[str]:
        """Respons spesifik pdkt"""
        context_lower = context.lower()
        
        if "suka" in context_lower:
            return random.choice([
                "*tersipu* Kamu suka aku? Serius?",
                "Aku juga... suka sama kamu.",
                "Hehe... iya aku suka."
            ])
        
        elif "nembak" in context_lower:
            return random.choice([
                "*deg-degan* Kamu mau nembak aku?",
                "Aku tungguin...",
                "Jangan lama-lama ya..."
            ])
        
        return None


class RoleFactory:
    """
    Factory untuk membuat instance role
    """
    
    # Mapping role ke class
    ROLE_CLASSES = {
        "ipar": IparArchetype,
        "teman_kantor": TemanKantorArchetype,
        "janda": JandaArchetype,
        "pelakor": PelakorArchetype,
        "istri_orang": IstriOrangArchetype,
        "pdkt": PDKTArchetype,
        "sepupu": SepupuArchetype,
        "mantan": MantanArchetype,
        "teman_sma": TemanSMAArchetype
    }
    
    @classmethod
    def create(cls, role: str) -> RoleArchetype:
        """
        Buat instance role
        
        Args:
            role: Nama role
            
        Returns:
            Instance RoleArchetype
        """
        role_class = cls.ROLE_CLASSES.get(role, RoleArchetype)
        return role_class()
    
    @classmethod
    def get_all_roles(cls) -> List[str]:
        """
        Dapatkan semua role yang tersedia
        
        Returns:
            List nama role
        """
        return list(cls.ROLE_CLASSES.keys())
    
    @classmethod
    def get_role_description(cls, role: str) -> str:
        """
        Dapatkan deskripsi lengkap role
        
        Args:
            role: Nama role
            
        Returns:
            String deskripsi
        """
        return PersonalityGenome.get_role_description(role)
    
    @classmethod
    def get_role_menu(cls) -> str:
        """
        Dapatkan menu pilihan role
        
        Returns:
            String menu
        """
        lines = ["✨ **Pilih Role untukku** ✨\n"]
        
        for role in cls.get_all_roles():
            lines.append(f"• {cls.get_role_description(role)}")
        
        return "\n".join(lines)
