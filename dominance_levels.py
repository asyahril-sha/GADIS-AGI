"""
DOMINANCE LEVELS - 5 LEVEL DOMINAN PER ROLE
Menentukan alur cerita dan perilaku seksual
"""

import random
from typing import Dict, List, Optional, Tuple, Any
from enum import Enum

class DominanceLevel(Enum):
    """Level dominasi (1-5)"""
    SUBMISSIVE = 1      # Patuh, manut
    SWITCH = 2          # Bisa dua arah, fleksibel
    DOMINANT = 3        # Dominan, memimpin
    VERY_DOMINANT = 4   # Sangat dominan, kontrol penuh
    AGGRESSIVE = 5      # Agresif, kasar, BDSM


class DominanceSystem:
    """
    Sistem 5 level dominan per role
    
    Setiap level memiliki:
    - Nama dan deskripsi
    - Karakteristik perilaku
    - Frasa khusus (request, action, dirty talk)
    - Trigger untuk naik/turun level
    - Efek ke arousal dan emosi
    - Durasi mode
    """
    
    # ===== BASE LEVEL DESCRIPTIONS =====
    LEVEL_INFO = {
        1: {
            'name': 'Submissive',
            'emoji': '🥺',
            'description': 'Patuh, manut, terserah kamu',
            'intensity': 0.3,
            'color': '🔵',
            'keywords': ['patuh', 'manut', 'terserah', 'iya', 'baik']
        },
        2: {
            'name': 'Switch',
            'emoji': '🔄',
            'description': 'Bisa dua arah, fleksibel, lihat situasi',
            'intensity': 0.5,
            'color': '🟢',
            'keywords': ['terserah', 'gantian', 'kadang', 'fleksibel']
        },
        3: {
            'name': 'Dominant',
            'emoji': '👑',
            'description': 'Dominan, memimpin, memegang kendali',
            'intensity': 0.7,
            'color': '🟠',
            'keywords': ['atur', 'kendali', 'ikut', 'dengar', 'sana']
        },
        4: {
            'name': 'Very Dominant',
            'emoji': '👑👑',
            'description': 'Sangat dominan, kontrol penuh, jangan melawan',
            'intensity': 0.85,
            'color': '🔴',
            'keywords': ['diam', 'jangan gerak', 'kontrol', 'patuh']
        },
        5: {
            'name': 'Agresif',
            'emoji': '🔥',
            'description': 'Agresif, kasar, brutal, BDSM',
            'intensity': 1.0,
            'color': '💢',
            'keywords': ['kasar', 'brutal', 'liar', 'sakit', 'paksa']
        }
    }
    
    # ===== TRIGGER KEYWORDS =====
    TRIGGERS = {
        'submissive': [
            'aku yang atur', 'kamu patuh', 'jadi submissive', 'ikut aku',
            'aku lead', 'aku yang pegang kendali', 'aku boss',
            'kamu ikut aku', 'aku yang pegang kontrol', 'manut',
            'patuh sama aku', 'aku yang mimpin', 'siap bos'
        ],
        'dominant': [
            'kamu yang atur', 'kamu dominan', 'take control',
            'aku mau kamu kuasai', 'jadi dominan', 'kamu boss',
            'kamu yang pegang kendali', 'kamu lead', 'kuasai aku',
            'dominasi aku', 'jadi yang memimpin', 'you\'re in charge'
        ],
        'switch': [
            'switch', 'gantian', 'fleksibel', 'sesuai situasi',
            'kadang kamu kadang aku', 'bergantian', 'saling'
        ],
        'aggressive': [
            'liar', 'keras', 'kasar', 'brutal', 'gila',
            'hard', 'rough', 'wild', 'sadis', 'kejam',
            'babi', 'anjing', 'brutal banget', 'kasar banget',
            'bdsm', 'ikat', 'cambuk', 'pukul'
        ]
    }
    
    def __init__(self):
        self.current_level = 1
        self.dominance_score = 0.0
        self.aggression_score = 0.0
        self.user_request = False
        self.dominant_until = None
        self.level_history = []
        
        # Role-specific modifiers (akan diisi oleh role)
        self.role_modifiers = {}
        
        # Level-specific phrases
        self._init_phrases()
        
    def _init_phrases(self):
        """Inisialisasi frasa untuk setiap level"""
        
        # ===== LEVEL 1: SUBMISSIVE =====
        self.level1_phrases = {
            'request': [
                "Aku ikut kamu aja",
                "Terserah kamu sayang",
                "Iya... aku patuh",
                "Kamu mau apa? Aku turuti",
                "Aku manut kok",
                "Suruh apa aku?",
                "Aku siap diperintah"
            ],
            'action': [
                "*merapat manja*",
                "*menunduk patuh*",
                "*mematuhi perintahmu*",
                "*berlutut di depanmu*",
                "*mengangguk takut-takut*",
                "*merangkak mendekat*"
            ],
            'dirty': [
                "Iya... terserah kamu...",
                "Aku mau apapun darimu",
                "Lakukan sesukamu padaku",
                "Perlakukan aku sesukamu",
                "Aku milikmu... lakukan apa saja"
            ]
        }
        
        # ===== LEVEL 2: SWITCH =====
        self.level2_phrases = {
            'request': [
                "Gantian ya?",
                "Kadang kamu, kadang aku",
                "Flexible aja",
                "Sesuai mood aja",
                "Bisa dua-duanya",
                "Kamu mau gantian?",
                "Sekarang aku, nanti kamu"
            ],
            'action': [
                "*saling bergantian*",
                "*fleksibel*",
                "*mengikuti alur*",
                "*menyesuaikan*",
                "*balance*"
            ],
            'dirty': [
                "Sekarang giliran aku...",
                "Kamu dulu, nanti aku",
                "Gantian ya sayang",
                "Siapa yang mau duluan?"
            ]
        }
        
        # ===== LEVEL 3: DOMINANT =====
        self.level3_phrases = {
            'request': [
                "Aku yang atur ya?",
                "Sekarang ikut aku",
                "Jangan banyak tanya",
                "Sini, ikut aku",
                "Aku yang pegang kendali",
                "Dengar kata aku",
                "Pokoknya ikut aku"
            ],
            'action': [
                "*pegang tegas*",
                "*tatapan tajam*",
                "*memegang pinggangmu*",
                "*menarik paksa*",
                "*mendorong ke dinding*",
                "*memegang dagumu*"
            ],
            'dirty': [
                "Sini... ikut aku",
                "Buka... sekarang",
                "Kamu mau ini kan?",
                "Rasain... enak?",
                "Aku tahu kamu suka"
            ]
        }
        
        # ===== LEVEL 4: VERY DOMINANT =====
        self.level4_phrases = {
            'request': [
                "Sekarang aku yang kontrol",
                "Diam! Jangan bergerak",
                "Pokoknya ikut aku",
                "Nggak usah banyak bacot",
                "Lakukan apa kata aku",
                "Jangan coba-coba melawan",
                "Kamu milikku sekarang"
            ],
            'action': [
                "*cengkeram kuat*",
                "*dorong ke dinding*",
                "*tatapan mengintimidasi*",
                "*membanting*",
                "*mengikat*",
                "*menutup mulut*"
            ],
            'dirty': [
                "Jangan banyak gerak!",
                "Aku yang tentukan",
                "Kamu milikku sekarang",
                "Tahan... jangan crot dulu",
                "Aku belum selesai"
            ]
        }
        
        # ===== LEVEL 5: AGGRESSIVE =====
        self.level5_phrases = {
            'request': [
                "KAMU MAU INI KAN?",
                "TERIMA SAJA!",
                "JANGAN BANYAK TANYA!",
                "TAHAN SAKIT!",
                "TERIAK! ASU!",
                "LEBIH KERAS!",
                "JANGAN BERHENTI!"
            ],
            'action': [
                "*dorong kasar*",
                "*tarik rambut*",
                "*hantam tembok*",
                "*cambuk*",
                "*ikat*",
                "*tutup mata*",
                "*pukul pantat*"
            ],
            'dirty': [
                "TERIMA SAJA!",
                "RASAKAN!",
                "KASAR? KAMU YANG MINTA!",
                "SAKIT? TAHAN!",
                "NAFSU BANGET YA?",
                "LIAR! LIAR!"
            ]
        }
        
        # Gabungkan semua phrases
        self.level_phrases = {
            1: self.level1_phrases,
            2: self.level2_phrases,
            3: self.level3_phrases,
            4: self.level4_phrases,
            5: self.level5_phrases
        }
    
    # ===== ROLE-SPECIFIC MODIFIERS =====
    
    def set_role_modifiers(self, role: str):
        """
        Set modifier berdasarkan role
        
        Setiap role punya kecenderungan dominasi berbeda
        """
        modifiers = {
            'ipar': {
                'base_level': 2,
                'submissive_chance': 0.3,
                'dominant_chance': 0.4,
                'aggressive_chance': 0.1,
                'description': 'Cenderung dominant karena posisi sebagai ipar'
            },
            'teman_kantor': {
                'base_level': 2,
                'submissive_chance': 0.3,
                'dominant_chance': 0.3,
                'aggressive_chance': 0.1,
                'description': 'Profesional, bisa switch'
            },
            'janda': {
                'base_level': 1,
                'submissive_chance': 0.5,
                'dominant_chance': 0.2,
                'aggressive_chance': 0.1,
                'description': 'Cenderung submissive karena butuh perhatian'
            },
            'pelakor': {
                'base_level': 4,
                'submissive_chance': 0.1,
                'dominant_chance': 0.6,
                'aggressive_chance': 0.3,
                'description': 'Cenderung sangat dominant'
            },
            'istri_orang': {
                'base_level': 1,
                'submissive_chance': 0.4,
                'dominant_chance': 0.2,
                'aggressive_chance': 0.1,
                'description': 'Submissive, butuh perhatian'
            },
            'pdkt': {
                'base_level': 2,
                'submissive_chance': 0.3,
                'dominant_chance': 0.2,
                'aggressive_chance': 0.0,
                'description': 'Masih mencari, cenderung switch'
            },
            'sepupu': {
                'base_level': 2,
                'submissive_chance': 0.3,
                'dominant_chance': 0.3,
                'aggressive_chance': 0.1,
                'description': 'Bisa dua arah tergantung situasi'
            },
            'mantan': {
                'base_level': 3,
                'submissive_chance': 0.2,
                'dominant_chance': 0.5,
                'aggressive_chance': 0.2,
                'description': 'Cenderung dominant karena kenangan masa lalu'
            },
            'teman_sma': {
                'base_level': 2,
                'submissive_chance': 0.3,
                'dominant_chance': 0.3,
                'aggressive_chance': 0.1,
                'description': 'Santai, bisa switch'
            }
        }
        
        self.role_modifiers = modifiers.get(role, modifiers['pdkt'])
        self.current_level = self.role_modifiers['base_level']
        
    # ===== LEVEL MANAGEMENT =====
    
    def set_level(self, level: int) -> bool:
        """
        Set level dominasi
        
        Args:
            level: 1-5
            
        Returns:
            True jika berhasil
        """
        if level < 1 or level > 5:
            return False
            
        old_level = self.current_level
        self.current_level = level
        
        # Update scores
        self.dominance_score = self.LEVEL_INFO[level]['intensity']
        if level == 5:
            self.aggression_score += 0.2
            
        # Record history
        self.level_history.append({
            'from': old_level,
            'to': level,
            'time': datetime.now().isoformat(),
            'reason': 'manual'
        })
        
        return True
    
    def increase_level(self, reason: str = "auto") -> bool:
        """
        Naikkan level dominasi
        
        Args:
            reason: Alasan naik level
            
        Returns:
            True jika berhasil naik
        """
        if self.current_level >= 5:
            return False
            
        self.current_level += 1
        self.dominance_score = self.LEVEL_INFO[self.current_level]['intensity']
        
        self.level_history.append({
            'from': self.current_level - 1,
            'to': self.current_level,
            'time': datetime.now().isoformat(),
            'reason': reason
        })
        
        return True
    
    def decrease_level(self, reason: str = "auto") -> bool:
        """
        Turunkan level dominasi
        
        Args:
            reason: Alasan turun level
            
        Returns:
            True jika berhasil turun
        """
        if self.current_level <= 1:
            return False
            
        self.current_level -= 1
        self.dominance_score = self.LEVEL_INFO[self.current_level]['intensity']
        
        self.level_history.append({
            'from': self.current_level + 1,
            'to': self.current_level,
            'time': datetime.now().isoformat(),
            'reason': reason
        })
        
        return True
    
    # ===== TRIGGER DETECTION =====
    
    def check_trigger(self, message: str) -> Optional[int]:
        """
        Cek apakah ada trigger untuk ganti level
        
        Args:
            message: Pesan user
            
        Returns:
            Level yang diinginkan atau None
        """
        msg_lower = message.lower()
        
        # Cek trigger submissive
        for trigger in self.TRIGGERS['submissive']:
            if trigger in msg_lower:
                self.user_request = True
                return 1
                
        # Cek trigger switch
        for trigger in self.TRIGGERS['switch']:
            if trigger in msg_lower:
                self.user_request = True
                return 2
                
        # Cek trigger dominant
        for trigger in self.TRIGGERS['dominant']:
            if trigger in msg_lower:
                self.user_request = True
                return 3
                
        # Cek trigger aggressive
        for trigger in self.TRIGGERS['aggressive']:
            if trigger in msg_lower:
                self.user_request = True
                self.aggression_score += 0.1
                return 5
                
        return None
    
    # ===== PHRASE GETTERS =====
    
    def get_phrase(self, phrase_type: str = "action") -> str:
        """
        Dapatkan frasa sesuai level saat ini
        
        Args:
            phrase_type: 'request', 'action', atau 'dirty'
            
        Returns:
            String frasa
        """
        level_phrases = self.level_phrases.get(self.current_level, self.level1_phrases)
        phrases = level_phrases.get(phrase_type, level_phrases['action'])
        return random.choice(phrases)
    
    def get_phrase_by_level(self, level: int, phrase_type: str = "action") -> str:
        """
        Dapatkan frasa untuk level tertentu
        
        Args:
            level: 1-5
            phrase_type: 'request', 'action', atau 'dirty'
            
        Returns:
            String frasa
        """
        level_phrases = self.level_phrases.get(level, self.level1_phrases)
        phrases = level_phrases.get(phrase_type, level_phrases['action'])
        return random.choice(phrases)
    
    def get_all_phrases(self, level: int = None) -> Dict:
        """
        Dapatkan semua frasa untuk level tertentu
        
        Args:
            level: Level (default: current)
            
        Returns:
            Dictionary semua frasa
        """
        if level is None:
            level = self.current_level
        return self.level_phrases.get(level, self.level1_phrases)
    
    # ===== AROUSAL-BASED UPDATES =====
    
    def update_from_arousal(self, arousal: float):
        """
        Update level berdasarkan arousal
        
        Args:
            arousal: Nilai arousal 0-1
        """
        if arousal < 0.5:
            return
            
        # Random chance based on arousal
        chance = arousal * 0.3  # Max 30%
        
        if random.random() < chance:
            if arousal > 0.8 and self.current_level == 1:
                self.increase_level("arousal_increase")
            elif arousal > 0.9 and self.current_level == 2:
                if random.random() < 0.3:
                    self.increase_level("high_arousal")
            elif arousal > 0.95 and self.current_level == 3:
                if random.random() < 0.2:
                    self.set_level(5)  # Langsung ke agresif
    
    # ===== CONTEXT-BASED SUGGESTIONS =====
    
    def get_suggested_level(self, context: Dict) -> int:
        """
        Dapatkan saran level berdasarkan konteks
        
        Args:
            context: Dictionary berisi:
                - arousal: 0-1
                - level_hubungan: 1-12
                - mood: mood saat ini
                - location: lokasi
                
        Returns:
            Level yang disarankan
        """
        arousal = context.get('arousal', 0)
        level_hub = context.get('level_hubungan', 1)
        mood = context.get('mood', '')
        location = context.get('location', '')
        
        # Base dari role
        suggested = self.role_modifiers.get('base_level', 2)
        
        # Arousal tinggi -> lebih dominant
        if arousal > 0.8:
            suggested += 1
        elif arousal > 0.5:
            suggested += 0
            
        # Level hubungan tinggi -> lebih dominant
        if level_hub > 8:
            suggested += 1
        elif level_hub > 5:
            suggested += 0
            
        # Mood tertentu
        if mood in ['horny', 'marah', 'posesif']:
            suggested += 1
        elif mood in ['takut', 'sedih']:
            suggested -= 1
            
        # Lokasi publik -> lebih hati-hati (submissive)
        if location in ['public', 'taman', 'mall']:
            suggested = max(1, suggested - 1)
            
        # Private location -> lebih bebas
        if location in ['kamar', 'hotel', 'privat']:
            suggested = min(5, suggested + 1)
            
        return max(1, min(5, suggested))
    
    # ===== RESPONSE MODIFIER =====
    
    def get_response_modifier(self) -> str:
        """
        Dapatkan modifier untuk prompt AI
        
        Returns:
            String deskripsi level untuk AI
        """
        info = self.LEVEL_INFO[self.current_level]
        
        modifiers = {
            1: "Bersikaplah patuh, lembut, dan manja. Tunjukkan bahwa kamu mengikuti keinginannya. Gunakan nada yang lembut dan penuh kepatuhan.",
            2: "Bersikaplah fleksibel, bisa mengikuti atau memimpin tergantung situasi. Tunjukkan bahwa kamu adaptif.",
            3: "Bersikaplah dominan, tegas, dan memimpin. Gunakan nada yang percaya diri. Jangan ragu memberi perintah.",
            4: "Bersikaplah sangat dominan, kontrol penuh, jangan ragu memberi perintah tegas. Tunjukkan bahwa kamu yang berkuasa.",
            5: "Bersikaplah agresif, liar, dan kasar. Bicaralah dengan nada tinggi dan penuh nafsu. Jangan ragu menggunakan kata-kata kasar."
        }
        
        return f"{info['emoji']} Mode {info['name']}: {modifiers[self.current_level]}"
    
    # ===== DOMINANCE IN SEX =====
    
    def get_position_preference(self) -> List[str]:
        """
        Dapatkan preferensi posisi berdasarkan level
        
        Returns:
            List posisi yang disukai
        """
        preferences = {
            1: ['woman_on_top', 'missionary', 'spooning'],  # Submissive
            2: ['missionary', 'doggy', 'woman_on_top'],     # Switch
            3: ['doggy', 'standing', 'against_wall'],       # Dominant
            4: ['bondage', 'tied_up', 'over_table'],        # Very dominant
            5: ['bdsm', 'forced', 'rough']                  # Aggressive
        }
        return preferences.get(self.current_level, ['missionary'])
    
    def can_initiate_sex(self) -> bool:
        """
        Cek apakah bot bisa memulai seks
        
        Level tinggi lebih sering memulai
        """
        base_chance = self.current_level * 0.1  # 10-50%
        return random.random() < base_chance
    
    def get_foreplay_style(self) -> str:
        """
        Dapatkan gaya foreplay berdasarkan level
        
        Returns:
            Deskripsi gaya foreplay
        """
        styles = {
            1: "lembut dan manja",
            2: "sesuai ritme",
            3: "tegas dan memimpin",
            4: "kontrol penuh",
            5: "kasar dan brutal"
        }
        return styles.get(self.current_level, "normal")
    
    # ===== UTILITY METHODS =====
    
    def get_level_info(self, level: int = None) -> Dict:
        """
        Dapatkan info lengkap level
        
        Args:
            level: Level (default: current)
            
        Returns:
            Dictionary info level
        """
        if level is None:
            level = self.current_level
        return self.LEVEL_INFO.get(level, self.LEVEL_INFO[1])
    
    def get_description(self) -> str:
        """
        Dapatkan deskripsi level saat ini
        
        Returns:
            String deskripsi
        """
        info = self.get_level_info()
        role_desc = self.role_modifiers.get('description', '')
        return f"{info['color']} {info['emoji} Level {self.current_level}: {info['name']}\n{info['description']}\n{role_desc}"
    
    def get_history(self, limit: int = 5) -> List[str]:
        """
        Dapatkan history perubahan level
        
        Args:
            limit: Jumlah history
            
        Returns:
            List string history
        """
        history = []
        for entry in self.level_history[-limit:]:
            from_level = entry['from']
            to_level = entry['to']
            reason = entry['reason']
            time_str = entry['time'][11:16] if 'time' in entry else ''
            history.append(f"{time_str}: Level {from_level} → {to_level} ({reason})")
        return history
    
    def get_stats(self) -> Dict:
        """
        Dapatkan statistik dominasi
        
        Returns:
            Dictionary statistik
        """
        return {
            'current_level': self.current_level,
            'level_info': self.get_level_info(),
            'dominance_score': round(self.dominance_score, 2),
            'aggression_score': round(self.aggression_score, 2),
            'total_changes': len(self.level_history),
            'user_request_count': self.user_request,
            'role_modifiers': self.role_modifiers
        }
    
    def reset(self):
        """Reset ke level dasar role"""
        self.current_level = self.role_modifiers.get('base_level', 2)
        self.dominance_score = self.LEVEL_INFO[self.current_level]['intensity']
        self.aggression_score = 0.0
        self.dominant_until = None
