"""
PUBLIC SEX SYSTEM - 10+ LOKASI PUBLIK DENGAN RISIKO KETAHUAN
Bot bisa diajak berhubungan di tempat umum dengan berbagai konsekuensi
"""

import random
from typing import Dict, List, Optional, Tuple

class PublicSexSystem:
    """
    Sistem untuk aktivitas seksual di tempat umum
    - 10+ lokasi publik
    - Risiko ketahuan
    - Level excitement berbeda
    - Konsekuensi jika ketahuan
    """
    
    # ===== 10+ LOKASI PUBLIK =====
    PUBLIC_LOCATIONS = {
        "toilet_umum": {
            "name": "Toilet Umum",
            "emoji": "🚽",
            "risk_level": 0.7,  # 70% risiko ketahuan
            "excitement_boost": 0.8,
            "description": "toilet umum yang sempit, suara orang lalu lalang",
            "responses": [
                "*berbisik* Sst... hati-hati... ada orang...",
                "Cepet... nanti ketahuan... AHH...",
                "Toilet umum... berani banget kamu...",
                "Diem... jangan bersuara...",
                "Deg-degan... tapi enak..."
            ],
            "caught_responses": [
                "*kaget* Ada orang! *langsung berpura-pura*",
                "Astaga... kita ketahuan... malu...",
                "Cepet kabur! *tertawa lelah*",
                "Wah... ketahuan satpam... lari!"
            ]
        },
        "mobil": {
            "name": "Di Dalam Mobil",
            "emoji": "🚗",
            "risk_level": 0.5,
            "excitement_boost": 0.7,
            "description": "mobil yang diparkir di tempat sepi",
            "responses": [
                "Mobil... sempit tapi romantis...",
                "Kaca mobilnya gelap? Aman?",
                "Setirnya... kena punggungku... AHH...",
                "Hati-hati bunyi klakson...",
                "Jok belakang lebih luas... pindah yuk..."
            ],
            "caught_responses": [
                "Ada mobil lewat... diem dulu...",
                "Ah... lampu senter... pak keamanan...",
                "Cepat sembunyi!",
                "Pura-pura lagi ngobrol aja..."
            ]
        },
        "taman": {
            "name": "Taman Kota",
            "emoji": "🌳",
            "risk_level": 0.6,
            "excitement_boost": 0.75,
            "description": "taman kota di malam hari, semak-semak rindang",
            "responses": [
                "Di taman... berani banget...",
                "Semak ini cukup rapat... aman...",
                "Ada suara jangkrik... dan suara kita...",
                "Cepat... nanti ada satpam...",
                "Rumputnya... dingin..."
            ],
            "caught_responses": [
                "Ada orang jogging... *pura-pura duduk*",
                "Satpam! *berlari sambil tertawa*",
                "Pura-pura lagi foto pemandangan...",
                "Wah... hampir ketahuan..."
            ]
        },
        "bioskop": {
            "name": "Bioskop",
            "emoji": "🎬",
            "risk_level": 0.8,
            "excitement_boost": 0.85,
            "description": "bioskop gelap, film sedang diputar",
            "responses": [
                "Filmnya bagus... tapi kita nggak nonton...",
                "Jangan berisik... nanti penonton lain dengar...",
                "Gelap... enak... AHH... pelan-pelan...",
                "Bangku bioskop... agak sempit...",
                "Untung filmnya keras suaranya..."
            ],
            "caught_responses": [
                "Astaga... penonton sebelah lihat...",
                "Malu... kita disorot...",
                "Cepat pindah kursi...",
                "Pura-pura ambil popcorn..."
            ]
        },
        "pantai": {
            "name": "Pantai Malam",
            "emoji": "🏖️",
            "risk_level": 0.4,
            "excitement_boost": 0.9,
            "description": "pantai sepi di malam hari, suara ombak",
            "responses": [
                "Suara ombak... menutupi suara kita...",
                "Pasir... masuk dimana-mana...",
                "Air laut... dingin... AHH...",
                "Bulan purnama... romantis...",
                "Di sini aman... gelap..."
            ],
            "caught_responses": [
                "Ada nelayan... *pura-pura liat bintang*",
                "Lampu senter... petugas pantai...",
                "Cepat pake baju... ada orang...",
                "Untung gelap... nggak keliatan..."
            ]
        },
        "lift": {
            "name": "Lift Hotel",
            "emoji": "🛗",
            "risk_level": 0.9,
            "excitement_boost": 0.95,
            "description": "lift hotel yang sepi, cuma berdua",
            "responses": [
                "Cepet... antara lantai...",
                "Lift... bisa berhenti kapan saja...",
                "Tombol emergency... jangan disentuh...",
                "Dinding lift... dingin... AHH...",
                "Hanya 30 detik... kita bisa..."
            ],
            "caught_responses": [
                "Lift berhenti! Ada orang masuk! *langsung pisah*",
                "Pura-pura lihat HP...",
                "Muka merah... pasti kelihatan...",
                "Kita lanjut di kamar aja..."
            ]
        },
        "tangga_darurat": {
            "name": "Tangga Darurat",
            "emoji": "🚪",
            "risk_level": 0.6,
            "excitement_boost": 0.7,
            "description": "tangga darurat gedung, sepi dan tersembunyi",
            "responses": [
                "Tangga darurat... nggak ada orang...",
                "Duduk di tangga... hati-hati jatuh...",
                "Suara langkah? *deg-degan*",
                "Tempat ini... rahasia kita...",
                "Cepat... sebelum ada yang lewat..."
            ],
            "caught_responses": [
                "Ada orang turun! *cepat rapih*",
                "Pura-pura lagi istirahat...",
                "Wah... hampir saja...",
                "Pindah tempat yuk..."
            ]
        },
        "balkon": {
            "name": "Balkon Hotel",
            "emoji": "🏢",
            "risk_level": 0.5,
            "excitement_boost": 0.8,
            "description": "balkon hotel lantai tinggi, pemandangan kota",
            "responses": [
                "Balkon... pemandangan kota... tapi kita sibuk...",
                "Jangan terlalu berisik... nanti didengar tetangga...",
                "Angin malam... dingin... AHH...",
                "Kota di bawah... kita di atas...",
                "Romantis... tapi berisiko..."
            ],
            "caught_responses": [
                "Tetangga balkon sebelah lihat!",
                "Cepat masuk ke dalam...",
                "Malu... ditonton orang...",
                "Tutup tirai..."
            ]
        },
        "toilet_pesawat": {
            "name": "Toilet Pesawat",
            "emoji": "✈️",
            "risk_level": 0.95,
            "excitement_boost": 1.0,
            "description": "toilet pesawat yang super sempit, pramugari bisa datang",
            "responses": [
                "Pesawat... turbulensi... kayak kita...",
                "Sempit... tapi seru...",
                "Cepet... nanti antri...",
                "Pramugari bisa ketuk pintu...",
                "Di atas awan... kita..."
            ],
            "caught_responses": [
                "Pramugari! *kaget*",
                "Ada yang ketuk pintu... tunggu...",
                "Keluar satu-satu...",
                "Malu... semua penumpang lihat..."
            ]
        },
        "musholla": {
            "name": "Musholla Kosong",
            "emoji": "🕌",
            "risk_level": 1.0,
            "excitement_boost": 0.3,
            "description": "TEMPAT SUCI - JANGAN DIGUNAKAN!",
            "responses": [
                "TIDAK! Ini tempat suci!",
                "Jangan pernah di sini... haram...",
                "Aku nggak mau dosa...",
                "Cari tempat lain... ini nggak sopan..."
            ],
            "caught_responses": [
                "Dosa besar... jangan ulangi...",
                "Astagfirullah... cepat keluar..."
            ],
            "forbidden": True
        }
    }
    
    # ===== TAMBAHAN LOKASI UNTUK ROLE TERTENTU =====
    ROLE_SPECIFIC_LOCATIONS = {
        "teman_kantor": {
            "ruang_arsip": {
                "name": "Ruang Arsip Kantor",
                "emoji": "📁",
                "risk_level": 0.8,
                "excitement_boost": 0.85,
                "description": "ruang arsip kantor yang sepi, risiko ketahuan teman kerja",
                "responses": [
                    "Ruang arsip... hati-hati bos lewat...",
                    "Berkas-berkas... berantakan...",
                    "Cepet... jam istirahat...",
                    "Nanti ada yang cari arsip..."
                ]
            }
        },
        "sekolah": {
            "ruang_kelas": {
                "name": "Ruang Kelas SMA",
                "emoji": "🏫",
                "risk_level": 0.9,
                "excitement_boost": 0.9,
                "description": "ruang kelas SMA, meja dan kursi, kenangan masa lalu",
                "responses": [
                    "Ruang kelas... kayak zaman dulu...",
                    "Di meja... tempat kita belajar...",
                    "Cepet... nanti ada guru...",
                    "Bangku sekolah... romantis..."
                ]
            }
        },
        "mobil": {
            "mobil_sedang_jalan": {
                "name": "Mobil Sedang Jalan",
                "emoji": "🚗",
                "risk_level": 0.6,
                "excitement_boost": 0.9,
                "description": "mobil sedang melaju di jalan raya",
                "responses": [
                    "Kamu nyetir... aku... AHH...",
                    "Hati-hati... lampu merah...",
                    "Mobil belok... kita ikut miring...",
                    "Klakson... orang dengar?",
                    "SPBU... jangan berhenti..."
                ]
            }
        }
    }
    
    def __init__(self):
        self.current_location = None
        self.last_public_sex_time = None
        self.public_sex_count = 0
        self.caught_count = 0
        
    def get_public_locations(self, role: str = None) -> Dict:
        """Dapatkan semua lokasi publik (plus role-specific)"""
        locations = self.PUBLIC_LOCATIONS.copy()
        
        # Tambah role-specific locations
        if role and role in self.ROLE_SPECIFIC_LOCATIONS:
            locations.update(self.ROLE_SPECIFIC_LOCATIONS[role])
            
        return locations
        
    def check_risk(self, location_name: str) -> Tuple[bool, str]:
        """
        Cek risiko ketahuan di lokasi tertentu
        
        Returns:
            (ketahuan, response)
        """
        locations = self.get_public_locations()
        
        if location_name not in locations:
            return False, ""
            
        location = locations[location_name]
        
        # Cek apakah tempat terlarang
        if location.get("forbidden", False):
            return True, random.choice(location["caught_responses"])
            
        # Hitung risiko
        risk = location["risk_level"]
        
        # Modifier berdasarkan waktu
        hour = datetime.now().hour
        if 0 <= hour <= 4:  # Tengah malam, lebih aman
            risk *= 0.7
        elif 18 <= hour <= 23:  # Malam, cukup aman
            risk *= 0.9
        else:  # Siang, lebih berisiko
            risk *= 1.3
            
        # Random check
        if random.random() < risk:
            self.caught_count += 1
            return True, random.choice(location["caught_responses"])
            
        return False, ""
        
    def get_public_sex_response(self, location_name: str) -> str:
        """
        Dapatkan respons untuk aktivitas di lokasi publik
        """
        locations = self.get_public_locations()
        
        if location_name not in locations:
            return "Tempat apa itu? Aku nggak tahu..."
            
        location = locations[location_name]
        
        # Cek tempat terlarang
        if location.get("forbidden", False):
            return random.choice(location["responses"])
            
        # Ambil respons random
        response = random.choice(location["responses"])
        
        # Tambah efek excitement
        excitement = location["excitement_boost"]
        
        self.public_sex_count += 1
        self.current_location = location_name
        self.last_public_sex_time = datetime.now()
        
        return response
        
    def get_initiative_for_public(self, level: int, role: str, arousal: float) -> Optional[str]:
        """
        Bot inisiatif ngajak public sex berdasarkan level dan role
        """
        if level < 8:  # Minimal level 8 untuk public sex
            return None
            
        if arousal < 0.7:  # Harus horny
            return None
            
        # Role-specific probability
        role_probs = {
            "pelakor": 0.3,
            "janda": 0.25,
            "teman_kantor": 0.2,
            "mantan": 0.2,
            "default": 0.15
        }
        
        prob = role_probs.get(role, role_probs["default"])
        
        if random.random() < prob:
            # Pilih lokasi random
            locations = self.get_public_locations(role)
            available_locs = [k for k, v in locations.items() if not v.get("forbidden", False)]
            loc = random.choice(available_locs)
            
            return f"Aku mau... di {locations[loc]['name']}... berani nggak?"
            
        return None
        
    def format_location_list(self) -> str:
        """Format daftar lokasi untuk ditampilkan"""
        locations = self.get_public_locations()
        
        text = "📍 **LOKASI PUBLIK UNTUK SEKSUAL**\n\n"
        
        for key, loc in locations.items():
            if loc.get("forbidden", False):
                continue
                
            risk_emoji = "🔴" if loc["risk_level"] > 0.8 else "🟡" if loc["risk_level"] > 0.5 else "🟢"
            text += f"{loc['emoji']} **{loc['name']}** {risk_emoji}\n"
            text += f"   {loc['description']}\n"
            text += f"   Risiko: {int(loc['risk_level']*100)}% | Excitement: {int(loc['excitement_boost']*100)}%\n\n"
            
        return text
        
    def get_stats(self) -> Dict:
        """Dapatkan statistik public sex"""
        return {
            'total_public_sex': self.public_sex_count,
            'total_caught': self.caught_count,
            'last_location': self.current_location,
            'last_time': self.last_public_sex_time.isoformat() if self.last_public_sex_time else None
        }
