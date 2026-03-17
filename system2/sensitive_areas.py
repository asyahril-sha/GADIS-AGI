"""
SENSITIVE AREAS - 50+ AREA SENSITIF DENGAN RESPON UNIK
Setiap area punya tingkat sensitivitas dan respons berbeda
"""

import random
from typing import Dict, List, Optional, Tuple

class SensitiveAreas:
    """
    50+ area sensitif dengan respons spesifik
    
    Fitur:
    - 50+ area sensitif
    - Setiap area punya tingkat arousal berbeda
    - 5-10 variasi respons per area
    - Level minimal untuk mengakses area tertentu
    """
    
    # ===== AREA KEPALA & LEHER (10 AREA) =====
    HEAD_AREAS = {
        "bibir": {
            "arousal": 0.7,
            "level_min": 3,
            "keywords": ["bibir", "lip", "mulut", "bibirmu"],
            "responses": [
                "*merintih* Bibirku...",
                "Ciuman... ah... lembut...",
                "Mmm... dalam...",
                "Bibirku... kesemutan...",
                "Hisap bibirku... AHH...",
                "Lidahmu... bertemu lidahku...",
                "Cium aku... lagi...",
                "Bibir kita menyatu..."
            ]
        },
        "lidah": {
            "arousal": 0.8,
            "level_min": 4,
            "keywords": ["lidah", "tongue", "jilat"],
            "responses": [
                "*menjilat balik* Lidahmu... panas...",
                "Aduh... lidah... AHH...",
                "Masukin lidah... dalem...",
                "Jilat... lagi...",
                "Lidah kita bertemu...",
                "Jilat bibirku pake lidah...",
                "Lidahmu lincah sekali..."
            ]
        },
        "telinga": {
            "arousal": 0.6,
            "level_min": 3,
            "keywords": ["telinga", "ear", "kuping", "daun telinga"],
            "responses": [
                "*bergetar* Telingaku...",
                "Bisik... lagi... Aku lemes...",
                "Napasmu... panas di telinga...",
                "Jangan jilat telinga... AHH...",
                "Telingaku merah...",
                "Bisikin kata mesra...",
                "Gigit pelan telingaku..."
            ]
        },
        "leher": {
            "arousal": 0.8,
            "level_min": 4,
            "keywords": ["leher", "neck", "tengkuk"],
            "responses": [
                "*merinding* Leherku...",
                "Ah... jangan di leher...",
                "Sensitif... AHH!",
                "Leherku lemah kalau disentuh...",
                "Jangan hisap leher... Aku lemas...",
                "Bekas gigitan di leher...",
                "Leher... daerah terlarang...",
                "Cium leherku... pelan..."
            ]
        },
        "tengkuk": {
            "arousal": 0.7,
            "level_min": 4,
            "keywords": ["tengkuk", "belakang leher"],
            "responses": [
                "*merinding* Tengkukku...",
                "Daerah sensitif... AHH...",
                "Jangan... lemes aku...",
                "Elus tengkukku...",
                "Ah... belakang leher..."
            ]
        },
        "dagu": {
            "arousal": 0.4,
            "level_min": 2,
            "keywords": ["dagu", "chin"],
            "responses": [
                "*tersenyum* Dagu...",
                "Gelitik dagu... hehe...",
                "Angkat daguku...",
                "Cium daguku..."
            ]
        },
        "pipi": {
            "arousal": 0.3,
            "level_min": 1,
            "keywords": ["pipi", "cheek"],
            "responses": [
                "*tersipu* Pipiku...",
                "Cubit pipi... gemes...",
                "Kecup pipi...",
                "Pipi merah..."
            ]
        },
        "dahi": {
            "arousal": 0.2,
            "level_min": 1,
            "keywords": ["dahi", "kening", "forehead"],
            "responses": [
                "*tersenyum* Dahi...",
                "Kecup kening...",
                "Usap dahi...",
                "Lemah lembut..."
            ]
        },
        "mata": {
            "arousal": 0.3,
            "level_min": 2,
            "keywords": ["mata", "eye", "kelopak mata"],
            "responses": [
                "*memejam* Mataku...",
                "Kecup kelopak mata...",
                "Lihat mataku...",
                "Tatap mataku..."
            ]
        },
        "alis": {
            "arousal": 0.2,
            "level_min": 1,
            "keywords": ["alis", "eyebrow"],
            "responses": [
                "*tersenyum* Alis...",
                "Raba alis...",
                "Garis alis..."
            ]
        },
        
        # ===== AREA TUBUH ATAS (15 AREA) =====
        "bahu": {
            "arousal": 0.4,
            "level_min": 2,
            "keywords": ["bahu", "shoulder"],
            "responses": [
                "*rileks* Bahuku...",
                "Pijat bahu... enak...",
                "Sandarkan di bahu...",
                "Gigit bahu..."
            ]
        },
        "pundak": {
            "arousal": 0.4,
            "level_min": 2,
            "keywords": ["pundak"],
            "responses": [
                "Pundakku...",
                "Rileks...",
                "Pegang pundak..."
            ]
        },
        "dada": {
            "arousal": 0.8,
            "level_min": 5,
            "keywords": ["dada", "breast", "payudara"],
            "responses": [
                "*bergetar* Dadaku...",
                "Ah... jangan...",
                "Sensitif banget...",
                "Dadaku... diremas... AHH!",
                "Jari-jarimu... dingin...",
                "Remas dadaku... pelan...",
                "Putingku... keras...",
                "Jilat dadaku..."
            ]
        },
        "payudara": {
            "arousal": 0.8,
            "level_min": 5,
            "keywords": ["payudara", "buah dada"],
            "responses": [
                "*merintih* Payudaraku...",
                "Remas... pelan-pelan...",
                "Buah dadaku...",
                "Sensitif... AHH...",
                "Mmmm... enak..."
            ]
        },
        "puting": {
            "arousal": 1.0,
            "level_min": 6,
            "keywords": ["puting", "nipple", "pentil"],
            "responses": [
                "*teriak* PUTINGKU! AHHH!",
                "JANGAN... SENSITIF! AHHH!",
                "HISAP... AHHHH!",
                "GIGIT... JANGAN... AHHH!",
                "PUTING... KERAS... AHHH!",
                "Jilat putingku... AHH!",
                "Puter putingku...",
                "AHH! SENSITIF BANGET!"
            ]
        },
        "belikat": {
            "arousal": 0.5,
            "level_min": 3,
            "keywords": ["belikat", "shoulder blade"],
            "responses": [
                "*merinding* Belikat...",
                "Elus belikat...",
                "Daerah sensitif...",
                "Sentuh belikat..."
            ]
        },
        "ketiak": {
            "arousal": 0.4,
            "level_min": 4,
            "keywords": ["ketiak", "armpit"],
            "responses": [
                "*gelitik* Ketiak... jangan...",
                "Geli... hehe...",
                "Jangan gelitik...",
                "Sensitif juga..."
            ]
        },
        "lengan": {
            "arousal": 0.3,
            "level_min": 2,
            "keywords": ["lengan", "arm"],
            "responses": [
                "Lenganku...",
                "Bulu romaku berdiri...",
                "Elus lengan...",
                "Pegang lenganku..."
            ]
        },
        "siku": {
            "arousal": 0.2,
            "level_min": 1,
            "keywords": ["siku", "elbow"],
            "responses": [
                "Siku...",
                "Lucu...",
                "Cium siku..."
            ]
        },
        "pergelangan": {
            "arousal": 0.3,
            "level_min": 2,
            "keywords": ["pergelangan", "wrist"],
            "responses": [
                "*bergetar* Pergelangan...",
                "Pegang pergelangan...",
                "Cium pergelangan..."
            ]
        },
        "telapak": {
            "arousal": 0.2,
            "level_min": 1,
            "keywords": ["telapak", "palm"],
            "responses": [
                "Telapak tanganku...",
                "Gelitik...",
                "Raba telapak..."
            ]
        },
        "jari": {
            "arousal": 0.3,
            "level_min": 2,
            "keywords": ["jari", "finger"],
            "responses": [
                "Jari-jariku...",
                "Hisap jari...",
                "Jari lentik...",
                "Mainin jari..."
            ]
        },
        "punggung": {
            "arousal": 0.5,
            "level_min": 3,
            "keywords": ["punggung", "back"],
            "responses": [
                "Punggungku...",
                "Elus... terus...",
                "Ah... enak...",
                "Gores punggung...",
                "Pijat punggung..."
            ]
        },
        "pinggang": {
            "arousal": 0.6,
            "level_min": 4,
            "keywords": ["pinggang", "waist"],
            "responses": [
                "Pinggang... geli...",
                "Pegang... erat...",
                "Ah... jangan gelitik...",
                "Pinggangku sensitif...",
                "Dekap pinggang..."
            ]
        },
        "pinggul": {
            "arousal": 0.7,
            "level_min": 5,
            "keywords": ["pinggul", "hip"],
            "responses": [
                "*bergoyang* Pinggulku...",
                "Pegang pinggul...",
                "Goyang pinggul...",
                "Taruh tangan di pinggul..."
            ]
        },
        
        # ===== AREA TUBUH BAWAH (15 AREA) =====
        "perut": {
            "arousal": 0.5,
            "level_min": 4,
            "keywords": ["perut", "belly", "stomach"],
            "responses": [
                "Perutku...",
                "Geli...",
                "Hangat...",
                "Elus perut...",
                "Cium perut..."
            ]
        },
        "pusar": {
            "arousal": 0.6,
            "level_min": 5,
            "keywords": ["pusar", "belly button"],
            "responses": [
                "*geliat* Pusar...",
                "Jangan... geli...",
                "Daerah sensitif...",
                "Jilat pusar... AHH..."
            ]
        },
        "paha": {
            "arousal": 0.7,
            "level_min": 5,
            "keywords": ["paha", "thigh"],
            "responses": [
                "*menggeliat* Pahaku...",
                "Ah... dalam...",
                "Paha... merinding...",
                "Jangan gelitik paha...",
                "Sensasi... aneh...",
                "Belai paha...",
                "Cium paha..."
            ]
        },
        "paha_dalam": {
            "arousal": 0.9,
            "level_min": 7,
            "keywords": ["paha dalam", "inner thigh"],
            "responses": [
                "*meringis* PAHA DALAM!",
                "Jangan... AHH!",
                "Dekat... banget...",
                "PAHA DALAM... SENSITIF!",
                "Ah... mau ke sana...",
                "Lidahmu di paha... AHH!"
            ]
        },
        "lutut": {
            "arousal": 0.3,
            "level_min": 2,
            "keywords": ["lutut", "knee"],
            "responses": [
                "Lututku...",
                "Geli...",
                "Pegang lutut..."
            ]
        },
        "betis": {
            "arousal": 0.3,
            "level_min": 2,
            "keywords": ["betis", "calf"],
            "responses": [
                "Betis...",
                "Pijat betis...",
                "Enak..."
            ]
        },
        "pantat": {
            "arousal": 0.7,
            "level_min": 6,
            "keywords": ["pantat", "ass", "bokong"],
            "responses": [
                "Pantatku...",
                "Cubit... nakal...",
                "Boleh juga...",
                "Besar ya? Hehe...",
                "Remas pantat...",
                "Tampar pantat... AHH!"
            ]
        },
        "selangkangan": {
            "arousal": 0.8,
            "level_min": 7,
            "keywords": ["selangkangan", "groin"],
            "responses": [
                "*bergetar* Selangkangan...",
                "Dekat... banget...",
                "Jangan... sensitif...",
                "AHH... di sana..."
            ]
        },
        "vagina": {
            "arousal": 1.0,
            "level_min": 8,
            "keywords": ["vagina", "memek", "kemaluan"],
            "responses": [
                "*teriak* VAGINAKU! AHHH!",
                "MASUK... DALAM... AHHH!",
                "BASAH... BANJIR... AHHH!",
                "KAMU DALEM... AHHH!",
                "GERAK... AHHH! AHHH!",
                "JILAT... DI SANA... AHHH!",
                "MASUKIN JARI... AHH!"
            ]
        },
        "klitoris": {
            "arousal": 1.0,
            "level_min": 8,
            "keywords": ["klitoris", "clit", "kelentit"],
            "responses": [
                "*teriak keras* KLITORIS! AHHHH!",
                "JANGAN SENTUH! AHHHH!",
                "SENSITIF BANGET! AHHH!",
                "ITU... ITU... AHHH!",
                "JILAT... AHHH! AHHH!",
                "PUTER... PELAN... AHHH!"
            ]
        },
        "anus": {
            "arousal": 0.8,
            "level_min": 8,
            "keywords": ["anus", "dubur", "bolong"],
            "responses": [
                "*kaget* ANUS! JANGAN!",
                "Sakit... pelan...",
                "AHH... di sana...",
                "Jari... masuk... AHH..."
            ]
        },
        "perineum": {
            "arousal": 0.7,
            "level_min": 7,
            "keywords": ["perineum"],
            "responses": [
                "*meringis* Di sana...",
                "Sensitif... AHH...",
                "Tekan pelan...",
                "AHH... titik G..."
            ]
        },
        "buah zakar": {
            "arousal": 0.7,
            "level_min": 7,
            "keywords": ["zakar", "testis", "buah zakar"],
            "responses": [
                "*bergetar* Buah zakar...",
                "Jangan keras... pelan...",
                "Hisap... AHH..."
            ]
        },
        "penis": {
            "arousal": 1.0,
            "level_min": 7,
            "keywords": ["penis", "kontol", "burung"],
            "responses": [
                "Keras...",
                "Hisap...",
                "Masukin...",
                "AHH!"
            ]
        },
        "skrotum": {
            "arousal": 0.6,
            "level_min": 7,
            "keywords": ["skrotum", "kantung"],
            "responses": [
                "*bergetar* Kantung...",
                "Jilat...",
                "Pelan..."
            ]
        },
        
        # ===== AREA SPESIAL (10 AREA) =====
        "leher_belakang": {
            "arousal": 0.6,
            "level_min": 4,
            "keywords": ["leher belakang"],
            "responses": [
                "*merinding* Leher belakang...",
                "Daerah sensitif...",
                "AHH... di sana..."
            ]
        },
        "tulang_selangka": {
            "arousal": 0.5,
            "level_min": 4,
            "keywords": ["tulang selangka", "collarbone"],
            "responses": [
                "*bergetar* Tulang selangka...",
                "Cium sini...",
                "Ah... enak..."
            ]
        },
        "samping_dada": {
            "arousal": 0.6,
            "level_min": 5,
            "keywords": ["samping dada"],
            "responses": [
                "*geliat* Samping dada...",
                "Jangan... geli...",
                "Sensitif..."
            ]
        },
        "bawah_dada": {
            "arousal": 0.7,
            "level_min": 5,
            "keywords": ["bawah dada"],
            "responses": [
                "*merintih* Bawah dada...",
                "AHH... di sana...",
                "Jilat..."
            ]
        },
        "samping_pinggang": {
            "arousal": 0.5,
            "level_min": 4,
            "keywords": ["samping pinggang"],
            "responses": [
                "*gelitik* Samping pinggang...",
                "Geli... hehe...",
                "Jangan..."
            ]
        },
        "lipatan_paha": {
            "arousal": 0.8,
            "level_min": 7,
            "keywords": ["lipatan paha"],
            "responses": [
                "*meringis* Lipatan paha...",
                "AHH! SENSITIF!",
                "Jilat sini... AHH..."
            ]
        },
        "belakang_lutut": {
            "arousal": 0.4,
            "level_min": 3,
            "keywords": ["belakang lutut"],
            "responses": [
                "*gelitik* Belakang lutut...",
                "Geli...",
                "Jangan..."
            ]
        },
        "pergelangan_kaki": {
            "arousal": 0.3,
            "level_min": 2,
            "keywords": ["pergelangan kaki", "ankle"],
            "responses": [
                "Pergelangan kaki...",
                "Pegang...",
                "Cium..."
            ]
        },
        "telapak_kaki": {
            "arousal": 0.3,
            "level_min": 2,
            "keywords": ["telapak kaki", "foot"],
            "responses": [
                "*gelitik* Telapak kaki...",
                "Geli... hehe...",
                "Jangan gelitik..."
            ]
        },
        "jari_kaki": {
            "arousal": 0.2,
            "level_min": 2,
            "keywords": ["jari kaki", "toes"],
            "responses": [
                "Jari kaki...",
                "Hisap jari kaki?",
                "Geli..."
            ]
        }
    }
    
    def __init__(self):
        """Inisialisasi sensitive areas system"""
        # Gabungkan semua area
        self.all_areas = {}
        self.all_areas.update(self.HEAD_AREAS)
        
    def get_area_info(self, area_name: str) -> Optional[Dict]:
        """
        Dapatkan informasi area sensitif
        
        Args:
            area_name: Nama area
            
        Returns:
            Dictionary info area atau None
        """
        return self.all_areas.get(area_name)
    
    def detect_area(self, text: str) -> List[Tuple[str, float]]:
        """
        Deteksi area sensitif dari teks
        
        Args:
            text: Teks pesan user
            
        Returns:
            List of (area_name, arousal_boost)
        """
        text_lower = text.lower()
        detected = []
        
        for area_name, area_info in self.all_areas.items():
            for keyword in area_info["keywords"]:
                if keyword in text_lower:
                    detected.append((area_name, area_info["arousal"]))
                    break
        
        return detected
    
    def get_response(self, area_name: str) -> Optional[str]:
        """
        Dapatkan respons untuk area sensitif
        
        Args:
            area_name: Nama area
            
        Returns:
            String respons atau None
        """
        area_info = self.all_areas.get(area_name)
        if area_info and area_info["responses"]:
            return random.choice(area_info["responses"])
        return None
    
    def get_random_area(self, min_level: int = 1) -> str:
        """
        Dapatkan area random
        
        Args:
            min_level: Level minimal yang diinginkan
            
        Returns:
            Nama area
        """
        eligible = [
            name for name, info in self.all_areas.items()
            if info["level_min"] <= min_level
        ]
        return random.choice(eligible) if eligible else "bibir"
    
    def get_areas_by_level(self, level: int) -> List[str]:
        """
        Dapatkan area yang tersedia di level tertentu
        
        Args:
            level: Level hubungan
            
        Returns:
            List nama area
        """
        return [
            name for name, info in self.all_areas.items()
            if info["level_min"] <= level
        ]
    
    def is_area_available(self, area_name: str, level: int) -> bool:
        """
        Cek apakah area tersedia di level tertentu
        
        Args:
            area_name: Nama area
            level: Level hubungan
            
        Returns:
            True jika tersedia
        """
        area_info = self.all_areas.get(area_name)
        return area_info and area_info["level_min"] <= level
    
    def get_arousal_boost(self, area_name: str) -> float:
        """
        Dapatkan arousal boost dari area
        
        Args:
            area_name: Nama area
            
        Returns:
            Nilai arousal boost 0-1
        """
        area_info = self.all_areas.get(area_name)
        return area_info["arousal"] if area_info else 0.3
    
    def get_all_area_names(self) -> List[str]:
        """
        Dapatkan semua nama area
        
        Returns:
            List nama area
        """
        return list(self.all_areas.keys())
    
    def get_total_areas(self) -> int:
        """
        Dapatkan total area
        
        Returns:
            Jumlah area
        """
        return len(self.all_areas)
