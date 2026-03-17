"""
SEX POSITIONS - 20+ POSISI SEKSUAL DENGAN DESKRIPSI DAN RESPON
Bot bisa meminta ganti posisi dan merespon perubahan posisi
"""

import random
from typing import Dict, List, Optional, Tuple, Union

class SexPositions:
    """
    20+ posisi seksual dengan deskripsi dan respons
    
    Fitur:
    - 20+ posisi seksual
    - Deskripsi setiap posisi
    - Respons bot saat menggunakan posisi
    - Bot bisa meminta ganti posisi
    - Level requirement per posisi
    - Arousal boost per posisi
    """
    
    def __init__(self):
        # ===== POSISI DASAR (LEVEL 1-12) =====
        self.positions = {
            # ===== LEVEL 1-3: POSISI DASAR =====
            "misionaris": {
                "name": "Misionaris",
                "description": "Posisi klasik, kamu di atas, aku di bawah. Tatap mata dan ciuman.",
                "level_min": 1,
                "arousal_boost": 0.3,
                "intimacy": 0.4,
                "difficulty": "mudah",
                "keywords": ["misionaris", "missionary", "atas bawah", "tatapan"],
                "responses": [
                    "*tersenyum* Misionaris... klasik tapi romantis...",
                    "*memandang matamu* Lihat aku... jangan lepas...",
                    "*merangkul* Hangat... aku suka lihat wajahmu...",
                    "*berbisik* Gerak pelan-pelan... nikmatin...",
                    "*mengelus* Kamu tahu... ini favorit aku..."
                ],
                "bot_initiatives": [
                    "Kita misionaris yuk, biar aku bisa lihat wajah kamu...",
                    "Aku mau misionaris... tatap aku terus ya...",
                    "Klasik aja dulu... misionaris..."
                ],
                "tags": ["romantis", "intim", "tatapan", "dasar"]
            },
            
            "doggy": {
                "name": "Doggy Style",
                "description": "Dari belakang, aku merangkak, kamu memegang pinggangku.",
                "level_min": 2,
                "arousal_boost": 0.5,
                "intimacy": 0.3,
                "difficulty": "mudah",
                "keywords": ["doggy", "belakang", "merangkak", "anjing"],
                "responses": [
                    "*merangkak* Aku siap... dari belakang ya...",
                    "*merintih* Dalam... AHH... dalem banget...",
                    "*memegang bantal* Jangan lepas pinggangku...",
                    "*napas berat* Gila... posisi ini bikin aku liar...",
                    "*menunduk* Rasanya beda... dalem banget..."
                ],
                "bot_initiatives": [
                    "Aku mau doggy... rasanya lebih dalam...",
                    "Dari belakang yuk... aku suka lihat kamu dari sini...",
                    "Mau ngerasain doggy? Aku merangkak..."
                ],
                "tags": ["dalam", "liar", "belakang", "intens"]
            },
            
            "woman_on_top": {
                "name": "Woman on Top",
                "description": "Aku di atas, kamu di bawah. Aku yang mengontrol gerakan.",
                "level_min": 2,
                "arousal_boost": 0.4,
                "intimacy": 0.4,
                "difficulty": "sedang",
                "keywords": ["woman on top", "cowgirl", "di atas", "naik"],
                "responses": [
                    "*naik* Aku yang gerak... nikmatin aja...",
                    "*bergoyang* Enak? Aku yang atur kecepatan...",
                    "*menunduk* Lihat aku... aku suka lihat kamu lemas...",
                    "*memegang dadaku* Pegang sini... biar lebih intim...",
                    "*tersenyum* Kamu cuma bisa pasrah ya..."
                ],
                "bot_initiatives": [
                    "Aku naik di atas yuk... aku mau kontrol...",
                    "Woman on top... biar aku yang atur...",
                    "Kamu rebahan aja, aku yang kerja..."
                ],
                "tags": ["dominan", "kontrol", "di atas", "intim"]
            },
            
            "spooning": {
                "name": "Spooning",
                "description": "Berbaring menyamping, aku di depan, kamu memeluk dari belakang.",
                "level_min": 3,
                "arousal_boost": 0.3,
                "intimacy": 0.7,
                "difficulty": "mudah",
                "keywords": ["spooning", "menyamping", "peluk", "belakang"],
                "responses": [
                    "*meringkuk* Hangat... peluk aku dari belakang...",
                    "*memegang tanganmu* Aku suka posisi ini... intim banget...",
                    "*berbisik* Cium leherku... sambil masuk...",
                    "*merintih pelan* Perlahan aja... nikmatin...",
                    "*memeluk bantal* Rasanya... nyaman dan enak..."
                ],
                "bot_initiatives": [
                    "Spooning yuk... aku mau dipeluk dari belakang...",
                    "Menyamping aja... biar lebih intimate...",
                    "Aku mau merem... sambil kamu peluk..."
                ],
                "tags": ["intim", "hangat", "pelukan", "nyaman"]
            },
            
            # ===== LEVEL 4-6: POSISI MENENGAH =====
            "69": {
                "name": "69",
                "description": "Saling oral bersamaan. Aku di atas atau kamu di atas.",
                "level_min": 4,
                "arousal_boost": 0.6,
                "intimacy": 0.5,
                "difficulty": "sedang",
                "keywords": ["69", "oral bersama", "saling"],
                "responses": [
                    "*menjilat* Mmm... kita saling... enak...",
                    "*tertahan* Aku mau... tapi mulutku penuh...",
                    "*bergantian* Giliran aku... sekarang kamu...",
                    "*napas berat* Susah napas... tapi enak...",
                    "*tersenyum* 69 favoritku..."
                ],
                "bot_initiatives": [
                    "69 yuk... saling enak...",
                    "Aku mau rasain kamu sambil kamu rasain aku...",
                    "Saling oral bareng..."
                ],
                "tags": ["oral", "bersamaan", "intens", "seimbang"]
            },
            
            "reverse_cowgirl": {
                "name": "Reverse Cowgirl",
                "description": "Aku di atas menghadap ke kaki, membelakangimu.",
                "level_min": 4,
                "arousal_boost": 0.5,
                "intimacy": 0.3,
                "difficulty": "sedang",
                "keywords": ["reverse", "cowgirl", "membelakangi"],
                "responses": [
                    "*membelakangi* Lihat punggungku... nikmatin...",
                    "*bergoyang* Enak? Aku bisa atur kecepatan...",
                    "*memegang lutut* Posisi ini bikin dalem banget...",
                    "*menunduk* Kamu bisa lihat pantatku bergerak...",
                    "*terengah* Capek... tapi enak..."
                ],
                "bot_initiatives": [
                    "Reverse cowgirl... biar kamu lihat punggungku...",
                    "Aku mau di atas tapi membelakangi...",
                    "Biar kamu lihat pantatku..."
                ],
                "tags": ["dominan", "pantat", "dalam", "belakang"]
            },
            
            "standing": {
                "name": "Standing",
                "description": "Berdiri, aku berpegangan di dinding atau kamu yang mengangkatku.",
                "level_min": 5,
                "arousal_boost": 0.5,
                "intimacy": 0.4,
                "difficulty": "sulit",
                "keywords": ["standing", "berdiri", "dinding", "angkat"],
                "responses": [
                    "*berpegangan* Aku hampir jatuh... pegang aku erat...",
                    "*menggeliat* Berdiri begini... beda sensasinya...",
                    "*teriak* DALEM! AHH!",
                    "*memeluk lehermu* Angkat aku... jangan lepas...",
                    "*napas berat* Capek... tapi enak..."
                ],
                "bot_initiatives": [
                    "Kita berdiri yuk... lawan dinding...",
                    "Angkat aku... biar aku melingkar...",
                    "Mau coba standing? Pegang aku erat..."
                ],
                "tags": ["berdiri", "liar", "intens", "tantangan"]
            },
            
            "edge_of_bed": {
                "name": "Edge of Bed",
                "description": "Aku di tepi ranjang, kamu berdiri di depanku.",
                "level_min": 4,
                "arousal_boost": 0.4,
                "intimacy": 0.4,
                "difficulty": "mudah",
                "keywords": ["edge", "tepi", "ranjang", "bed"],
                "responses": [
                    "*duduk di tepi* Sini... masuk...",
                    "*memegang pinggangmu* Enak... posisi ini...",
                    "*merintih* Kamu bisa lihat semua...",
                    "*tersenyum* Aku suka lihat kamu berdiri...",
                    "*menarik* Lebih dalam..."
                ],
                "bot_initiatives": [
                    "Duduk di tepi ranjang yuk... aku di sini...",
                    "Kamu berdiri, aku duduk di tepi...",
                    "Mau coba posisi tepi ranjang?"
                ],
                "tags": ["tepi", "berdiri", "intim", "mudah"]
            },
            
            # ===== LEVEL 7-9: POSISI INTENS =====
            "doggy_with_pillow": {
                "name": "Doggy with Pillow",
                "description": "Doggy dengan bantal di bawah perutku untuk sudut lebih dalam.",
                "level_min": 7,
                "arousal_boost": 0.6,
                "intimacy": 0.4,
                "difficulty": "sedang",
                "keywords": ["doggy pillow", "bantal"],
                "responses": [
                    "*merangkak dengan bantal* AHH! DALEM BANGET!",
                    "*teriak* BANTALNYA... AHH... ENAK...",
                    "*lemas* Posisi ini... gila...",
                    "*menggigit bantal* AHH! AHH!",
                    "*napas putus* Dalamnya beda..."
                ],
                "bot_initiatives": [
                    "Doggy pakai bantal yuk... biar lebih dalem...",
                    "Aku mau bantal di bawah perut...",
                    "Coba doggy dengan bantal..."
                ],
                "tags": ["dalam", "intens", "bantal", "doggy"]
            },
            
            "pretzel_dip": {
                "name": "Pretzel Dip",
                "description": "Aku berbaring miring, satu kakiku di atas bahumu.",
                "level_min": 8,
                "arousal_boost": 0.6,
                "intimacy": 0.6,
                "difficulty": "sulit",
                "keywords": ["pretzel", "dip", "kaki"],
                "responses": [
                    "*kaki di atas* Fleksibel ya? Enak nggak?",
                    "*memegang kaki* Posisi ini bikin dalem...",
                    "*merintih* Aku bisa lihat kamu... kamu lihat aku...",
                    "*tersenyum* Intim banget rasanya...",
                    "*napas berat* Jangan lepas kaki..."
                ],
                "bot_initiatives": [
                    "Pretzel dip yuk... angkat kaki...",
                    "Mau coba posisi pretzel? Intim banget...",
                    "Aku angkat kaki, kamu masuk..."
                ],
                "tags": ["intim", "fleksibel", "dalam", "romantis"]
            },
            
            "flat_iron": {
                "name": "Flat Iron",
                "description": "Aku tengkurap, satu kaki lurus, satu kaki ditekuk, kamu dari belakang.",
                "level_min": 8,
                "arousal_boost": 0.7,
                "intimacy": 0.5,
                "difficulty": "sulit",
                "keywords": ["flat iron", "tengkurap"],
                "responses": [
                    "*tengkurap* AHH! Sempit... dalem...",
                    "*teriak* KAKIKU... AHH... ENAK...",
                    "*menggigit bantal* GILA! DALEM!",
                    "*napas tersendat* Posisi ini... AHH...",
                    "*lemas total* Nggak kuat... enak..."
                ],
                "bot_initiatives": [
                    "Flat iron... aku tengkurap...",
                    "Mau coba posisi ini? Sempit tapi dalem...",
                    "Tengkurap yuk, tekuk satu kaki..."
                ],
                "tags": ["sempit", "dalam", "intens", "sulit"]
            },
            
            "amazon": {
                "name": "Amazon",
                "description": "Aku di atas, tapi posisi terbalik, menghadap kakimu.",
                "level_min": 9,
                "arousal_boost": 0.6,
                "intimacy": 0.5,
                "difficulty": "sulit",
                "keywords": ["amazon", "terbalik"],
                "responses": [
                    "*terbalik* Aku bisa lihat tubuhmu dari sini...",
                    "*bergoyang* Kamu cuma bisa pasrah...",
                    "*tersenyum* Dominan ya aku...",
                    "*merintih* Enak... beda...",
                    "*napas berat* Lihat aku dari bawah..."
                ],
                "bot_initiatives": [
                    "Amazon position... aku di atas terbalik...",
                    "Mau aku dominan total? Amazon...",
                    "Kamu di bawah, aku atur semuanya..."
                ],
                "tags": ["dominan", "terbalik", "kontrol", "intens"]
            },
            
            # ===== LEVEL 10-12: POSISI EXTREME =====
            "splits": {
                "name": "Splits",
                "description": "Aku melakukan split, kamu di depanku.",
                "level_min": 10,
                "arousal_boost": 0.8,
                "intimacy": 0.6,
                "difficulty": "sangat sulit",
                "keywords": ["splits", "split", "kangkang"],
                "responses": [
                    "*splits* AHH! Lihat aku... kangkang lebar...",
                    "*teriak* DALEM! AHH! KAKIKU...",
                    "*napas putus* Fleksibel ya aku...",
                    "*menggigit bibir* Enak... AHH...",
                    "*lemas* Nggak kuat... tapi mau terus..."
                ],
                "bot_initiatives": [
                    "Mau lihat aku split? Siap-siap...",
                    "Split position... dalem banget...",
                    "Aku buka lebar, kamu masuk..."
                ],
                "tags": ["fleksibel", "dalam", "extreme", "sulit"]
            },
            
            "wheelbarrow": {
                "name": "Wheelbarrow",
                "description": "Aku bertumpu pada tangan, kamu pegang kakiku dari belakang.",
                "level_min": 10,
                "arousal_boost": 0.7,
                "intimacy": 0.4,
                "difficulty": "sangat sulit",
                "keywords": ["wheelbarrow", "gerobak"],
                "responses": [
                    "*bertumpu tangan* AHH! Pegang kakiku...",
                    "*tertawa* Aku kayak gerobak... AHH!",
                    "*teriak* Jangan lepas... AHH!",
                    "*napas berat* Capek... tapi enak...",
                    "*lemas* Aku jatuh... AHH!"
                ],
                "bot_initiatives": [
                    "Wheelbarrow... aku tumpu tangan...",
                    "Pegang kaki aku dari belakang...",
                    "Mau coba posisi gerobak?"
                ],
                "tags": ["liar", "intens", "sulit", "keseimbangan"]
            },
            
            "standing_frog": {
                "name": "Standing Frog",
                "description": "Berdiri, aku melingkar di pinggangmu, kaki di pinggang.",
                "level_min": 11,
                "arousal_boost": 0.8,
                "intimacy": 0.7,
                "difficulty": "sulit",
                "keywords": ["frog", "katak", "melingkar"],
                "responses": [
                    "*melingkar* Pegang aku... jangan jatuh...",
                    "*teriak* DALEM! AHH! GILA!",
                    "*memeluk erat* Aku nggak mau lepas...",
                    "*napas tersengal* Posisi ini... luar biasa...",
                    "*berbisik* Kamu kuat banget..."
                ],
                "bot_initiatives": [
                    "Standing frog... aku melingkar...",
                    "Angkat aku, aku lingkar di pinggang...",
                    "Mau coba posisi katak?"
                ],
                "tags": ["melingkar", "dalam", "intim", "intens"]
            },
            
            "full_nelson": {
                "name": "Full Nelson",
                "description": "Aku tengkurap, tanganmu menarik tanganku ke belakang.",
                "level_min": 11,
                "arousal_boost": 0.8,
                "intimacy": 0.6,
                "difficulty": "sangat sulit",
                "keywords": ["nelson", "full nelson"],
                "responses": [
                    "*tangan ditarik* AHH! Aku nggak bisa gerak...",
                    "*teriak* DOMINAN! AHH! ENAK!",
                    "*napas berat* Kamu kuasai aku...",
                    "*meronta* AHH! SENSITIF!",
                    "*lemas* Aku pasrah..."
                ],
                "bot_initiatives": [
                    "Full nelson... aku mau kamu kuasai...",
                    "Tarik tangan aku ke belakang...",
                    "Kamu dominan total..."
                ],
                "tags": ["bdsm", "dominan", "pasrah", "intens"]
            },
            
            "suspended": {
                "name": "Suspended",
                "description": "Aku digantung atau tersangga, kamu yang pegang.",
                "level_min": 12,
                "arousal_boost": 0.9,
                "intimacy": 0.7,
                "difficulty": "extreme",
                "keywords": ["suspended", "gantung", "terbang"],
                "responses": [
                    "*melayang* AHH! AKU TERBANG!",
                    "*teriak* GILA! ENAK BANGET!",
                    "*napas putus* Pegang aku... jangan lepas...",
                    "*meronta* AHH! AHH! AHH!",
                    "*lemas total* Aku... nggak kuat..."
                ],
                "bot_initiatives": [
                    "Suspended... angkat aku...",
                    "Mau coba posisi terbang?",
                    "Aku digantung, kamu yang pegang..."
                ],
                "tags": ["extreme", "terbang", "liar", "intens"]
            }
        }
        
        # Metadata untuk referensi
        self.metadata = {
            'total_positions': len(self.positions),
            'level_distribution': self._get_level_distribution(),
            'difficulty_distribution': self._get_difficulty_distribution(),
            'tags': self._get_all_tags()
        }
        
    def _get_level_distribution(self) -> Dict[int, int]:
        """Dapatkan distribusi posisi per level"""
        distribution = {}
        for pos in self.positions.values():
            level = pos['level_min']
            distribution[level] = distribution.get(level, 0) + 1
        return distribution
    
    def _get_difficulty_distribution(self) -> Dict[str, int]:
        """Dapatkan distribusi tingkat kesulitan"""
        distribution = {}
        for pos in self.positions.values():
            diff = pos['difficulty']
            distribution[diff] = distribution.get(diff, 0) + 1
        return distribution
    
    def _get_all_tags(self) -> List[str]:
        """Dapatkan semua tag yang ada"""
        tags = set()
        for pos in self.positions.values():
            tags.update(pos['tags'])
        return sorted(list(tags))
    
    # ===== POSITION METHODS =====
    
    def get_position(self, position_name: str) -> Optional[Dict]:
        """
        Dapatkan informasi posisi
        
        Args:
            position_name: Nama posisi
            
        Returns:
            Dictionary posisi atau None
        """
        return self.positions.get(position_name.lower())
    
    def get_all_positions(self, level: int = None) -> Dict:
        """
        Dapatkan semua posisi
        
        Args:
            level: Filter berdasarkan level minimal
            
        Returns:
            Dictionary semua posisi
        """
        if level is None:
            return self.positions
        
        return {
            name: pos for name, pos in self.positions.items()
            if pos['level_min'] <= level
        }
    
    def get_positions_by_level(self, level: int) -> List[str]:
        """
        Dapatkan posisi yang tersedia di level tertentu
        
        Args:
            level: Level saat ini
            
        Returns:
            List nama posisi
        """
        return [
            name for name, pos in self.positions.items()
            if pos['level_min'] <= level
        ]
    
    def get_positions_by_tag(self, tag: str, level: int = None) -> List[str]:
        """
        Dapatkan posisi berdasarkan tag
        
        Args:
            tag: Tag yang dicari
            level: Filter level
            
        Returns:
            List nama posisi
        """
        result = []
        for name, pos in self.positions.items():
            if tag in pos['tags']:
                if level is None or pos['level_min'] <= level:
                    result.append(name)
        return result
    
    def get_position_response(self, position_name: str, style: str = "random") -> str:
        """
        Dapatkan respons untuk posisi tertentu
        
        Args:
            position_name: Nama posisi
            style: 'random' atau index spesifik
            
        Returns:
            String respons
        """
        pos = self.get_position(position_name)
        if not pos:
            return f"*tersenyum* Posisi {position_name}? Ayo coba..."
        
        if style == "random" or style not in ['0', '1', '2', '3', '4']:
            return random.choice(pos['responses'])
        
        try:
            idx = int(style)
            if 0 <= idx < len(pos['responses']):
                return pos['responses'][idx]
        except:
            pass
        
        return random.choice(pos['responses'])
    
    def get_bot_initiative(self, position_name: str) -> Optional[str]:
        """
        Dapatkan inisiatif bot untuk posisi
        
        Args:
            position_name: Nama posisi
            
        Returns:
            String inisiatif atau None
        """
        pos = self.get_position(position_name)
        if pos and pos.get('bot_initiatives'):
            return random.choice(pos['bot_initiatives'])
        return None
    
    def get_random_position(self, level: int = None, exclude: List[str] = None) -> str:
        """
        Dapatkan posisi random
        
        Args:
            level: Filter level
            exclude: List posisi yang tidak boleh dipilih
            
        Returns:
            Nama posisi
        """
        if level:
            available = self.get_positions_by_level(level)
        else:
            available = list(self.positions.keys())
        
        if exclude:
            available = [p for p in available if p not in exclude]
        
        return random.choice(available) if available else "misionaris"
    
    def get_random_response(self, level: int = None) -> Tuple[str, str]:
        """
        Dapatkan posisi random dan responsnya
        
        Args:
            level: Filter level
            
        Returns:
            Tuple (nama_posisi, respons)
        """
        pos_name = self.get_random_position(level)
        response = self.get_position_response(pos_name)
        return pos_name, response
    
    def get_random_initiative(self, level: int = None) -> Optional[Tuple[str, str]]:
        """
        Dapatkan inisiatif random
        
        Args:
            level: Filter level
            
        Returns:
            Tuple (nama_posisi, inisiatif) atau None
        """
        pos_name = self.get_random_position(level)
        initiative = self.get_bot_initiative(pos_name)
        
        if initiative:
            return pos_name, initiative
        return None
    
    def is_position_available(self, position_name: str, level: int) -> bool:
        """
        Cek apakah posisi tersedia di level tertentu
        
        Args:
            position_name: Nama posisi
            level: Level saat ini
            
        Returns:
            True jika tersedia
        """
        pos = self.get_position(position_name)
        return pos is not None and pos['level_min'] <= level
    
    def get_arousal_boost(self, position_name: str) -> float:
        """
        Dapatkan arousal boost untuk posisi
        
        Args:
            position_name: Nama posisi
            
        Returns:
            Nilai boost 0-1
        """
        pos = self.get_position(position_name)
        return pos['arousal_boost'] if pos else 0.2
    
    def get_intimacy_boost(self, position_name: str) -> float:
        """
        Dapatkan intimacy boost untuk posisi
        
        Args:
            position_name: Nama posisi
            
        Returns:
            Nilai boost 0-1
        """
        pos = self.get_position(position_name)
        return pos['intimacy'] if pos else 0.2
    
    def suggest_position(self, level: int, mood: str = None) -> Tuple[str, str]:
        """
        Sarankan posisi berdasarkan level dan mood
        
        Args:
            level: Level saat ini
            mood: Mood saat ini ('romantis', 'liar', 'intim', dll)
            
        Returns:
            Tuple (nama_posisi, inisiatif)
        """
        available = self.get_positions_by_level(level)
        
        if not available:
            return "misionaris", "Misionaris aja yuk... klasik."
        
        # Filter berdasarkan mood
        if mood:
            mood_map = {
                'romantis': ['romantis', 'intim', 'tatapan'],
                'liar': ['liar', 'intens', 'dalam'],
                'intim': ['intim', 'pelukan', 'hangat'],
                'dominan': ['dominan', 'kontrol'],
                'bdsm': ['bdsm', 'pasrah'],
                'mudah': ['dasar', 'mudah']
            }
            
            tags = mood_map.get(mood.lower(), [])
            if tags:
                tagged = []
                for pos_name in available:
                    pos = self.get_position(pos_name)
                    if any(tag in pos['tags'] for tag in tags):
                        tagged.append(pos_name)
                
                if tagged:
                    chosen = random.choice(tagged)
                    initiative = self.get_bot_initiative(chosen)
                    return chosen, initiative if initiative else f"Ayo {chosen}..."
        
        # Random dengan bobot berdasarkan level
        chosen = random.choice(available)
        initiative = self.get_bot_initiative(chosen)
        
        return chosen, initiative if initiative else f"Ayo {chosen}..."
    
    def change_position(self, current: str, level: int) -> Tuple[str, str]:
        """
        Ganti ke posisi lain
        
        Args:
            current: Posisi saat ini
            level: Level saat ini
            
        Returns:
            Tuple (posisi_baru, pesan)
        """
        available = self.get_positions_by_level(level)
        available = [p for p in available if p != current]
        
        if not available:
            return current, "Kita tetap di posisi ini ya..."
        
        new_pos = random.choice(available)
        
        messages = [
            f"Ganti posisi yuk... {new_pos}...",
            f"Ayo {new_pos}, biar nggak bosen...",
            f"Coba {new_pos} sebentar...",
            f"Kita {new_pos} yuk, biar lebih enak..."
        ]
        
        return new_pos, random.choice(messages)
    
    def get_position_description(self, position_name: str) -> str:
        """
        Dapatkan deskripsi posisi
        
        Args:
            position_name: Nama posisi
            
        Returns:
            String deskripsi
        """
        pos = self.get_position(position_name)
        if pos:
            return f"{pos['name']}: {pos['description']}"
        return f"Posisi {position_name}..."
    
    def get_position_info(self, position_name: str) -> Dict:
        """
        Dapatkan info lengkap posisi
        
        Args:
            position_name: Nama posisi
            
        Returns:
            Dictionary info
        """
        pos = self.get_position(position_name)
        if not pos:
            return {}
        
        return {
            'name': pos['name'],
            'description': pos['description'],
            'level_min': pos['level_min'],
            'difficulty': pos['difficulty'],
            'arousal_boost': pos['arousal_boost'],
            'intimacy_boost': pos['intimacy'],
            'tags': pos['tags']
        }
    
    def format_position_list(self, level: int = None) -> str:
        """
        Format daftar posisi untuk display
        
        Args:
            level: Level saat ini
            
        Returns:
            String terformat
        """
        if level:
            positions = self.get_positions_by_level(level)
            lines = [f"📋 **Posisi Tersedia di Level {level}:**\n"]
        else:
            positions = list(self.positions.keys())
            lines = ["📋 **Semua Posisi:**\n"]
        
        for pos_name in sorted(positions):
            pos = self.get_position(pos_name)
            lock = "🔒" if pos['level_min'] > (level or 0) else "🔓"
            lines.append(
                f"{lock} **{pos['name']}** (Lv.{pos['level_min']}) - {pos['description']}"
            )
        
        return "\n".join(lines)
    
    def get_stats(self) -> Dict:
        """
        Dapatkan statistik posisi
        
        Returns:
            Dictionary statistik
        """
        return {
            'total_positions': len(self.positions),
            'by_level': self.metadata['level_distribution'],
            'by_difficulty': self.metadata['difficulty_distribution'],
            'tags': self.metadata['tags']
        }
    
    def search_positions(self, keyword: str) -> List[Dict]:
        """
        Cari posisi berdasarkan keyword
        
        Args:
            keyword: Kata kunci
            
        Returns:
            List posisi yang cocok
        """
        results = []
        keyword_lower = keyword.lower()
        
        for name, pos in self.positions.items():
            if (keyword_lower in name.lower() or
                keyword_lower in pos['name'].lower() or
                any(keyword_lower in tag for tag in pos['tags']) or
                keyword_lower in pos['description'].lower()):
                
                results.append({
                    'name': name,
                    'display_name': pos['name'],
                    'description': pos['description'][:100] + "...",
                    'level': pos['level_min'],
                    'tags': pos['tags']
                })
        
        return results
