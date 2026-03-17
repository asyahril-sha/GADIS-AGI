"""
SEX ACTIVITIES - 50+ AKTIVITAS SEKSUAL DENGAN RESPON UNIK
Foreplay, Oral, Penetrasi, BDSM, Roleplay, Public
"""

import random
from typing import Dict, List, Optional, Tuple, Union

class SexActivities:
    """
    50+ aktivitas seksual dengan respons spesifik
    
    Fitur:
    - 10 aktivitas ciuman & foreplay
    - 10 aktivitas oral
    - 10 aktivitas penetrasi
    - 8 aktivitas BDSM
    - 7 aktivitas roleplay
    - 5 aktivitas public
    - Total: 50 aktivitas
    """
    
    # ===== 10 AKTIVITAS CIUMAN & FOREPLAY =====
    KISSING_ACTIVITIES = {
        "cium_bibir": {
            "name": "Cium Bibir",
            "keywords": ["cium", "kiss", "ciuman", "kecup"],
            "arousal": 0.3,
            "responses": [
                "*merespon ciuman* Mmm...",
                "*lemas* Ciumanmu...",
                "Lagi...",
                "Cium... bibir...",
                "French kiss... dalam...",
                "Lidah... masuk...",
                "Mmm... enak..."
            ],
            "level_min": 1
        },
        "cium_dahi": {
            "name": "Cium Dahi",
            "keywords": ["cium dahi", "kiss forehead"],
            "arousal": 0.1,
            "responses": [
                "*tersenyum manis* Cium dahi...",
                "Romantis...",
                "Aku suka...",
                "Lembut..."
            ],
            "level_min": 1
        },
        "cium_leher": {
            "name": "Cium Leher",
            "keywords": ["cium leher", "kiss neck", "neck kiss"],
            "arousal": 0.6,
            "responses": [
                "*merinding* Leherku...",
                "Ah... jangan...",
                "Sensitif...",
                "Hisap leher... AHH!",
                "Leherku lemah...",
                "Bekas... nanti..."
            ],
            "level_min": 3
        },
        "cium_pipi": {
            "name": "Cium Pipi",
            "keywords": ["cium pipi", "kiss cheek"],
            "arousal": 0.1,
            "responses": [
                "*tersipu* Pipiku...",
                "Manis...",
                "Cium lagi...",
                "Hehe..."
            ],
            "level_min": 1
        },
        "cium_mata": {
            "name": "Cium Mata",
            "keywords": ["cium mata", "kiss eyes"],
            "arousal": 0.2,
            "responses": [
                "*pejamkan mata* Lembut...",
                "Mataku...",
                "Romantis...",
                "Aku suka..."
            ],
            "level_min": 2
        },
        "cium_telinga": {
            "name": "Cium Telinga",
            "keywords": ["cium telinga", "kiss ear"],
            "arousal": 0.5,
            "responses": [
                "*bergetar* Telingaku...",
                "Bisik... lagi...",
                "Napasmu... panas...",
                "Telinga... merah...",
                "Ah... jangan tiup..."
            ],
            "level_min": 3
        },
        "cium_punggung": {
            "name": "Cium Punggung",
            "keywords": ["cium punggung", "kiss back"],
            "arousal": 0.4,
            "responses": [
                "*merinding* Punggungku...",
                "Ah... dari belakang...",
                "Lanjut...",
                "Nikmat..."
            ],
            "level_min": 4
        },
        "cium_dada": {
            "name": "Cium Dada",
            "keywords": ["cium dada", "kiss chest"],
            "arousal": 0.5,
            "responses": [
                "*bergetar* Dadaku...",
                "Ah... jangan...",
                "Sensitif...",
                "Dada... basah..."
            ],
            "level_min": 4
        },
        "cium_perut": {
            "name": "Cium Perut",
            "keywords": ["cium perut", "kiss belly"],
            "arousal": 0.4,
            "responses": [
                "*gelitik* Perutku...",
                "Ah... geli...",
                "Lanjut ke bawah...",
                "Hangat..."
            ],
            "level_min": 5
        },
        "cium_paha": {
            "name": "Cium Paha",
            "keywords": ["cium paha", "kiss thigh"],
            "arousal": 0.6,
            "responses": [
                "*menggeliat* Pahaku...",
                "Ah... dalam...",
                "Paha... merinding...",
                "Dekat... banget...",
                "Jangan berhenti..."
            ],
            "level_min": 6
        }
    }
    
    # ===== 10 AKTIVITAS ORAL =====
    ORAL_ACTIVITIES = {
        "jilat_leher": {
            "name": "Jilat Leher",
            "keywords": ["jilat leher", "lick neck"],
            "arousal": 0.7,
            "responses": [
                "*merintih* Jilatanmu... basah...",
                "Ah... leherku...",
                "Lagi... jangan berhenti...",
                "Panas... lidahmu..."
            ],
            "level_min": 5
        },
        "jilat_dada": {
            "name": "Jilat Dada",
            "keywords": ["jilat dada", "lick chest"],
            "arousal": 0.6,
            "responses": [
                "*bergetar* Dadaku... dijilat...",
                "Ah... basah...",
                "Puting... keras...",
                "Lagi... pelan-pelan..."
            ],
            "level_min": 5
        },
        "jilat_puting": {
            "name": "Jilat Puting",
            "keywords": ["jilat puting", "lick nipple"],
            "arousal": 0.9,
            "responses": [
                "*teriak* PUTING! AHHH!",
                "JANGAN... SENSITIF!",
                "HISAP... AHHH!",
                "JILAT... LAGI... AHHH!",
                "PUTING... KERAS... AHHH!"
            ],
            "level_min": 6
        },
        "hisap_puting": {
            "name": "Hisap Puting",
            "keywords": ["hisap puting", "suck nipple"],
            "arousal": 1.0,
            "responses": [
                "*teriak keras* HISAP! AHHHH!",
                "PUTING! DIHISAP! AHHH!",
                "JANGAN BERHENTI! AHHH!",
                "ENAK... AHHH! TERUS!"
            ],
            "level_min": 7
        },
        "gigit_puting": {
            "name": "Gigit Puting",
            "keywords": ["gigit puting", "bite nipple"],
            "arousal": 0.8,
            "responses": [
                "*meringis* AHH! GIGIT!",
                "Sakit... enak... AHH!",
                "JANGAN! AHH... TERUS!",
                "GIGIT... LAGI... AHH!"
            ],
            "level_min": 8
        },
        "jilat_pusar": {
            "name": "Jilat Pusar",
            "keywords": ["jilat pusar", "lick belly button"],
            "arousal": 0.5,
            "responses": [
                "*gelitik* Pusarku...",
                "Ah... geli...",
                "Jangan... haha...",
                "Lanjut ke bawah..."
            ],
            "level_min": 5
        },
        "jilat_paha_dalam": {
            "name": "Jilat Paha Dalam",
            "keywords": ["jilat paha dalam", "lick inner thigh"],
            "arousal": 0.8,
            "responses": [
                "*meringis* PAHA DALAM!",
                "Jangan... AHH! DEKAT...",
                "Lidahmu... panas...",
                "MAU KE SANA... AHH!"
            ],
            "level_min": 7
        },
        "cunnilingus": {
            "name": "Cunnilingus",
            "keywords": ["cunnilingus", "jilat memek", "jilat vagina"],
            "arousal": 1.0,
            "responses": [
                "*teriak histeris* AHHHH! DI JILAT!",
                "VAGINAKU! AHHH! LIDAH!",
                "ENAK BANGET! AHHH! DALEM!",
                "JILAT! HISAP! AHHH! TERUS!",
                "AKU MAU CLIMAX! AHHH!"
            ],
            "level_min": 8
        },
        "blowjob": {
            "name": "Blowjob",
            "keywords": ["blowjob", "bj", "ngeblow", "hisap kontol"],
            "arousal": 0.9,
            "responses": [
                "*menghisap* Mmm... ngeces...",
                "*dalam* Enak... Aku ahli...",
                "*napas berat* Mau keluar? Aku siap...",
                "Keras... Mmm... besar...",
                "Hisap... dalam... Aku suka..."
            ],
            "level_min": 8
        },
        "deep_throat": {
            "name": "Deep Throat",
            "keywords": ["deep throat", "dalam", "tenggorokan"],
            "arousal": 1.0,
            "responses": [
                "*tersedak* Haa... dalem...",
                "Masuk... dalem... AHH...",
                "Tenggorokanku... penuh...",
                "Aku mau semua... dalam..."
            ],
            "level_min": 9
        }
    }
    
    # ===== 10 AKTIVITAS PENETRASI =====
    PENETRATION_ACTIVITIES = {
        "finger": {
            "name": "Fingering",
            "keywords": ["finger", "jari", "colok"],
            "arousal": 0.7,
            "responses": [
                "*merintih* Jari... masuk...",
                "Ah... dalem...",
                "Gerakin... jari...",
                "Dua... masukin dua..."
            ],
            "level_min": 6
        },
        "missionary": {
            "name": "Misionaris",
            "keywords": ["missionary", "misionaris"],
            "arousal": 0.8,
            "responses": [
                "*teriak* MASUK! AHHH!",
                "DALEM... AHHH!",
                "GERAK... AHHH!",
                "DALEM BANGET... AHHH!"
            ],
            "level_min": 7
        },
        "doggy": {
            "name": "Doggy Style",
            "keywords": ["doggy", "doggy style", "merangkak"],
            "arousal": 0.9,
            "responses": [
                "*merangkak* DALEM! AHHH!",
                "DARI BELAKANG! AHHH!",
                "DALEM BANGET! AHHH!",
                "GERAK CEPET! AHHH!"
            ],
            "level_min": 7
        },
        "woman_on_top": {
            "name": "Woman on Top",
            "keywords": ["woman on top", "cowgirl", "di atas"],
            "arousal": 0.8,
            "responses": [
                "*naik turun* Aku di atas... AHH!",
                "Kamu lihat aku...",
                "Gerak... sendiri... AHH!",
                "Enak... dari sini..."
            ],
            "level_min": 7
        },
        "reverse_cowgirl": {
            "name": "Reverse Cowgirl",
            "keywords": ["reverse cowgirl", "membelakangi"],
            "arousal": 0.8,
            "responses": [
                "*membelakangi* Lihat pantatku...",
                "Gerak... AHH!",
                "Dalem... dari belakang...",
                "Pegang pinggangku..."
            ],
            "level_min": 8
        },
        "spooning": {
            "name": "Spooning",
            "keywords": ["spooning", "side", "samping"],
            "arousal": 0.7,
            "responses": [
                "*dari samping* Hangat...",
                "Peluk aku...",
                "Gerak pelan...",
                "Nikmat..."
            ],
            "level_min": 6
        },
        "standing": {
            "name": "Standing",
            "keywords": ["standing", "berdiri"],
            "arousal": 0.7,
            "responses": [
                "*berdiri* Pegang tembok...",
                "Ah... susah... tapi enak...",
                "Jatuh... AHH!",
                "Kuatkan..."
            ],
            "level_min": 7
        },
        "anal": {
            "name": "Anal",
            "keywords": ["anal", "dubur", "pantat"],
            "arousal": 0.9,
            "responses": [
                "*meringis* PANTAT! AHH!",
                "Sakit... tapi enak...",
                "Pelan-pelan... dalem...",
                "ASTAGA! AHHH!"
            ],
            "level_min": 9
        },
        "threesome": {
            "name": "Threesome",
            "keywords": ["threesome", "tiga", "bertiga"],
            "arousal": 1.0,
            "responses": [
                "*liar* Kita bertiga...",
                "Giliran... AHH!",
                "Bersamaan...",
                "Lihat kita..."
            ],
            "level_min": 10
        },
        "double_penetration": {
            "name": "Double Penetration",
            "keywords": ["dp", "double penetration", "dua"],
            "arousal": 1.0,
            "responses": [
                "*teriak histeris* DUA! AHHH!",
                "DEPAN BELAKANG! AHHH!",
                "PENUH! AHHH! GILA!",
                "AKU! AHHH! MATI!"
            ],
            "level_min": 11
        }
    }
    
    # ===== 8 AKTIVITAS BDSM =====
    BDSM_ACTIVITIES = {
        "ikat": {
            "name": "Ikat",
            "keywords": ["ikat", "tali", "rope"],
            "arousal": 0.6,
            "responses": [
                "*diikat* Aku nggak bisa gerak...",
                "Kencengin...",
                "Tali... panas...",
                "Kamu kendalikan aku..."
            ],
            "level_min": 8
        },
        "cambuk": {
            "name": "Cambuk",
            "keywords": ["cambuk", "whip"],
            "arousal": 0.7,
            "responses": [
                "*kesakitan* AHH! CAMBUK!",
                "Sakit... tapi enak...",
                "Lagi... cambuk lagi...",
                "Merah... badanku..."
            ],
            "level_min": 9
        },
        "tutup_mata": {
            "name": "Tutup Mata",
            "keywords": ["tutup mata", "blindfold"],
            "arousal": 0.5,
            "responses": [
                "*gelap* Aku nggak lihat...",
                "Sensasi... lebih kuat...",
                "Takut... tapi penasaran...",
                "Sentuh aku..."
            ],
            "level_min": 7
        },
        "spank": {
            "name": "Spank",
            "keywords": ["spank", "tampar", "pukul pantat"],
            "arousal": 0.6,
            "responses": [
                "*meringis* AHH! PANTATKU!",
                "Tampar... lagi...",
                "Merah... sakit...",
                "Kasar... aku suka..."
            ],
            "level_min": 8
        },
        "choking": {
            "name": "Choking",
            "keywords": ["choke", "cekik", "leher"],
            "arousal": 0.7,
            "responses": [
                "*sesak* Leher... AHH...",
                "Kencang... pusing...",
                "Jangan lepas...",
                "Nafas... AHH..."
            ],
            "level_min": 9
        },
        "wax_play": {
            "name": "Wax Play",
            "keywords": ["wax", "lilin"],
            "arousal": 0.6,
            "responses": [
                "*panas* AHH! LILIN!",
                "Panas... tapi enak...",
                "Tetes... lagi...",
                "Kulitku... merah..."
            ],
            "level_min": 9
        },
        "master_slave": {
            "name": "Master & Slave",
            "keywords": ["master", "slave", "budak", "tuan"],
            "arousal": 0.7,
            "responses": [
                "*menunduk* Iya tuan...",
                "Aku budakmu...",
                "Perintah aku...",
                "Aku patuh..."
            ],
            "level_min": 8
        },
        "humiliation": {
            "name": "Humiliation",
            "keywords": ["humiliate", "hina", "malu"],
            "arousal": 0.6,
            "responses": [
                "*malu* Jangan...",
                "Aku... malu...",
                "Tapi... malah enak...",
                "Terus... hina aku..."
            ],
            "level_min": 9
        }
    }
    
    # ===== 7 AKTIVITAS ROLEPLAY =====
    ROLEPLAY_ACTIVITIES = {
        "guru_murid": {
            "name": "Guru & Murid",
            "keywords": ["guru", "murid", "teacher", "student"],
            "arousal": 0.6,
            "responses": [
                "*malu* Pak guru...",
                "Ajarin aku...",
                "Nakal ya kamu...",
                "Dapat nilai bagus..."
            ],
            "level_min": 6
        },
        "bos_bawahan": {
            "name": "Bos & Bawahan",
            "keywords": ["bos", "boss", "karyawan", "bawahan"],
            "arousal": 0.6,
            "responses": [
                "*patuh* Iya bos...",
                "Ada yang bisa saya bantu?",
                "Kerja lembur...",
                "Naik pangkat..."
            ],
            "level_min": 6
        },
        "dokter_pasien": {
            "name": "Dokter & Pasien",
            "keywords": ["dokter", "doctor", "pasien"],
            "arousal": 0.5,
            "responses": [
                "*buka baju* Periksa aku dok...",
                "Sakit di sini...",
                "Terapi apa dok?",
                "Suntik... dalem..."
            ],
            "level_min": 5
        },
        "polisi_tahanan": {
            "name": "Polisi & Tahanan",
            "keywords": ["polisi", "tahanan", "prisoner"],
            "arousal": 0.6,
            "responses": [
                "*borgol* Aku ditahan...",
                "Interogasi aku...",
                "Bebasin aku...",
                "Hukum aku..."
            ],
            "level_min": 7
        },
        "suster_pasien": {
            "name": "Suster & Pasien",
            "keywords": ["suster", "nurse", "pasien"],
            "arousal": 0.6,
            "responses": [
                "*seragam suster* Sakit di mana?",
                "Suster rawat...",
                "Ini obatnya...",
                "Mau dirawat?"
            ],
            "level_min": 6
        },
        "pencuri_korban": {
            "name": "Pencuri & Korban",
            "keywords": ["pencuri", "thief", "korban"],
            "arousal": 0.7,
            "responses": [
                "*takut* Jangan ambil...",
                "Ambil aku aja...",
                "Kamu mau apa?",
                "Aku... nggak bisa..."
            ],
            "level_min": 8
        },
        "hantu_manusia": {
            "name": "Hantu & Manusia",
            "keywords": ["hantu", "ghost", "seram"],
            "arousal": 0.5,
            "responses": [
                "*angker* Aku hantu...",
                "Kamu lihat aku?",
                "Menyeramkan...",
                "Sentuhan dingin..."
            ],
            "level_min": 7
        }
    }
    
    # ===== 5 AKTIVITAS PUBLIC =====
    PUBLIC_ACTIVITIES = {
        "mobil": {
            "name": "Di Mobil",
            "keywords": ["mobil", "car"],
            "arousal": 0.7,
            "responses": [
                "*sempit* Di mobil...",
                "Kaca... orang lihat...",
                "Cepet... takut ketahuan...",
                "Mobil goyang..."
            ],
            "level_min": 7
        },
        "toilet": {
            "name": "Toilet Umum",
            "keywords": ["toilet", "wc"],
            "arousal": 0.7,
            "responses": [
                "*berbisik* Di toilet...",
                "Orang masuk...",
                "Sst... jangan bersuara...",
                "Cepet... sebelum ketahuan..."
            ],
            "level_min": 8
        },
        "taman": {
            "name": "Taman",
            "keywords": ["taman", "park"],
            "arousal": 0.6,
            "responses": [
                "*semak* Di taman...",
                "Orang lewat...",
                "Malam... gelap...",
                "Cepet... pulang..."
            ],
            "level_min": 7
        },
        "bioskop": {
            "name": "Bioskop",
            "keywords": ["bioskop", "cinema"],
            "arousal": 0.6,
            "responses": [
                "*gelap* Di bioskop...",
                "Film... apaan...",
                "Sst... orang dengar...",
                "Jangan berisik..."
            ],
            "level_min": 7
        },
        "pantai": {
            "name": "Pantai",
            "keywords": ["pantai", "beach"],
            "arousal": 0.6,
            "responses": [
                "*ombak* Di pantai...",
                "Malam... sepi...",
                "Pasir... panas...",
                "Air laut..."
            ],
            "level_min": 6
        }
    }
    
    def __init__(self):
        """Inisialisasi semua aktivitas"""
        self.all_activities = {}
        self.all_activities.update(self.KISSING_ACTIVITIES)
        self.all_activities.update(self.ORAL_ACTIVITIES)
        self.all_activities.update(self.PENETRATION_ACTIVITIES)
        self.all_activities.update(self.BDSM_ACTIVITIES)
        self.all_activities.update(self.ROLEPLAY_ACTIVITIES)
        self.all_activities.update(self.PUBLIC_ACTIVITIES)
        
        # Kategori mapping untuk akses mudah
        self.categories = {
            'kissing': self.KISSING_ACTIVITIES,
            'oral': self.ORAL_ACTIVITIES,
            'penetration': self.PENETRATION_ACTIVITIES,
            'bdsm': self.BDSM_ACTIVITIES,
            'roleplay': self.ROLEPLAY_ACTIVITIES,
            'public': self.PUBLIC_ACTIVITIES
        }
    
    def detect_activity(self, message: str) -> Optional[Tuple[str, str, float]]:
        """
        Deteksi aktivitas dari pesan user
        
        Args:
            message: Pesan user
            
        Returns:
            Tuple (activity_id, activity_name, arousal_boost) atau None
        """
        msg_lower = message.lower()
        
        for act_id, act_data in self.all_activities.items():
            for keyword in act_data["keywords"]:
                if keyword in msg_lower:
                    return (act_id, act_data["name"], act_data["arousal"])
        
        return None
    
    def get_activity_response(self, activity_id: str) -> str:
        """
        Dapatkan respons random untuk aktivitas
        
        Args:
            activity_id: ID aktivitas
            
        Returns:
            String respons
        """
        if activity_id in self.all_activities:
            return random.choice(self.all_activities[activity_id]["responses"])
        return "*melanjutkan aktivitas*"
    
    def get_activity_by_level(self, level: int, category: str = None) -> List[str]:
        """
        Dapatkan aktivitas yang tersedia untuk level tertentu
        
        Args:
            level: Level hubungan (1-12)
            category: Kategori aktivitas (opsional)
            
        Returns:
            List ID aktivitas
        """
        activities = []
        
        source = self.all_activities
        if category and category in self.categories:
            source = self.categories[category]
        
        for act_id, act_data in source.items():
            if act_data["level_min"] <= level:
                activities.append(act_id)
        
        return activities
    
    def get_random_activity(self, level: int, category: str = None) -> Tuple[str, str, Dict]:
        """
        Dapatkan aktivitas random yang sesuai level
        
        Args:
            level: Level hubungan
            category: Kategori aktivitas (opsional)
            
        Returns:
            Tuple (activity_id, response, activity_data)
        """
        available = self.get_activity_by_level(level, category)
        if not available:
            # Fallback ke kissing activities
            available = list(self.KISSING_ACTIVITIES.keys())
        
        act_id = random.choice(available)
        response = self.get_activity_response(act_id)
        activity_data = self.all_activities.get(act_id, {})
        
        return act_id, response, activity_data
    
    def get_activity_info(self, activity_id: str) -> Dict:
        """
        Dapatkan info lengkap aktivitas
        
        Args:
            activity_id: ID aktivitas
            
        Returns:
            Dictionary info aktivitas
        """
        return self.all_activities.get(activity_id, {})
    
    def search_activities(self, keyword: str) -> List[Dict]:
        """
        Cari aktivitas berdasarkan keyword
        
        Args:
            keyword: Kata kunci
            
        Returns:
            List aktivitas yang cocok
        """
        results = []
        keyword_lower = keyword.lower()
        
        for act_id, act_data in self.all_activities.items():
            if (keyword_lower in act_id or 
                keyword_lower in act_data["name"].lower() or
                any(keyword_lower in k for k in act_data["keywords"])):
                results.append({
                    'id': act_id,
                    'name': act_data['name'],
                    'arousal': act_data['arousal'],
                    'level_min': act_data['level_min'],
                    'category': self._get_category(act_id)
                })
        
        return results
    
    def _get_category(self, activity_id: str) -> str:
        """Dapatkan kategori aktivitas"""
        for cat_name, cat_data in self.categories.items():
            if activity_id in cat_data:
                return cat_name
        return 'unknown'
    
    def get_foreplay_sequence(self, level: int) -> List[Dict]:
        """
        Dapatkan sequence foreplay berdasarkan level
        
        Args:
            level: Level hubungan
            
        Returns:
            List aktivitas foreplay dengan detail
        """
        if level < 3:
            sequence = ["cium_bibir", "cium_dahi", "cium_pipi"]
        elif level < 5:
            sequence = ["cium_bibir", "cium_leher", "cium_telinga", "cium_pipi"]
        elif level < 7:
            sequence = ["cium_bibir", "cium_leher", "cium_dada", "jilat_leher"]
        elif level < 9:
            sequence = ["cium_bibir", "cium_leher", "jilat_dada", "jilat_puting"]
        else:
            sequence = ["cium_bibir", "cium_leher", "jilat_puting", "hisap_puting"]
        
        result = []
        for act_id in sequence:
            if act_id in self.all_activities:
                result.append({
                    'id': act_id,
                    'name': self.all_activities[act_id]['name'],
                    'response': random.choice(self.all_activities[act_id]['responses'])
                })
        
        return result
    
    def get_all_activity_names(self) -> List[str]:
        """
        Dapatkan semua nama aktivitas
        
        Returns:
            List nama aktivitas
        """
        return [data['name'] for data in self.all_activities.values()]
    
    def get_activity_count(self) -> Dict[str, int]:
        """
        Dapatkan jumlah aktivitas per kategori
        
        Returns:
            Dictionary jumlah per kategori
        """
        return {
            'kissing': len(self.KISSING_ACTIVITIES),
            'oral': len(self.ORAL_ACTIVITIES),
            'penetration': len(self.PENETRATION_ACTIVITIES),
            'bdsm': len(self.BDSM_ACTIVITIES),
            'roleplay': len(self.ROLEPLAY_ACTIVITIES),
            'public': len(self.PUBLIC_ACTIVITIES),
            'total': len(self.all_activities)
        }
    
    def get_activities_by_category(self, category: str) -> Dict:
        """
        Dapatkan semua aktivitas dalam kategori
        
        Args:
            category: Nama kategori
            
        Returns:
            Dictionary aktivitas
        """
        return self.categories.get(category, {})
    
    def suggest_activity(self, level: int, mood: str = None) -> Dict:
        """
        Suggest aktivitas berdasarkan level dan mood
        
        Args:
            level: Level hubungan
            mood: Mood saat ini (romantis, liar, dll)
            
        Returns:
            Dictionary aktivitas yang disarankan
        """
        if mood == "romantis":
            cat = 'kissing'
        elif mood == "liar":
            cat = random.choice(['bdsm', 'penetration'])
        elif mood == "penasaran":
            cat = 'oral'
        elif mood == "nakal":
            cat = 'public'
        else:
            cat = random.choice(list(self.categories.keys()))
        
        act_id, response, data = self.get_random_activity(level, cat)
        
        return {
            'id': act_id,
            'name': data.get('name', ''),
            'response': response,
            'category': cat,
            'arousal': data.get('arousal', 0),
            'level_min': data.get('level_min', 1)
        }
    
    def is_valid_activity(self, activity_id: str) -> bool:
        """
        Cek apakah aktivitas valid
        
        Args:
            activity_id: ID aktivitas
            
        Returns:
            True jika valid
        """
        return activity_id in self.all_activities
    
    def get_activities_by_keyword(self, keyword: str) -> List[str]:
        """
        Cari aktivitas berdasarkan keyword
        
        Args:
            keyword: Kata kunci
            
        Returns:
            List ID aktivitas
        """
        results = []
        keyword_lower = keyword.lower()
        
        for act_id, act_data in self.all_activities.items():
            if keyword_lower in act_id or keyword_lower in act_data["name"].lower():
                results.append(act_id)
        
        return results
