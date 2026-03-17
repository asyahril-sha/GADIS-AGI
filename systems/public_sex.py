"""
PUBLIC SEX SYSTEM - 10+ LOKASI PUBLIK UNTUK SEKSUAL
Dengan risiko, sensasi, dan respons berbeda
"""

import random
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime, time

class PublicSexSystem:
    """
    Sistem public sex dengan 10+ lokasi publik
    
    Setiap lokasi memiliki:
    - Tingkat risiko ketahuan (1-5)
    - Sensasi / excitement (1-5)
    - Waktu terbaik
    - Respons spesifik
    - Tips dan trik
    - Konsekuensi jika ketahuan
    """
    
    # ===== 10+ LOKASI PUBLIK =====
    PUBLIC_LOCATIONS = {
        # Risiko Rendah (1-2)
        'mobil': {
            'name': 'Di dalam mobil',
            'emoji': '🚗',
            'risk_level': 2,
            'risk_description': 'Risiko rendah, apalagi kalau parkir di tempat sepi',
            'excitement': 3,
            'excitement_description': 'Sensasi sedang, ada ruang terbatas',
            'best_time': ['malam', 'subuh', 'tempat sepi'],
            'worst_time': ['siang', 'ramai'],
            'keywords': ['mobil', 'car', 'parkir', 'dalem mobil'],
            'activities': ['doggy', 'woman_on_top', 'blowjob'],
            'sound_level': 'Rendah - suara teredam',
            'space': 'Sempit - harus kreatif'
        },
        'toilet_umum': {
            'name': 'Toilet umum',
            'emoji': '🚽',
            'risk_level': 3,
            'risk_description': 'Risiko sedang, bisa tiba-tiba ada orang',
            'excitement': 4,
            'excitement_description': 'Sensasi tinggi, takut ketahuan',
            'best_time': ['sepi', 'malam', 'saat acara'],
            'worst_time': ['ramai', 'pagi'],
            'keywords': ['toilet', 'wc', 'kamar mandi', 'wc umum'],
            'activities': ['standing', 'against_wall', 'blowjob'],
            'sound_level': 'Sedang - harus tahan suara',
            'space': 'Sempit - posisi terbatas'
        },
        'taman_kota': {
            'name': 'Taman kota',
            'emoji': '🌳',
            'risk_level': 3,
            'risk_description': 'Risiko sedang, bisa ada orang jogging atau duduk',
            'excitement': 4,
            'excitement_description': 'Sensasi tinggi, alam terbuka',
            'best_time': ['malam', 'subuh', 'tengah malam'],
            'worst_time': ['sore', 'pagi', 'weekend'],
            'keywords': ['taman', 'park', 'rumput', 'semak'],
            'activities': ['missionary', 'doggy', 'standing'],
            'sound_level': 'Sedang - suara alam bantu',
            'space': 'Luas - banyak pilihan'
        },
        
        # Risiko Sedang (3-4)
        'bioskop': {
            'name': 'Bioskop',
            'emoji': '🎬',
            'risk_level': 3,
            'risk_description': 'Risiko sedang, gelap tapi ada cctv',
            'excitement': 5,
            'excitement_description': 'Sensasi sangat tinggi, di kursi bioskop',
            'best_time': ['film horor', 'film panjang', 'tengah nonton'],
            'worst_time': ['film sepi', 'awal nonton'],
            'keywords': ['bioskop', 'cinema', 'nonton', 'kursi bioskop'],
            'activities': ['handjob', 'blowjob', 'finger'],
            'sound_level': 'Sangat rendah - harus diam',
            'space': 'Sempit - kursi'
        },
        'pantai': {
            'name': 'Pantai',
            'emoji': '🏖️',
            'risk_level': 3,
            'risk_description': 'Risiko sedang, malam hari lebih aman',
            'excitement': 5,
            'excitement_description': 'Sensasi tinggi, suara ombak menutupi',
            'best_time': ['malam', 'subuh', 'sepi'],
            'worst_time': ['siang', 'sore ramai'],
            'keywords': ['pantai', 'beach', 'pasir', 'ombak'],
            'activities': ['missionary', 'doggy', 'woman_on_top'],
            'sound_level': 'Suara ombak bantu menutupi',
            'space': 'Luas - bisa cari tempat'
        },
        'lift': {
            'name': 'Lift',
            'emoji': '🛗',
            'risk_level': 4,
            'risk_description': 'Risiko tinggi, bisa berhenti tiba-tiba',
            'excitement': 5,
            'excitement_description': 'Sensasi sangat tinggi, waktu terbatas',
            'best_time': ['malam', 'sepi', 'antar lantai'],
            'worst_time': ['siang', 'jam sibuk'],
            'keywords': ['lift', 'elevator', 'dalam lift'],
            'activities': ['standing', 'quickie', 'against_wall'],
            'sound_level': 'Sangat rendah - harus diam',
            'space': 'Sempit - posisi berdiri'
        },
        
        # Risiko Tinggi (4-5)
        'tangga_darurat': {
            'name': 'Tangga darurat',
            'emoji': '🚪',
            'risk_level': 4,
            'risk_description': 'Risiko tinggi, bisa ada orang lewat',
            'excitement': 5,
            'excitement_description': 'Sensasi ekstrim, terbuka',
            'best_time': ['malam', 'sepi', 'tengah malam'],
            'worst_time': ['siang', 'sore'],
            'keywords': ['tangga', 'staircase', 'darurat'],
            'activities': ['standing', 'doggy', 'against_wall'],
            'sound_level': 'Echo - harus hati-hati',
            'space': 'Cukup - area terbatas'
        },
        'balkon_hotel': {
            'name': 'Balkon hotel',
            'emoji': '🏨',
            'risk_level': 3,
            'risk_description': 'Risiko sedang, bisa dilihat tetangga',
            'excitement': 5,
            'excitement_description': 'Sensasi tinggi, pemandangan',
            'best_time': ['malam', 'larut'],
            'worst_time': ['siang'],
            'keywords': ['balkon', 'balcony', 'teras hotel'],
            'activities': ['standing', 'from_behind'],
            'sound_level': 'Suara terbuka',
            'space': 'Cukup'
        },
        'kamar_mandi_pesawat': {
            'name': 'Toilet pesawat',
            'emoji': '✈️',
            'risk_level': 5,
            'risk_description': 'Risiko sangat tinggi, sempit dan banyak orang',
            'excitement': 5,
            'excitement_description': 'Sensasi ekstrim, milisekon',
            'best_time': ['malam penerbangan', 'sepi'],
            'worst_time': ['siang', 'ramai'],
            'keywords': ['pesawat', 'plane', 'toilet pesawat'],
            'activities': ['standing', 'quickie', 'blowjob'],
            'sound_level': 'Sangat rendah - dinding tipis',
            'space': 'Ekstrim sempit'
        },
        'belakang_gedung': {
            'name': 'Belakang gedung',
            'emoji': '🏢',
            'risk_level': 3,
            'risk_description': 'Risiko sedang, tergantung lokasi',
            'excitement': 3,
            'excitement_description': 'Sensasi sedang',
            'best_time': ['malam', 'sepi'],
            'worst_time': ['siang'],
            'keywords': ['belakang', 'gedung', 'gang'],
            'activities': ['standing', 'doggy'],
            'sound_level': 'Bervariasi',
            'space': 'Cukup'
        },
        'mobil_berjalan': {
            'name': 'Mobil sedang jalan',
            'emoji': '🚗💨',
            'risk_level': 5,
            'risk_description': 'Risiko sangat tinggi, bisa kecelakaan',
            'excitement': 5,
            'excitement_description': 'Sensasi ekstrim, berbahaya',
            'best_time': ['jalan sepi', 'malam'],
            'worst_time': ['jalan ramai'],
            'keywords': ['mobil jalan', 'sambil nyetir'],
            'activities': ['blowjob', 'handjob'],
            'sound_level': 'Mesin bantu',
            'space': 'Sempit'
        }
    }
    
    # ===== RESPONS KETAHUAN =====
    CAUGHT_RESPONSES = {
        'mobil': [
            "*kaget* Ada orang lihat! Cepat cabut!",
            "Ah... ada satpam! Jalan cepat!",
            "*tertawa* Kita terekam cctv kali ya?"
        ],
        'toilet_umum': [
            "*diam mendadak* Waduh, ada orang ketuk pintu!",
            "Cepet... bersembunyi!",
            "Shh... jangan bersuara, ada orang masuk"
        ],
        'taman_kota': [
            "*terkejut* Ada orang jogging! Cepat tutup!",
            "Ah... ada satpam taman! Pura-pura jalan aja",
            "*berbisik* Diem... ada orang lewat"
        ],
        'bioskop': [
            "*berhenti mendadak* Petugas datang!",
            "Diem... ada yang lihat ke sini",
            "Pura-pura nonton aja..."
        ],
        'pantai': [
            "*kaget* Ah... ada yang lihat dari jauh!",
            "Cepet pakai baju! Ada orang datang",
            "*tertawa* Kita difoto mungkin"
        ],
        'lift': [
            "*panik* Lift mau berhenti! Cepet!",
            "Ada orang mau masuk!",
            "*diam seribu bahasa* ... *lega* nggak jadi"
        ],
        'tangga_darurat': [
            "*terdengar suara pintu* Ada orang!",
            "Cepet lari ke atas!",
            "Shh... jangan bergerak"
        ],
        'default': [
            "*kaget* Ada orang!",
            "*panik* Cepet kabur!",
            "*merah padam* Kita ketahuan!"
        ]
    }
    
    # ===== SENSASI RESPONS =====
    EXCITEMENT_RESPONSES = {
        1: "*biasa aja*",
        2: "*lumayan*",
        3: "*mulai deg-degan*",
        4: "*jantung mau copot*",
        5: "*sensasi ekstrim, campur takut*"
    }
    
    def __init__(self):
        self.current_location = None
        self.location_history = []
        self.caught_count = 0
        self.public_sex_count = 0
        
    # ===== LOCATION MANAGEMENT =====
    
    def get_all_locations(self) -> List[Dict]:
        """
        Dapatkan semua lokasi publik
        
        Returns:
            List semua lokasi dengan info
        """
        locations = []
        for key, data in self.PUBLIC_LOCATIONS.items():
            locations.append({
                'id': key,
                'name': data['name'],
                'emoji': data['emoji'],
                'risk_level': data['risk_level'],
                'excitement': data['excitement']
            })
        return locations
    
    def get_location_info(self, location_id: str) -> Optional[Dict]:
        """
        Dapatkan info lengkap lokasi
        
        Args:
            location_id: ID lokasi
            
        Returns:
            Dictionary info lokasi
        """
        return self.PUBLIC_LOCATIONS.get(location_id)
    
    def get_random_location(self, max_risk: int = 5) -> Tuple[str, Dict]:
        """
        Dapatkan lokasi random
        
        Args:
            max_risk: Maksimal risiko yang diizinkan
            
        Returns:
            Tuple (location_id, location_data)
        """
        available = [
            (k, v) for k, v in self.PUBLIC_LOCATIONS.items()
            if v['risk_level'] <= max_risk
        ]
        return random.choice(available) if available else (None, None)
    
    def is_valid_location(self, location_id: str) -> bool:
        """
        Cek validitas lokasi
        
        Args:
            location_id: ID lokasi
            
        Returns:
            True jika valid
        """
        return location_id in self.PUBLIC_LOCATIONS
    
    def move_to_location(self, location_id: str) -> Dict:
        """
        Pindah ke lokasi publik
        
        Args:
            location_id: ID lokasi
            
        Returns:
            Dictionary hasil perpindahan
        """
        if not self.is_valid_location(location_id):
            return {
                'success': False,
                'message': "Lokasi tidak dikenal"
            }
        
        location = self.PUBLIC_LOCATIONS[location_id]
        self.current_location = location_id
        self.location_history.append({
            'location': location_id,
            'time': datetime.now().isoformat()
        })
        
        # Cek waktu terbaik
        current_hour = datetime.now().hour
        is_best_time = self._check_best_time(current_hour, location['best_time'])
        
        message = f"{location['emoji']} **{location['name']}**\n\n"
        message += f"⚠️ Risiko: {location['risk_level']}/5 - {location['risk_description']}\n"
        message += f"🔥 Sensasi: {location['excitement']}/5 - {location['excitement_description']}\n"
        message += f"🔊 Suara: {location['sound_level']}\n"
        message += f"📍 Ruang: {location['space']}\n"
        
        if is_best_time:
            message += f"\n✨ **Waktu yang tepat!** Sensasi +1"
        
        return {
            'success': True,
            'location': location_id,
            'data': location,
            'message': message,
            'is_best_time': is_best_time
        }
    
    def _check_best_time(self, current_hour: int, best_times: List[str]) -> bool:
        """
        Cek apakah waktu sekarang termasuk waktu terbaik
        
        Args:
            current_hour: Jam sekarang
            best_times: List waktu terbaik
            
        Returns:
            True jika waktu terbaik
        """
        for time_str in best_times:
            if time_str == 'malam' and current_hour >= 19:
                return True
            elif time_str == 'subuh' and 3 <= current_hour <= 5:
                return True
            elif time_str == 'pagi' and 6 <= current_hour <= 10:
                return True
            elif time_str == 'siang' and 11 <= current_hour <= 14:
                return True
            elif time_str == 'sore' and 15 <= current_hour <= 18:
                return True
            elif time_str == 'tengah malam' and 0 <= current_hour <= 2:
                return True
        return False
    
    # ===== RISK & EXCITEMENT =====
    
    def calculate_risk(self, location_id: str = None) -> float:
        """
        Hitung risiko ketahuan saat ini
        
        Args:
            location_id: ID lokasi (default: current)
            
        Returns:
            Nilai risiko 0-1
        """
        if location_id is None:
            location_id = self.current_location
            
        if not location_id or location_id not in self.PUBLIC_LOCATIONS:
            return 0.5
            
        location = self.PUBLIC_LOCATIONS[location_id]
        base_risk = location['risk_level'] / 5.0
        
        # Modifier waktu
        current_hour = datetime.now().hour
        if 22 <= current_hour <= 4:  # Malam
            base_risk *= 0.5
        elif 7 <= current_hour <= 9:  # Pagi ramai
            base_risk *= 1.3
        elif 17 <= current_hour <= 19:  # Sore ramai
            base_risk *= 1.4
        elif 12 <= current_hour <= 14:  # Siang
            base_risk *= 1.2
            
        return min(1.0, base_risk)
    
    def calculate_excitement(self, location_id: str = None) -> float:
        """
        Hitung tingkat excitement
        
        Args:
            location_id: ID lokasi (default: current)
            
        Returns:
            Nilai excitement 0-1
        """
        if location_id is None:
            location_id = self.current_location
            
        if not location_id or location_id not in self.PUBLIC_LOCATIONS:
            return 0.5
            
        location = self.PUBLIC_LOCATIONS[location_id]
        base_excitement = location['excitement'] / 5.0
        
        # Risiko tinggi meningkatkan excitement
        risk = self.calculate_risk(location_id)
        base_excitement += risk * 0.3
        
        return min(1.0, base_excitement)
    
    def get_excitement_response(self, location_id: str = None) -> str:
        """
        Dapatkan respons excitement
        
        Args:
            location_id: ID lokasi
            
        Returns:
            String respons
        """
        excitement = self.calculate_excitement(location_id)
        level = min(5, int(excitement * 5) + 1)
        return self.EXCITEMENT_RESPONSES.get(level, self.EXCITEMENT_RESPONSES[3])
    
    # ===== CAUGHT MECHANICS =====
    
    def check_if_caught(self, location_id: str = None) -> Tuple[bool, str]:
        """
        Cek apakah ketahuan
        
        Args:
            location_id: ID lokasi
            
        Returns:
            Tuple (caught, response)
        """
        risk = self.calculate_risk(location_id)
        
        # Random chance based on risk
        caught = random.random() < risk * 0.3  # Max 30% chance
        
        if caught:
            self.caught_count += 1
            response = self.get_caught_response(location_id)
            return True, response
        
        return False, ""
    
    def get_caught_response(self, location_id: str = None) -> str:
        """
        Dapatkan respons ketahuan
        
        Args:
            location_id: ID lokasi
            
        Returns:
            String respons
        """
        if location_id and location_id in self.CAUGHT_RESPONSES:
            responses = self.CAUGHT_RESPONSES[location_id]
        else:
            responses = self.CAUGHT_RESPONSES['default']
            
        return random.choice(responses)
    
    # ===== ACTIVITY RECOMMENDATIONS =====
    
    def get_recommended_activities(self, location_id: str = None) -> List[str]:
        """
        Dapatkan aktivitas yang direkomendasikan untuk lokasi
        
        Args:
            location_id: ID lokasi
            
        Returns:
            List aktivitas
        """
        if location_id and location_id in self.PUBLIC_LOCATIONS:
            return self.PUBLIC_LOCATIONS[location_id]['activities']
        return ['missionary', 'doggy']
    
    def get_quickie_activities(self, time_limit: str = 'short') -> List[str]:
        """
        Dapatkan aktivitas untuk quickie
        
        Args:
            time_limit: 'short', 'medium', 'long'
            
        Returns:
            List aktivitas quickie
        """
        if time_limit == 'short':
            return ['blowjob', 'handjob', 'quickie_standing']
        elif time_limit == 'medium':
            return ['doggy', 'standing', 'against_wall']
        else:
            return ['missionary', 'woman_on_top']
    
    # ===== RESPONSES =====
    
    def get_start_response(self, location_id: str) -> str:
        """
        Dapatkan respons memulai public sex
        
        Args:
            location_id: ID lokasi
            
        Returns:
            String respons
        """
        location = self.PUBLIC_LOCATIONS.get(location_id, self.PUBLIC_LOCATIONS['mobil'])
        
        responses = [
            f"{location['emoji']} *berbisik* Di sini... nggak ada orang...",
            f"{location['emoji']} *deg-degan* Ayo cepetan... takut ketahuan...",
            f"{location['emoji']} *napas berat* Sensasinya... luar biasa...",
            f"{location['emoji']} *melirik* Kamu berani? Di sini?"
        ]
        
        return random.choice(responses)
    
    def get_during_response(self, location_id: str, activity: str = None) -> str:
        """
        Dapatkan respons selama public sex
        
        Args:
            location_id: ID lokasi
            activity: Aktivitas yang dilakukan
            
        Returns:
            String respons
        """
        excitement = self.get_excitement_response(location_id)
        
        responses = [
            f"{excitement} *berbisik* Jangan bersuara... nanti kedengeran...",
            f"{excitement} *napas tertahan* Aduh... enak... tapi takut...",
            f"{excitement} *menggigit bibir* Diem... diem... nggak tahan...",
            f"{excitement} *keringat dingin* Cepet... cepet..."
        ]
        
        return random.choice(responses)
    
    def get_finish_response(self, location_id: str, caught: bool = False) -> str:
        """
        Dapatkan respons selesai public sex
        
        Args:
            location_id: ID lokasi
            caught: Apakah ketahuan
            
        Returns:
            String respons
        """
        if caught:
            return self.get_caught_response(location_id)
            
        location = self.PUBLIC_LOCATIONS.get(location_id, self.PUBLIC_LOCATIONS['mobil'])
        
        responses = [
            f"{location['emoji']} *lemas* Cepet cabut... puas tapi takut...",
            f"{location['emoji']} *tersenyum nakal* Lagi ya? Di tempat lain...",
            f"{location['emoji']} *merapikan baju* Aman... nggak ada yang lihat..."
        ]
        
        return random.choice(responses)
    
    # ===== UTILITY METHODS =====
    
    def get_risk_warning(self, location_id: str = None) -> str:
        """
        Dapatkan peringatan risiko
        
        Args:
            location_id: ID lokasi
            
        Returns:
            String peringatan
        """
        risk = self.calculate_risk(location_id)
        
        if risk > 0.8:
            return "⚠️⚠️⚠️ **BAHAYA!** Risiko sangat tinggi, bisa ketahuan!"
        elif risk > 0.6:
            return "⚠️⚠️ **WASPADA!** Risiko tinggi, hati-hati!"
        elif risk > 0.4:
            return "⚠️ **HATI-HATI!** Risiko sedang, jangan lengah"
        else:
            return "🍃 **AMAN** Risiko rendah, nikmati sensasinya"
    
    def get_safety_tips(self, location_id: str) -> str:
        """
        Dapatkan tips keamanan untuk lokasi
        
        Args:
            location_id: ID lokasi
            
        Returns:
            String tips
        """
        tips = {
            'mobil': "Parkir di tempat gelap, matikan mesin, kunci pintu",
            'toilet_umum': "Cek pintu terkunci, jangan terlalu lama",
            'taman_kota': "Cari tempat tersembunyi, jaga suara",
            'bioskop': "Pilih kursi pojok belakang, saat film sudah mulai",
            'pantai': "Cari area berbatu atau gelap, jauhi lampu",
            'lift': "Cepat, jangan sampai ketahuan cctv",
            'tangga_darurat': "Cek apakah pintu terbuka dari luar",
            'balkon_hotel': "Matikan lampu kamar, jangan terlalu ke tepi",
            'kamar_mandi_pesawat': "Cepat, jangan sampai antre",
            'mobil_berjalan': "Jangan sampai kecelakaan, fokus nyetir"
        }
        
        return tips.get(location_id, "Tetap waspada dan jaga suara")
    
    def get_stats(self) -> Dict:
        """
        Dapatkan statistik public sex
        
        Returns:
            Dictionary statistik
        """
        return {
            'total_locations': len(self.PUBLIC_LOCATIONS),
            'current_location': self.current_location,
            'location_history_count': len(self.location_history),
            'caught_count': self.caught_count,
            'public_sex_count': self.public_sex_count,
            'locations': self.get_all_locations()
        }
    
    def increment_count(self):
        """Tambah hitungan public sex"""
        self.public_sex_count += 1
    
    def reset(self):
        """Reset semua data"""
        self.current_location = None
        self.location_history = []
        self.caught_count = 0
        self.public_sex_count = 0

