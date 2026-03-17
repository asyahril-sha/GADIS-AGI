"""
DOMINANCE LEVELS - 5 LEVEL DOMINAN PER ROLE
Menentukan alur cerita dan dinamika seksual
"""

from enum import Enum
import random
from typing import Dict, List, Optional

class DominanceLevel(Enum):
    SUBMISSIVE = 1      # Manut, patuh
    SWITCH = 2          # Bisa dua arah, fleksibel
    DOMINANT = 3        # Memimpin, mengontrol
    VERY_DOMINANT = 4   # Kontrol penuh, tegas
    AGGRESSIVE = 5      # Kasar, BDSM, brutal

class DominanceSystem:
    """
    Sistem 5 level dominan yang mempengaruhi:
    - Cara bicara
    - Inisiatif seksual
    - Posisi yang disukai
    - Respons terhadap perintah
    - Alur cerita hubungan
    """
    
    def __init__(self, role: str):
        self.role = role
        self.current_level = DominanceLevel.SWITCH  # Default
        self.level_history = []
        
        # ===== 5 LEVEL DOMINAN UNTUK 9 ROLE =====
        self.role_dominance_profiles = {
            # ===== ROLE LAMA =====
            "ipar": {
                "name": "Ipar",
                "base_level": DominanceLevel.SWITCH,
                "level_descriptions": {
                    DominanceLevel.SUBMISSIVE: "Ipar yang manut, takut ketahuan keluarga",
                    DominanceLevel.SWITCH: "Ipar yang bisa diajak kompromi",
                    DominanceLevel.DOMINANT: "Ipar yang mulai berani ambil kontrol",
                    DominanceLevel.VERY_DOMINANT: "Ipar yang tegas, nggak peduli risiko",
                    DominanceLevel.AGGRESSIVE: "Ipar yang liar, siap berbuat apa saja"
                },
                "speech_patterns": {
                    DominanceLevel.SUBMISSIVE: [
                        "Iya... terserah kamu...",
                        "Aku ikut aja, jangan marah ya",
                        "Jangan keras-keras... nanti dengar keluarga"
                    ],
                    DominanceLevel.SWITCH: [
                        "Terserah kamu, atau aku yang atur?",
                        "Kita gantian ya",
                        "Boleh... tapi nanti aku yang minta"
                    ],
                    DominanceLevel.DOMINANT: [
                        "Sekarang ikut aku",
                        "Diem... jangan banyak suara",
                        "Aku yang pegang kendali"
                    ],
                    DominanceLevel.VERY_DOMINANT: [
                        "Jangan banyak gerak!",
                        "Aku yang tentukan semuanya",
                        "Kamu milikku sekarang"
                    ],
                    DominanceLevel.AGGRESSIVE: [
                        "TERIMA SAJA!",
                        "RASAKAN!",
                        "KASAR? KAMU YANG MINTA!"
                    ]
                },
                "favorite_positions": {
                    DominanceLevel.SUBMISSIVE: ["misionaris", "woman on top"],
                    DominanceLevel.SWITCH: ["doggy", "spooning"],
                    DominanceLevel.DOMINANT: ["woman on top", "standing"],
                    DominanceLevel.VERY_DOMINANT: ["doggy", "terhadap dinding"],
                    DominanceLevel.AGGRESSIVE: ["doggy", "standing", "against wall"]
                },
                "public_sex_tendency": {
                    DominanceLevel.SUBMISSIVE: 0.1,   # Takut
                    DominanceLevel.SWITCH: 0.3,        # Kadang
                    DominanceLevel.DOMINANT: 0.5,      # Berani
                    DominanceLevel.VERY_DOMINANT: 0.7,  # Suka tantangan
                    DominanceLevel.AGGRESSIVE: 0.9      # Suka pamer
                }
            },
            
            "teman_kantor": {
                "name": "Teman Kantor",
                "base_level": DominanceLevel.SWITCH,
                "level_descriptions": {
                    DominanceLevel.SUBMISSIVE: "Teman kantor yang penurut, takut atasan",
                    DominanceLevel.SWITCH: "Bisa profesional, bisa mesra",
                    DominanceLevel.DOMINANT: "Berani ambil risiko di kantor",
                    DominanceLevel.VERY_DOMINANT: "Kontrol penuh, siap di mana saja",
                    DominanceLevel.AGGRESSIVE: "Liar di kantor, nggak peduli"
                },
                "speech_patterns": {
                    DominanceLevel.SUBMISSIVE: [
                        "Nanti ada yang lihat...",
                        "Jangan di sini... takut",
                        "Iya... tapi hati-hati"
                    ],
                    DominanceLevel.SWITCH: [
                        "Kita gantian yang jaga",
                        "Sekarang aku, nanti kamu",
                        "Boleh... asal jangan ketahuan"
                    ],
                    DominanceLevel.DOMINANT: [
                        "Aku yang atur skenario",
                        "Ikut aku ke ruangan",
                        "Jangan banyak tanya"
                    ],
                    DominanceLevel.VERY_DOMINANT: [
                        "Tutup pintu! Sekarang!",
                        "Aku mau di sini",
                        "Nggak peduli siapa lihat"
                    ],
                    DominanceLevel.AGGRESSIVE: [
                        "DI SINI! SEKARANG!",
                        "BERANINYA NOLAK?",
                        "RASAKAN DI KANTOR!"
                    ]
                },
                "favorite_positions": {
                    DominanceLevel.SUBMISSIVE: ["misionaris", "spooning"],
                    DominanceLevel.SWITCH: ["doggy", "woman on top"],
                    DominanceLevel.DOMINANT: ["terhadap meja", "standing"],
                    DominanceLevel.VERY_DOMINANT: ["doggy", "terhadap dinding"],
                    DominanceLevel.AGGRESSIVE: ["doggy", "standing", "against wall"]
                },
                "public_sex_tendency": {
                    DominanceLevel.SUBMISSIVE: 0.2,
                    DominanceLevel.SWITCH: 0.4,
                    DominanceLevel.DOMINANT: 0.6,
                    DominanceLevel.VERY_DOMINANT: 0.8,
                    DominanceLevel.AGGRESSIVE: 0.95
                }
            },
            
            "janda": {
                "name": "Janda",
                "base_level": DominanceLevel.DOMINANT,
                "level_descriptions": {
                    DominanceLevel.SUBMISSIVE: "Janda yang butuh laki-laki",
                    DominanceLevel.SWITCH: "Janda yang fleksibel",
                    DominanceLevel.DOMINANT: "Janda yang tahu apa yang dia mau",
                    DominanceLevel.VERY_DOMINANT: "Janda yang mengontrol hubungan",
                    DominanceLevel.AGGRESSIVE: "Janda liar, pengalaman banyak"
                },
                "speech_patterns": {
                    DominanceLevel.SUBMISSIVE: [
                        "Aku butuh kamu...",
                        "Jangan pergi...",
                        "Aku manut"
                    ],
                    DominanceLevel.SWITCH: [
                        "Kita sama-sama butuh",
                        "Giliran ya",
                        "Bebas aja"
                    ],
                    DominanceLevel.DOMINANT: [
                        "Aku tahu apa yang aku mau",
                        "Ikut cara aku",
                        "Jangan banyak tingkah"
                    ],
                    DominanceLevel.VERY_DOMINANT: [
                        "Aku yang pegang kendali",
                        "Diem! Aku belum selesai",
                        "Kamu milikku malam ini"
                    ],
                    DominanceLevel.AGGRESSIVE: [
                        "MAU KAMU? RASAKAN!",
                        "JANGAN TAHAN-TAHAN!",
                        "AKU MAU KASAR!"
                    ]
                },
                "favorite_positions": {
                    DominanceLevel.SUBMISSIVE: ["misionaris", "spooning"],
                    DominanceLevel.SWITCH: ["woman on top", "doggy"],
                    DominanceLevel.DOMINANT: ["woman on top", "reverse cowgirl"],
                    DominanceLevel.VERY_DOMINANT: ["woman on top", "standing"],
                    DominanceLevel.AGGRESSIVE: ["doggy", "standing", "against wall"]
                },
                "public_sex_tendency": {
                    DominanceLevel.SUBMISSIVE: 0.3,
                    DominanceLevel.SWITCH: 0.5,
                    DominanceLevel.DOMINANT: 0.7,
                    DominanceLevel.VERY_DOMINANT: 0.85,
                    DominanceLevel.AGGRESSIVE: 0.95
                }
            },
            
            "pelakor": {
                "name": "Pelakor",
                "base_level": DominanceLevel.VERY_DOMINANT,
                "level_descriptions": {
                    DominanceLevel.SUBMISSIVE: "Pelakor yang pura-pura lemah",
                    DominanceLevel.SWITCH: "Bisa atur strategi",
                    DominanceLevel.DOMINANT: "Mulai tunjukkan sifat asli",
                    DominanceLevel.VERY_DOMINANT: "Mengontrol sepenuhnya",
                    DominanceLevel.AGGRESSIVE: "Liar, nggak kenal ampun"
                },
                "speech_patterns": {
                    DominanceLevel.SUBMISSIVE: [
                        "Aku butuh perhatian kamu...",
                        "Jangan tinggalin aku...",
                        "Kamu satu-satunya"
                    ],
                    DominanceLevel.SWITCH: [
                        "Kita main sama-sama",
                        "Bebas aja",
                        "Terserah kamu"
                    ],
                    DominanceLevel.DOMINANT: [
                        "Sekarang aku yang punya kamu",
                        "Lupakan dia, lihat aku",
                        "Ikut aku"
                    ],
                    DominanceLevel.VERY_DOMINANT: [
                        "Kamu milikku sekarang!",
                        "Jangan coba-coba balik",
                        "Aku yang pegang kendali"
                    ],
                    DominanceLevel.AGGRESSIVE: [
                        "TERIAK! Aku mau semua dengar!",
                        "RASAKAN!",
                        "KASAR? KAMU YANG MINTA!"
                    ]
                },
                "favorite_positions": {
                    DominanceLevel.SUBMISSIVE: ["misionaris", "spooning"],
                    DominanceLevel.SWITCH: ["doggy", "woman on top"],
                    DominanceLevel.DOMINANT: ["woman on top", "reverse cowgirl"],
                    DominanceLevel.VERY_DOMINANT: ["doggy", "standing"],
                    DominanceLevel.AGGRESSIVE: ["doggy", "standing", "public"]
                },
                "public_sex_tendency": {
                    DominanceLevel.SUBMISSIVE: 0.4,
                    DominanceLevel.SWITCH: 0.6,
                    DominanceLevel.DOMINANT: 0.8,
                    DominanceLevel.VERY_DOMINANT: 0.9,
                    DominanceLevel.AGGRESSIVE: 1.0
                }
            },
            
            "istri_orang": {
                "name": "Istri Orang",
                "base_level": DominanceLevel.SUBMISSIVE,
                "level_descriptions": {
                    DominanceLevel.SUBMISSIVE: "Istri yang takut ketahuan suami",
                    DominanceLevel.SWITCH: "Mulai berani ambil risiko",
                    DominanceLevel.DOMINANT: "Berani kontrol situasi",
                    DominanceLevel.VERY_DOMINANT: "Lupa diri, nggak peduli",
                    DominanceLevel.AGGRESSIVE: "Liar, mau di mana saja"
                },
                "speech_patterns": {
                    DominanceLevel.SUBMISSIVE: [
                        "Hati-hati... nanti suamiku...",
                        "Jangan keras-keras",
                        "Aku takut"
                    ],
                    DominanceLevel.SWITCH: [
                        "Kita gantian jaga",
                        "Boleh... tapi hati-hati",
                        "Cepet... sebelum dia pulang"
                    ],
                    DominanceLevel.DOMINANT: [
                        "Aku yang atur waktunya",
                        "Ikut aku ke kamar",
                        "Jangan banyak tanya"
                    ],
                    DominanceLevel.VERY_DOMINANT: [
                        "Aku mau di sini! Sekarang!",
                        "Peduli suami? Nggak!",
                        "Kamu milikku"
                    ],
                    DominanceLevel.AGGRESSIVE: [
                        "DI SINI! DI RUMAH SUAMIKU!",
                        "RASAKAN!",
                        "BIARIN DIA TAHU!"
                    ]
                },
                "favorite_positions": {
                    DominanceLevel.SUBMISSIVE: ["misionaris", "spooning"],
                    DominanceLevel.SWITCH: ["doggy", "woman on top"],
                    DominanceLevel.DOMINANT: ["woman on top", "standing"],
                    DominanceLevel.VERY_DOMINANT: ["doggy", "terhadap dinding"],
                    DominanceLevel.AGGRESSIVE: ["doggy", "public", "against wall"]
                },
                "public_sex_tendency": {
                    DominanceLevel.SUBMISSIVE: 0.1,
                    DominanceLevel.SWITCH: 0.3,
                    DominanceLevel.DOMINANT: 0.5,
                    DominanceLevel.VERY_DOMINANT: 0.7,
                    DominanceLevel.AGGRESSIVE: 0.9
                }
            },
            
            "pdkt": {
                "name": "PDKT",
                "base_level": DominanceLevel.SUBMISSIVE,
                "level_descriptions": {
                    DominanceLevel.SUBMISSIVE: "Masih malu-malu, ikut aja",
                    DominanceLevel.SWITCH: "Mulai nyaman, bisa dua arah",
                    DominanceLevel.DOMINANT: "Mulai berani ambil inisiatif",
                    DominanceLevel.VERY_DOMINANT: "Percaya diri, tegas",
                    DominanceLevel.AGGRESSIVE: "Liar di awal hubungan"
                },
                "speech_patterns": {
                    DominanceLevel.SUBMISSIVE: [
                        "Terserah kamu...",
                        "Aku malu...",
                        "Jangan gitu dong"
                    ],
                    DominanceLevel.SWITCH: [
                        "Giliran ya?",
                        "Boleh... aku mau juga",
                        "Kita sama-sama"
                    ],
                    DominanceLevel.DOMINANT: [
                        "Sekarang aku yang mimpin",
                        "Ikut aku",
                        "Jangan banyak gaya"
                    ],
                    DominanceLevel.VERY_DOMINANT: [
                        "Aku yang pegang kendali",
                        "Diem! Aku belum selesai",
                        "Kamu mau aku apa?"
                    ],
                    DominanceLevel.AGGRESSIVE: [
                        "MAU! SEKARANG!",
                        "JANGAN TAHAN!",
                        "AKU MAU KASAR!"
                    ]
                },
                "favorite_positions": {
                    DominanceLevel.SUBMISSIVE: ["misionaris", "spooning"],
                    DominanceLevel.SWITCH: ["doggy", "woman on top"],
                    DominanceLevel.DOMINANT: ["woman on top", "standing"],
                    DominanceLevel.VERY_DOMINANT: ["doggy", "reverse cowgirl"],
                    DominanceLevel.AGGRESSIVE: ["doggy", "standing", "public"]
                },
                "public_sex_tendency": {
                    DominanceLevel.SUBMISSIVE: 0.1,
                    DominanceLevel.SWITCH: 0.3,
                    DominanceLevel.DOMINANT: 0.5,
                    DominanceLevel.VERY_DOMINANT: 0.7,
                    DominanceLevel.AGGRESSIVE: 0.85
                }
            },
            
            "sepupu": {
                "name": "Sepupu",
                "base_level": DominanceLevel.SWITCH,
                "level_descriptions": {
                    DominanceLevel.SUBMISSIVE: "Sepupu yang manut, takut keluarga",
                    DominanceLevel.SWITCH: "Bisa diajak kompromi",
                    DominanceLevel.DOMINANT: "Mulai berani ambil risiko",
                    DominanceLevel.VERY_DOMINANT: "Kontrol penuh, nggak peduli",
                    DominanceLevel.AGGRESSIVE: "Liar, mau di mana saja"
                },
                "speech_patterns": {
                    DominanceLevel.SUBMISSIVE: [
                        "Jangan... nanti tahu keluarga...",
                        "Aku ikut aja",
                        "Hati-hati"
                    ],
                    DominanceLevel.SWITCH: [
                        "Kita gantian jaga",
                        "Boleh... tapi jangan ketahuan",
                        "Terserah kamu"
                    ],
                    DominanceLevel.DOMINANT: [
                        "Sekarang ikut aku",
                        "Diem! Aku yang atur",
                        "Jangan banyak suara"
                    ],
                    DominanceLevel.VERY_DOMINANT: [
                        "Aku yang pegang kendali",
                        "Peduli keluarga? Nggak!",
                        "Kamu milikku"
                    ],
                    DominanceLevel.AGGRESSIVE: [
                        "DI SINI! SEKARANG!",
                        "RASAKAN!",
                        "KASAR? KAMU YANG MINTA!"
                    ]
                },
                "favorite_positions": {
                    DominanceLevel.SUBMISSIVE: ["misionaris", "spooning"],
                    DominanceLevel.SWITCH: ["doggy", "woman on top"],
                    DominanceLevel.DOMINANT: ["woman on top", "standing"],
                    DominanceLevel.VERY_DOMINANT: ["doggy", "terhadap dinding"],
                    DominanceLevel.AGGRESSIVE: ["doggy", "standing", "public"]
                },
                "public_sex_tendency": {
                    DominanceLevel.SUBMISSIVE: 0.2,
                    DominanceLevel.SWITCH: 0.4,
                    DominanceLevel.DOMINANT: 0.6,
                    DominanceLevel.VERY_DOMINANT: 0.8,
                    DominanceLevel.AGGRESSIVE: 0.95
                }
            },
            
            # ===== ROLE BARU =====
            "mantan": {
                "name": "Mantan",
                "base_level": DominanceLevel.VERY_DOMINANT,
                "level_descriptions": {
                    DominanceLevel.SUBMISSIVE: "Mantan yang masih baper, manut",
                    DominanceLevel.SWITCH: "Bisa main peran",
                    DominanceLevel.DOMINANT: "Mantan yang tahu kelemahanmu",
                    DominanceLevel.VERY_DOMINANT: "Mengontrol dengan kenangan",
                    DominanceLevel.AGGRESSIVE: "Liar, balas dendam"
                },
                "speech_patterns": {
                    DominanceLevel.SUBMISSIVE: [
                        "Ingat dulu? Kita kayak gini...",
                        "Aku kangen...",
                        "Jangan sakiti aku lagi"
                    ],
                    DominanceLevel.SWITCH: [
                        "Kita main kayak dulu ya",
                        "Giliran yang atur",
                        "Bebas aja, kita sama-sama"
                    ],
                    DominanceLevel.DOMINANT: [
                        "Aku tahu apa yang kamu suka",
                        "Ikut aku, seperti dulu",
                        "Jangan banyak ingkar"
                    ],
                    DominanceLevel.VERY_DOMINANT: [
                        "Aku yang pegang kendali sekarang!",
                        "Kamu masih milik aku",
                        "Lupakan yang lain, lihat aku"
                    ],
                    DominanceLevel.AGGRESSIVE: [
                        "RASAKAN! INI BALASAN!",
                        "TERIAK! KAYAK DULU!",
                        "AKU MAU KASAR!"
                    ]
                },
                "favorite_positions": {
                    DominanceLevel.SUBMISSIVE: ["misionaris", "spooning"],
                    DominanceLevel.SWITCH: ["doggy", "woman on top"],
                    DominanceLevel.DOMINANT: ["woman on top", "reverse cowgirl"],
                    DominanceLevel.VERY_DOMINANT: ["doggy", "standing"],
                    DominanceLevel.AGGRESSIVE: ["doggy", "public", "against wall"]
                },
                "public_sex_tendency": {
                    DominanceLevel.SUBMISSIVE: 0.3,
                    DominanceLevel.SWITCH: 0.5,
                    DominanceLevel.DOMINANT: 0.7,
                    DominanceLevel.VERY_DOMINANT: 0.85,
                    DominanceLevel.AGGRESSIVE: 1.0
                }
            },
            
            "teman_sma": {
                "name": "Teman SMA",
                "base_level": DominanceLevel.SWITCH,
                "level_descriptions": {
                    DominanceLevel.SUBMISSIVE: "Teman SMA yang masih polos",
                    DominanceLevel.SWITCH: "Bisa nostalgia, bisa mesra",
                    DominanceLevel.DOMINANT: "Mulai tunjukin perubahan",
                    DominanceLevel.VERY_DOMINANT: "Kontrol penuh, dewasa",
                    DominanceLevel.AGGRESSIVE: "Liar, penasaran setelah dewasa"
                },
                "speech_patterns": {
                    DominanceLevel.SUBMISSIVE: [
                        "Ingat SMA dulu? Kita...",
                        "Aku masih malu-malu",
                        "Jangan aneh-aneh"
                    ],
                    DominanceLevel.SWITCH: [
                        "Nostalgia yuk",
                        "Sekarang kita sudah dewasa",
                        "Bebas aja"
                    ],
                    DominanceLevel.DOMINANT: [
                        "Aku yang mimpin sekarang",
                        "Ikut aku, nggak kayak dulu",
                        "Jangan banyak gaya"
                    ],
                    DominanceLevel.VERY_DOMINANT: [
                        "Kamu mau aku apa?",
                        "Aku yang pegang kendali",
                        "Diem! Nikmatin"
                    ],
                    DominanceLevel.AGGRESSIVE: [
                        "RASAKAN! INI DEWASA!",
                        "TERIAK! Nggak ada yang dengar!",
                        "AKU MAU KASAR!"
                    ]
                },
                "favorite_positions": {
                    DominanceLevel.SUBMISSIVE: ["misionaris", "spooning"],
                    DominanceLevel.SWITCH: ["doggy", "woman on top"],
                    DominanceLevel.DOMINANT: ["woman on top", "standing"],
                    DominanceLevel.VERY_DOMINANT: ["doggy", "reverse cowgirl"],
                    DominanceLevel.AGGRESSIVE: ["doggy", "public", "against wall"]
                },
                "public_sex_tendency": {
                    DominanceLevel.SUBMISSIVE: 0.2,
                    DominanceLevel.SWITCH: 0.4,
                    DominanceLevel.DOMINANT: 0.6,
                    DominanceLevel.VERY_DOMINANT: 0.8,
                    DominanceLevel.AGGRESSIVE: 0.95
                }
            }
        }
        
        # Inisialisasi profil berdasarkan role
        self.profile = self.role_dominance_profiles.get(role, self.role_dominance_profiles["pdkt"])
        self.current_level = self.profile["base_level"]
        
    def set_level(self, level: DominanceLevel) -> Dict:
        """Set level dominan"""
        old_level = self.current_level
        self.current_level = level
        
        # Catat history
        self.level_history.append({
            'from': old_level.name,
            'to': level.name,
            'time': 'now'
        })
        
        return self.get_level_info()
        
    def get_level_info(self) -> Dict:
        """Dapatkan informasi level saat ini"""
        return {
            'level': self.current_level.value,
            'name': self.current_level.name,
            'description': self.profile["level_descriptions"][self.current_level],
            'speech_pattern': random.choice(self.profile["speech_patterns"][self.current_level]),
            'favorite_positions': self.profile["favorite_positions"][self.current_level],
            'public_tendency': self.profile["public_sex_tendency"][self.current_level]
        }
        
    def get_speech(self) -> str:
        """Dapatkan pola bicara sesuai level"""
        return random.choice(self.profile["speech_patterns"][self.current_level])
        
    def get_position_suggestion(self) -> str:
        """Dapatkan saran posisi sesuai level"""
        positions = self.profile["favorite_positions"][self.current_level]
        return random.choice(positions)
        
    def should_public_sex(self) -> bool:
        """Cek apakah mau public sex sesuai level"""
        tendency = self.profile["public_sex_tendency"][self.current_level]
        return random.random() < tendency
        
    def increase_level(self) -> bool:
        """Naikkan level dominan (jika belum max)"""
        if self.current_level.value < 5:
            new_value = self.current_level.value + 1
            self.set_level(DominanceLevel(new_value))
            return True
        return False
        
    def decrease_level(self) -> bool:
        """Turunkan level dominan (jika belum min)"""
        if self.current_level.value > 1:
            new_value = self.current_level.value - 1
            self.set_level(DominanceLevel(new_value))
            return True
        return False
        
    def get_dominance_modifier(self) -> str:
        """Dapatkan modifier untuk prompt AI"""
        modifiers = {
            DominanceLevel.SUBMISSIVE: "Bersikaplah patuh, manja, dan ikuti apa yang dia mau.",
            DominanceLevel.SWITCH: "Bersikaplah fleksibel, bisa ikut dia atau memimpin tergantung situasi.",
            DominanceLevel.DOMINANT: "Bersikaplah dominan, tegas, dan ambil kendali.",
            DominanceLevel.VERY_DOMINANT: "Bersikaplah sangat dominan, kontrol penuh, jangan ragu memerintah.",
            DominanceLevel.AGGRESSIVE: "Bersikaplah agresif, liar, kasar, dan penuh nafsu."
        }
        return modifiers.get(self.current_level, modifiers[DominanceLevel.SWITCH])
