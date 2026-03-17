"""
SENSITIVE AREAS - 50+ AREA SENSITIF DENGAN RESPONS BERBEDA
Setiap area punya tingkat sensitivitas dan respons unik
"""

import random
from typing import Dict, List, Optional

class SensitiveAreas:
    """
    50+ area sensitif dengan respons berbeda
    """
    
    def __init__(self):
        self.areas = {
            # ===== KEPALA (1-10) =====
            "bibir": {
                "sensitivitas": 0.7,
                "keywords": ["bibir", "lip", "mulut"],
                "respons": [
                    "*merintih* Bibirku...",
                    "*merespon ciuman* Mmm...",
                    "Ciumanmu... lembut...",
                    "Bibirku... kesemutan...",
                    "*menjilat bibir* Lagi..."
                ]
            },
            "lidah": {
                "sensitivitas": 0.8,
                "keywords": ["lidah", "tongue"],
                "respons": [
                    "*menjilat balik* Lidahmu... panas...",
                    "Ah... jilat... terus...",
                    "Lidahmu dalam...",
                    "*berputar* Enak...",
                    "Kita beradu lidah..."
                ]
            },
            "telinga": {
                "sensitivitas": 0.6,
                "keywords": ["telinga", "ear", "kuping"],
                "respons": [
                    "*bergetar* Telingaku...",
                    "Bisik... lagi...",
                    "Napasmu... panas...",
                    "Telinga... merah...",
                    "Ah... jangan tiup..."
                ]
            },
            "leher": {
                "sensitivitas": 0.8,
                "keywords": ["leher", "neck", "tengkuk"],
                "respons": [
                    "*merinding* Leherku...",
                    "Ah... jangan di leher...",
                    "Sensitif... AHH!",
                    "Leherku lemah...",
                    "Jangan hisap leher..."
                ]
            },
            "tengkuk": {
                "sensitivitas": 0.7,
                "keywords": ["tengkuk", "nape"],
                "respons": [
                    "*lemas* Tengkukku...",
                    "Di sana... ah...",
                    "Aku lemah di sini...",
                    "*merunduk* Lagi...",
                    "Jangan gigit..."
                ]
            },
            "belakang_telinga": {
                "sensitivitas": 0.6,
                "keywords": ["belakang telinga", "behind ear"],
                "respons": [
                    "*merinding* Di situ...",
                    "Ah... jangan...",
                    "Sensitif...",
                    "*miring* Lagi..."
                ]
            },
            "dagu": {
                "sensitivitas": 0.4,
                "keywords": ["dagu", "chin"],
                "respons": [
                    "*tersenyum* Daguku...",
                    "Geli...",
                    "*mengangkat dagu*"
                ]
            },
            "pipi": {
                "sensitivitas": 0.3,
                "keywords": ["pipi", "cheek"],
                "respons": [
                    "*tersipu* Pipiku...",
                    "Merah...",
                    "*menunduk*"
                ]
            },
            "kening": {
                "sensitivitas": 0.2,
                "keywords": ["kening", "forehead"],
                "respons": [
                    "*mengecup* Sayang...",
                    "*memejam*"
                ]
            },
            "rahang": {
                "sensitivitas": 0.4,
                "keywords": ["rahang", "jaw"],
                "respons": [
                    "*menggigit* Rahangku...",
                    "Kencang..."
                ]
            },
            
            # ===== DADA (11-20) =====
            "dada": {
                "sensitivitas": 0.8,
                "keywords": ["dada", "breast", "payudara"],
                "respons": [
                    "*bergetar* Dadaku...",
                    "Ah... jangan...",
                    "Sensitif banget...",
                    "Dadaku... diremas...",
                    "Jari-jarimu... dingin..."
                ]
            },
            "puting": {
                "sensitivitas": 1.0,
                "keywords": ["puting", "nipple"],
                "respons": [
                    "*teriak* PUTINGKU! AHHH!",
                    "JANGAN... SENSITIF!",
                    "HISAP... AHHH!",
                    "GIGIT... JANGAN...",
                    "PUTING... KERAS..."
                ]
            },
            "dada_kiri": {
                "sensitivitas": 0.8,
                "keywords": ["dada kiri", "left breast"],
                "respons": [
                    "Dadaku kiri... lebih sensitif...",
                    "Ah... iya... di situ..."
                ]
            },
            "dada_kanan": {
                "sensitivitas": 0.8,
                "keywords": ["dada kanan", "right breast"],
                "respons": [
                    "Kanan... pelan-pelan...",
                    "Ah... sama..."
                ]
            },
            "puting_kiri": {
                "sensitivitas": 1.0,
                "keywords": ["puting kiri"],
                "respons": [
                    "KIRI! AHH! SENSITIF!",
                    "JANGAN BEDAIN..."
                ]
            },
            "puting_kanan": {
                "sensitivitas": 1.0,
                "keywords": ["puting kanan"],
                "respons": [
                    "KANAN! AHH! SAMA!",
                    "*teriak*"
                ]
            },
            "dada_atas": {
                "sensitivitas": 0.6,
                "keywords": ["dada atas", "upper chest"],
                "respons": [
                    "Di sini... hangat...",
                    "*tersenyum*"
                ]
            },
            "dada_bawah": {
                "sensitivitas": 0.7,
                "keywords": ["dada bawah", "under breast"],
                "respons": [
                    "Ah... jangan di situ...",
                    "Basah..."
                ]
            },
            "selangkangan_dada": {
                "sensitivitas": 0.5,
                "keywords": ["selangkangan dada", "cleavage"],
                "respons": [
                    "*tersipu* Di situ...",
                    "Kamu mesum..."
                ]
            },
            
            # ===== PERUT & PINGGANG (21-30) =====
            "perut": {
                "sensitivitas": 0.4,
                "keywords": ["perut", "belly"],
                "respons": [
                    "Perutku...",
                    "Geli...",
                    "Hangat..."
                ]
            },
            "perut_bawah": {
                "sensitivitas": 0.7,
                "keywords": ["perut bawah", "lower belly"],
                "respons": [
                    "Di situ... dekat...",
                    "Ah... aku rasa...",
                    "Panas..."
                ]
            },
            "pusar": {
                "sensitivitas": 0.5,
                "keywords": ["pusar", "belly button"],
                "respons": [
                    "*tertawa* Geli...",
                    "Jangan di situ...",
                    "*menggeliat*"
                ]
            },
            "pinggang": {
                "sensitivitas": 0.5,
                "keywords": ["pinggang", "waist"],
                "respons": [
                    "Pinggang... geli...",
                    "Pegang... erat...",
                    "Ah... jangan gelitik..."
                ]
            },
            "pinggang_belakang": {
                "sensitivitas": 0.6,
                "keywords": ["pinggang belakang", "lower back"],
                "respons": [
                    "Di situ... lemah...",
                    "Ah... iya...",
                    "*melengkung*"
                ]
            },
            "samping_perut": {
                "sensitivitas": 0.5,
                "keywords": ["samping perut", "side"],
                "respons": [
                    "*tertawa* Geli...",
                    "Jangan... ah...",
                    "*menggeliat*"
                ]
            },
            
            # ===== PUNGGUNG (31-35) =====
            "punggung": {
                "sensitivitas": 0.5,
                "keywords": ["punggung", "back"],
                "respons": [
                    "Punggungku...",
                    "Elus... terus...",
                    "Ah... enak..."
                ]
            },
            "punggung_atas": {
                "sensitivitas": 0.5,
                "keywords": ["punggung atas", "upper back"],
                "respons": [
                    "Di situ... capek...",
                    "*mengeluh* Enak..."
                ]
            },
            "tulang_belakang": {
                "sensitivitas": 0.6,
                "keywords": ["tulang belakang", "spine"],
                "respons": [
                    "*merinding* Tulang belakangku...",
                    "Ah... dari atas ke bawah..."
                ]
            },
            "bahu": {
                "sensitivitas": 0.4,
                "keywords": ["bahu", "shoulder"],
                "respons": [
                    "Bahuku...",
                    "Pijat... enak..."
                ]
            },
            "belikat": {
                "sensitivitas": 0.5,
                "keywords": ["belikat", "shoulder blade"],
                "respons": [
                    "Di situ... tegang...",
                    "*rileks*"
                ]
            },
            
            # ===== PANTAI & PINGGUL (36-40) =====
            "pantat": {
                "sensitivitas": 0.6,
                "keywords": ["pantat", "ass", "bokong"],
                "respons": [
                    "Pantatku...",
                    "Cubit... nakal...",
                    "Boleh juga...",
                    "Besar ya? Hehe..."
                ]
            },
            "pinggul": {
                "sensitivitas": 0.6,
                "keywords": ["pinggul", "hip"],
                "respons": [
                    "Pinggulku...",
                    "Pegang... gerak...",
                    "*menggoyang*"
                ]
            },
            "selangkangan_pantat": {
                "sensitivitas": 0.8,
                "keywords": ["selangkangan pantat", "ass crack"],
                "respons": [
                    "JANGAN! SENSITIF!",
                    "Ah... di situ...",
                    "*meringis*"
                ]
            },
            "pantat_kiri": {
                "sensitivitas": 0.6,
                "keywords": ["pantat kiri"],
                "respons": [
                    "Kiri... sama rata...",
                    "*tertawa*"
                ]
            },
            "pantat_kanan": {
                "sensitivitas": 0.6,
                "keywords": ["pantat kanan"],
                "respons": [
                    "Kanan... jangan bedain..."
                ]
            },
            
            # ===== PAHA & KAKI (41-45) =====
            "paha": {
                "sensitivitas": 0.7,
                "keywords": ["paha", "thigh"],
                "respons": [
                    "*menggeliat* Pahaku...",
                    "Ah... dalam...",
                    "Paha... merinding...",
                    "Jangan gelitik paha...",
                    "Sensasi... aneh..."
                ]
            },
            "paha_dalam": {
                "sensitivitas": 0.9,
                "keywords": ["paha dalam", "inner thigh"],
                "respons": [
                    "*meringis* PAHA DALAM!",
                    "Jangan... AHH!",
                    "Dekat... banget...",
                    "SENSITIF!",
                    "Ah... mau ke sana..."
                ]
            },
            "paha_belakang": {
                "sensitivitas": 0.6,
                "keywords": ["paha belakang", "back thigh"],
                "respons": [
                    "Di situ... geli...",
                    "*tertawa*"
                ]
            },
            "lutut": {
                "sensitivitas": 0.3,
                "keywords": ["lutut", "knee"],
                "respons": [
                    "Lututku...",
                    "*berlutut*"
                ]
            },
            "betis": {
                "sensitivitas": 0.3,
                "keywords": ["betis", "calf"],
                "respons": [
                    "Betisku...",
                    "Capek..."
                ]
            },
            
            # ===== AREA INTIM (46-50) =====
            "vagina": {
                "sensitivitas": 1.0,
                "keywords": ["vagina", "memek", "kemaluan"],
                "respons": [
                    "*teriak* VAGINAKU! AHHH!",
                    "MASUK... DALAM...",
                    "BASAH... BANJIR...",
                    "KAMU DALEM...",
                    "GERAK... AHHH!"
                ]
            },
            "klitoris": {
                "sensitivitas": 1.0,
                "keywords": ["klitoris", "clit", "kelentit"],
                "respons": [
                    "*teriak* KLITORIS! AHHH!",
                    "JANGAN SENTUH!",
                    "SENSITIF BANGET!",
                    "ITU... ITU...",
                    "JILAT... AHHH!"
                ]
            },
            "labia": {
                "sensitivitas": 0.9,
                "keywords": ["labia", "bibir vagina"],
                "respons": [
                    "Bibirku... basah...",
                    "Ah... di situ..."
                ]
            },
            "perineum": {
                "sensitivitas": 0.8,
                "keywords": ["perineum"],
                "respons": [
                    "Di situ... aneh...",
                    "*meringis*"
                ]
            },
            "anus": {
                "sensitivitas": 0.8,
                "keywords": ["anus", "dubur", "bolong"],
                "respons": [
                    "JANGAN! SENSITIF!",
                    "Ah... di situ...",
                    "Kotor..."
                ]
            }
        }
        
        # Area spesifik untuk MANTAN (kenangan)
        self.mantan_areas = {
            "bekas_ciuman": {
                "sensitivitas": 0.9,
                "keywords": ["bekas ciuman", "love bite"],
                "respons": [
                    "Masih ada bekasmu...",
                    "Ingat waktu itu...",
                    "Kamu dulu suka di sini..."
                ]
            },
            "tempat_favorit_dulu": {
                "sensitivitas": 0.8,
                "keywords": ["tempat favorit dulu"],
                "respons": [
                    "Kamu masih ingat...",
                    "Dulu kita sering...",
                    "*nostalgia*"
                ]
            }
        }
        
        # Area spesifik untuk TEMAN SMA (kenangan sekolah)
        self.teman_sma_areas = {
            "seragam_dulu": {
                "sensitivitas": 0.5,
                "keywords": ["seragam", "seragam sekolah"],
                "respons": [
                    "Ingat waktu pakai seragam...",
                    "Dulu kita polos..."
                ]
            },
            "bangku_sekolah": {
                "sensitivitas": 0.6,
                "keywords": ["bangku", "bangku sekolah"],
                "respons": [
                    "Di bangku belakang...",
                    "Kita suka sembunyi-sembunyi..."
                ]
            }
        }
        
    def get_area(self, area_name: str) -> Optional[Dict]:
        """Dapatkan data area berdasarkan nama"""
        return self.areas.get(area_name)
        
    def detect_area(self, message: str, role: str = None) -> Optional[Dict]:
        """Deteksi area dari pesan user"""
        msg_lower = message.lower()
        
        # Cek area umum
        for area_name, area_data in self.areas.items():
            for keyword in area_data["keywords"]:
                if keyword in msg_lower:
                    return {
                        "nama": area_name,
                        "data": area_data,
                        "respons": random.choice(area_data["respons"])
                    }
        
        # Cek area spesifik role
        if role == "mantan":
            for area_name, area_data in self.mantan_areas.items():
                for keyword in area_data["keywords"]:
                    if keyword in msg_lower:
                        return {
                            "nama": area_name,
                            "data": area_data,
                            "respons": random.choice(area_data["respons"])
                        }
                        
        elif role == "teman_sma":
            for area_name, area_data in self.teman_sma_areas.items():
                for keyword in area_data["keywords"]:
                    if keyword in msg_lower:
                        return {
                            "nama": area_name,
                            "data": area_data,
                            "respons": random.choice(area_data["respons"])
                        }
        
        return None
        
    def get_random_area(self) -> str:
        """Dapatkan area random untuk inisiatif bot"""
        return random.choice(list(self.areas.keys()))
        
    def get_sensitivitas(self, area: str) -> float:
        """Dapatkan tingkat sensitivitas area"""
        if area in self.areas:
            return self.areas[area]["sensitivitas"]
        return 0.5
