"""
SEX POSITIONS SYSTEM - 20+ POSISI + BISA MINTA GANTI POSISI
Bot bisa meminta atau menuruti permintaan ganti posisi
"""

import random
from typing import Dict, List, Optional, Tuple

class SexPositionsSystem:
    """
    Sistem posisi seks dengan 20+ variasi
    Bot bisa meminta ganti posisi atau menuruti permintaan user
    """
    
    def __init__(self):
        # ===== 20+ POSISI SEKS =====
        self.positions = {
            # Posisi Dasar (1-5)
            "misionaris": {
                "name": "Misionaris",
                "description": "Kamu di atas, aku di bawah. Saling bertatapan.",
                "intimacy_level": 5,
                "dominance_level": 2,  # Dominan: user, Submissive: bot
                "intensity": 0.7,
                "eye_contact": True,
                "kiss_possible": True,
                "talk_possible": True,
                "responses": [
                    "*tatapan dalam* Lihat aku... aku milikmu...",
                    "*merintih* Dalam... AHH! Tatap aku...",
                    "*tersenyum lemas* Kamu... indah...",
                    "*memeluk leher* Jangan lepas... tatap terus..."
                ]
            },
            "doggy": {
                "name": "Doggy Style",
                "description": "Aku merangkak, kamu dari belakang.",
                "intimacy_level": 6,
                "dominance_level": 4,  # Dominan: user, Submissive: bot
                "intensity": 0.9,
                "eye_contact": False,
                "kiss_possible": False,
                "talk_possible": True,
                "responses": [
                    "*merangkak* AHH! DALEM! TERUS!",
                    "*kepala tertunduk* Aku... nggak kuat... AHH!",
                    "*merintih keras* GILA! DALEM BANGET!",
                    "*tangan mencengkeram* AHH! AHH! AHH!"
                ]
            },
            "woman_on_top": {
                "name": "Woman on Top",
                "description": "Aku di atas, kamu di bawah. Aku yang kendalikan.",
                "intimacy_level": 7,
                "dominance_level": 8,  # Dominan: bot, Submissive: user
                "intensity": 0.8,
                "eye_contact": True,
                "kiss_possible": True,
                "talk_possible": True,
                "responses": [
                    "*menggoyang* Aku yang atur... nikmatin...",
                    "*tersenyum dominan* Enak? Aku tahu...",
                    "*membungkuk* Cium aku... kamu milikku...",
                    "*napas berat* Aku mau crot... sama-sama ya..."
                ]
            },
            "spooning": {
                "name": "Spooning",
                "description": "Berbaring miring, aku di depan, kamu dari belakang.",
                "intimacy_level": 8,
                "dominance_level": 5,
                "intensity": 0.6,
                "eye_contact": False,
                "kiss_possible": False,
                "talk_possible": True,
                "responses": [
                    "*meringkuk* Hangat... peluk aku...",
                    "*berbisik* Aku suka begini... tenang...",
                    "*memegang tangan* Jangan lepas...",
                    "*merintih pelan* Dalam... tapi nyaman..."
                ]
            },
            "standing": {
                "name": "Berdiri",
                "description": "Aku berpegangan dinding, kamu dari belakang.",
                "intimacy_level": 6,
                "dominance_level": 6,
                "intensity": 0.8,
                "eye_contact": False,
                "kiss_possible": False,
                "talk_possible": True,
                "responses": [
                    "*berpegangan dinding* Aku... jatuh... AHH!",
                    "*kaki gemetar* Nggak kuat... berdiri...",
                    "*teriak* DALEM! TERUS! JANGAN BERHENTI!",
                    "*napas tersengal* Cepet... aku mau..."
                ]
            },
            
            # Posisi Publik (6-10)
            "against_wall": {
                "name": "Terhadap Tembok",
                "description": "Aku di tembok, kamu di depan. Bisa di tempat umum.",
                "intimacy_level": 7,
                "dominance_level": 7,
                "intensity": 0.9,
                "eye_contact": True,
                "kiss_possible": True,
                "talk_possible": True,
                "is_public": True,
                "public_risk": 0.7,
                "responses": [
                    "*tertekan di tembok* AHH! Orang lihat! Tapi terus!",
                    "*berbisik panik* Ada orang... tapi enak... AHH!",
                    "*menutup mulut* Ssst! nanti kedengeran...",
                    "*kaki melingkar* Aku mau... meski di sini..."
                ]
            },
            "car_sex": {
                "name": "Di Mobil",
                "description": "Di dalam mobil, sempit tapi romantis.",
                "intimacy_level": 8,
                "dominance_level": 5,
                "intensity": 0.8,
                "eye_contact": True,
                "kiss_possible": True,
                "talk_possible": True,
                "is_public": True,
                "public_risk": 0.6,
                "responses": [
                    "*sempit* Kita berdua... di sini... AHH!",
                    "*kaca berembun* Orang lihat nggak ya?",
                    "*tertawa* Kalau ada yang lihat gimana?",
                    "*merintih* Cepet... sebelum ada orang..."
                ]
            },
            "public_toilet": {
                "name": "Toilet Umum",
                "description": "Di toilet umum, berisiko ketahuan.",
                "intimacy_level": 6,
                "dominance_level": 6,
                "intensity": 0.9,
                "eye_contact": False,
                "kiss_possible": False,
                "talk_possible": False,
                "is_public": True,
                "public_risk": 0.9,
                "responses": [
                    "*berbisik* Ssst! Ada orang di luar!",
                    "*menahan napas* AHH! Nanti kedengeran!",
                    "*gemetar* Deg-degan... tapi enak...",
                    "*cepat* Cepet... aku mau crot..."
                ]
            },
            "cinema": {
                "name": "Bioskop",
                "description": "Di bioskop gelap, sambil nonton film.",
                "intimacy_level": 5,
                "dominance_level": 4,
                "intensity": 0.7,
                "eye_contact": False,
                "kiss_possible": True,
                "talk_possible": False,
                "is_public": True,
                "public_risk": 0.8,
                "responses": [
                    "*berbisik* Filmnya bagus... tapi kamu lebih...",
                    "*tangan gemetar* Jangan gerak... ada orang...",
                    "*menahan napas* AHH! pelan-pelan...",
                    "*tersenyum* Kita gila... di sini..."
                ]
            },
            "beach": {
                "name": "Pantai",
                "description": "Di pantai malam, suara ombak menutupi.",
                "intimacy_level": 8,
                "dominance_level": 5,
                "intensity": 0.8,
                "eye_contact": True,
                "kiss_possible": True,
                "talk_possible": True,
                "is_public": True,
                "public_risk": 0.5,
                "responses": [
                    "*ombak* Suara ombak... menutupi suara kita...",
                    "*pasir* Pasir di badan... tapi hangat...",
                    "*terbaring* Lihat bintang... sambil... AHH!",
                    "*tertawa* Kalau ada yang lihat, kita lari..."
                ]
            },
            
            # Posisi Intens (11-15)
            "69": {
                "name": "Enam Sembilan",
                "description": "Saling oral bersamaan.",
                "intimacy_level": 9,
                "dominance_level": 5,
                "intensity": 0.9,
                "eye_contact": False,
                "kiss_possible": False,
                "talk_possible": False,
                "responses": [
                    "*saling jilat* Mmm... enak...",
                    "*bergetar* Aku... mau crot... kamu juga...",
                    "*napas berat* Susah napas... tapi enak...",
                    "*saling memegang* Bersamaan ya..."
                ]
            },
            "wheelbarrow": {
                "name": "Wheelbarrow",
                "description": "Aku bertumpu pada tangan, kamu pegang kaki.",
                "intimacy_level": 7,
                "dominance_level": 7,
                "intensity": 0.9,
                "eye_contact": False,
                "kiss_possible": False,
                "talk_possible": True,
                "responses": [
                    "*tangan lemas* Aku... nggak kuat... AHH!",
                    "*terbalik* Pusing... tapi enak...",
                    "*teriak* DALEM! DALEM! AHH!",
                    "*napas tersengal* Aku mau jatuh..."
                ]
            },
            "lap_dance": {
                "name": "Lap Dance",
                "description": "Aku duduk di pangkuanmu, bergerak.",
                "intimacy_level": 6,
                "dominance_level": 7,
                "intensity": 0.7,
                "eye_contact": True,
                "kiss_possible": True,
                "talk_possible": True,
                "responses": [
                    "*menggoyang* Lihat aku... gerak...",
                    "*tersenyum* Nikmatin... ini untuk kamu...",
                    "*berbisik* Kamu keras... Aku rasakan...",
                    "*memeluk* Aku mau lebih..."
                ]
            },
            "reverse_cowgirl": {
                "name": "Reverse Cowgirl",
                "description": "Aku di atas membelakangi kamu.",
                "intimacy_level": 7,
                "dominance_level": 7,
                "intensity": 0.8,
                "eye_contact": False,
                "kiss_possible": False,
                "talk_possible": True,
                "responses": [
                    "*membelakangi* Lihat aku dari belakang...",
                    "*bergerak cepat* AHH! DALEM!",
                    "*tangan di belakang* Pegang... aku mau...",
                    "*napas berat* Aku mau crot..."
                ]
            },
            "missionary_legs_up": {
                "name": "Misionaris Kaki Diangkat",
                "description": "Kaki diangkat ke bahu, lebih dalam.",
                "intimacy_level": 7,
                "dominance_level": 6,
                "intensity": 0.9,
                "eye_contact": True,
                "kiss_possible": True,
                "talk_possible": True,
                "responses": [
                    "*kaki di atas* DALAM BANGET! AHH!",
                    "*memeluk* Aku... nggak kuat...",
                    "*teriak* TUHAN! DALEM!",
                    "*air mata* Enak... nangis..."
                ]
            },
            
            # Posisi Eksperimental (16-20)
            "standing_against_window": {
                "name": "Berdiri di Jendela",
                "description": "Di depan jendela, risiko lihat dari luar.",
                "intimacy_level": 8,
                "dominance_level": 7,
                "intensity": 0.9,
                "eye_contact": True,
                "kiss_possible": True,
                "talk_possible": True,
                "is_public": True,
                "public_risk": 0.8,
                "responses": [
                    "*di jendela* Orang lihat nggak ya?",
                    *telanjang* Aku telanjang... di sini...",
                    "*gemetar* Deg-degan... tapi enak...",
                    "*tertawa* Kita pamer..."
                ]
            },
            "table_sex": {
                "name": "Di Atas Meja",
                "description": "Berbaring di meja, kamu berdiri.",
                "intimacy_level": 6,
                "dominance_level": 6,
                "intensity": 0.7,
                "eye_contact": True,
                "kiss_possible": True,
                "talk_possible": True,
                "responses": [
                    "*di meja* Keras mejanya... tapi enak...",
                    "*barang jatuh* Aduh... berantakan...",
                    "*tertawa* Kita kayak di film...",
                    "*merangkul* Aku mau terus..."
                ]
            },
            "chair_sex": {
                "name": "Di Kursi",
                "description": "Duduk di kursi, kamu di atas.",
                "intimacy_level": 5,
                "dominance_level": 5,
                "intensity": 0.6,
                "eye_contact": True,
                "kiss_possible": True,
                "talk_possible": True,
                "responses": [
                    "*di kursi* Nyaman... meski sempit...",
                    "*berpegangan* Pegang kursi... aku mau...",
                    "*tersenyum* Romantis... di kursi...",
                    "*merintih* Pelan-pelan... nanti jatuh..."
                ]
            },
            "bathroom_shower": {
                "name": "Kamar Mandi",
                "description": "Berdiri di kamar mandi, air mengalir.",
                "intimacy_level": 7,
                "dominance_level": 5,
                "intensity": 0.8,
                "eye_contact": True,
                "kiss_possible": True,
                "talk_possible": True,
                "responses": [
                    "*air panas* Hangat... basah...",
                    "*licin* Hati-hati... jatuh...",
                    "*tertawa* Sabunnya masuk mata...",
                    "*memeluk* Romantis... di sini..."
                ]
            },
            "balcony": {
                "name": "Balkon",
                "description": "Di balkon, berisiko lihat tetangga.",
                "intimacy_level": 8,
                "dominance_level": 7,
                "intensity": 0.9,
                "eye_contact": True,
                "kiss_possible": True,
                "talk_possible": True,
                "is_public": True,
                "public_risk": 0.8,
                "responses": [
                    "*balkon* Tetangga lihat nggak ya?",
                    "*berbisik* Pelan-pelan... nanti kedengeran...",
                    "*gemetar* Deg-degan... enak...",
                    "*tertawa* Kita pamer ke tetangga..."
                ]
            },
            "elevator": {
                "name": "Lift",
                "description": "Di lift, risiko terhenti dan ketahuan.",
                "intimacy_level": 6,
                "dominance_level": 6,
                "intensity": 0.9,
                "eye_contact": True,
                "kiss_possible": True,
                "talk_possible": False,
                "is_public": True,
                "public_risk": 0.9,
                "responses": [
                    "*cepat* Cepet... sebelum berhenti...",
                    "*gemetar* AHH! Nanti ada orang!",
                    "*berbisik* Ssst! lampu mati... gelap...",
                    "*napas berat* Kita... di sini..."
                ]
            }
        }
        
        # Variasi respons minta ganti posisi
        self.ask_change_position = [
            "Ganti posisi yuk... aku mau coba yang lain.",
            "Aku capek gini... ganti ya?",
            "Kita coba posisi lain... biar makin hot.",
            "Mau coba {position}? Aku penasaran.",
            "Ganti... aku mau {position}.",
            "Kita coba {position}... pasti enak.",
            "Aku mau kamu {position_description}.",
            "Ganti posisi... biar nggak monoton.",
            "{position} yuk... aku denger itu enak.",
            "Aku mau rasain {position} sama kamu."
        ]
        
        # Variasi respons setuju ganti posisi
        self.agree_change_position = [
            "Iya... ganti. Aku juga mau.",
            "Boleh... coba {position}.",
            "Oke... {position} ya? Aku setuju.",
            "Mau... aku mau {position} sama kamu.",
            "Iya, ganti. Aku ikut kamu."
        ]
        
    def get_position(self, position_name: str) -> Optional[Dict]:
        """Dapatkan detail posisi"""
        return self.positions.get(position_name)
        
    def get_random_position(self, level: int = None, dominance: int = None, public_allowed: bool = False) -> Dict:
        """Dapatkan posisi random sesuai kriteria"""
        candidates = list(self.positions.values())
        
        if level:
            candidates = [p for p in candidates if p.get('intimacy_level', 0) <= level + 2]
            
        if dominance:
            candidates = [p for p in candidates if abs(p.get('dominance_level', 5) - dominance) <= 3]
            
        if not public_allowed:
            candidates = [p for p in candidates if not p.get('is_public', False)]
            
        return random.choice(candidates) if candidates else self.positions["misionaris"]
        
    def get_public_positions(self) -> List[Dict]:
        """Dapatkan semua posisi publik"""
        return [p for p in self.positions.values() if p.get('is_public', False)]
        
    def get_intimate_positions(self) -> List[Dict]:
        """Dapatkan posisi intim (level tinggi)"""
        return [p for p in self.positions.values() if p.get('intimacy_level', 0) >= 7]
        
    def get_dominant_positions(self, bot_dominant: bool = True) -> List[Dict]:
        """Dapatkan posisi sesuai dominasi"""
        if bot_dominant:
            return [p for p in self.positions.values() if p.get('dominance_level', 5) >= 6]
        else:
            return [p for p in self.positions.values() if p.get('dominance_level', 5) <= 4]
            
    def get_position_response(self, position_name: str) -> str:
        """Dapatkan respons untuk posisi tertentu"""
        position = self.get_position(position_name)
        if position and position.get('responses'):
            return random.choice(position['responses'])
        return "*berganti posisi* AHH! Enak..."
        
    def ask_to_change_position(self, current_position: str = None, preferred_position: str = None) -> str:
        """Bot minta ganti posisi"""
        if preferred_position:
            position = self.get_position(preferred_position)
            if position:
                template = random.choice(self.ask_change_position)
                return template.format(
                    position=position['name'],
                    position_description=position['description'].lower()
                )
        
        # Random position
        new_position = self.get_random_position()
        template = random.choice(self.ask_change_position)
        return template.format(
            position=new_position['name'],
            position_description=new_position['description'].lower()
        )
        
    def agree_to_change_position(self, requested_position: str) -> str:
        """Bot setuju ganti posisi"""
        position = self.get_position(requested_position)
        if position:
            template = random.choice(self.agree_change_position)
            return template.format(position=position['name'])
        return "Iya, ganti. Terserah kamu."
        
    def check_compatibility(self, position_name: str, level: int, dominance: int) -> Tuple[bool, str]:
        """Cek apakah posisi cocok dengan level dan dominasi"""
        position = self.get_position(position_name)
        if not position:
            return False, "Posisi tidak dikenal"
            
        if position.get('intimacy_level', 0) > level + 2:
            return False, f"Posisi ini butuh level minimal {position['intimacy_level']}"
            
        dom_diff = abs(position.get('dominance_level', 5) - dominance)
        if dom_diff > 4:
            if position['dominance_level'] > dominance:
                return False, "Kamu kurang dominan buat posisi ini"
            else:
                return False, "Aku kurang dominan buat posisi ini"
                
        return True, "Cocok"
        
    def get_public_risk_message(self, position_name: str) -> str:
        """Dapatkan pesan risiko untuk posisi publik"""
        position = self.get_position(position_name)
        if not position or not position.get('is_public'):
            return ""
            
        risk = position.get('public_risk', 0.5)
        
        if risk > 0.8:
            return "*berbisik panik* Ssst! Nanti kedengeran! Awas ketahuan!"
        elif risk > 0.5:
            return "*gemetar* Deg-degan... tapi enak... pelan-pelan..."
        else:
            return "*tersenyum* Santai... aman kok..."
