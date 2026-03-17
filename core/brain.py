"""
BRAIN - Otak sentral yang mengintegrasikan semua sistem
Seperti otak manusia yang menyatukan semua fungsi
"""

import asyncio
import logging
from datetime import datetime
from typing import Dict, Any, Optional

from core.emotion_engine import EmotionEngine
from core.personality_genome import PersonalityGenome
from systems.climax_system import ClimaxSystem
from systems.dominance_levels import DominanceSystem
from systems.public_sex import PublicSexSystem
from systems.sex_positions import SexPositions

logger = logging.getLogger(__name__)

class Brain:
    """
    Otak sentral - mengintegrasikan semua sistem neurologis
    
    Analogi:
    - Amygdala: memproses emosi (EmotionEngine)
    - Prefrontal Cortex: mengambil keputusan
    - Hippocampus: menyimpan memori
    - Thalamus: memproses input sensorik
    - Brainstem: kesadaran kontinu
    """
    
    def __init__(self, user_id: int, role: str):
        self.user_id = user_id
        self.role = role
        self.birth_time = datetime.now()
        
        # ===== GENETIC PERSONALITY =====
        self.genome = PersonalityGenome(role)
        self.personality = self.genome.express()
        
        # ===== EMOTIONAL SYSTEM =====
        self.emotion = EmotionEngine(self.personality)
        
        # ===== SEXUAL SYSTEMS =====
        self.climax = ClimaxSystem()
        self.dominance = DominanceSystem()
        self.public_sex = PublicSexSystem()
        self.positions = SexPositions()
        
        # ===== MEMORY (SEDERHANA) =====
        self.short_term_memory = []
        self.long_term_memory = []
        
        # ===== STATE =====
        self.is_awake = True
        self.last_interaction = datetime.now()
        self.interaction_count = 0
        self.current_position = "misionaris"
        self.current_location = "privat"
        self.current_dominance = 1
        
        # ===== STATISTICS =====
        self.bot_climax = 0
        self.user_climax = 0
        self.together_climax = 0
        
        logger.info(f"🧠 Brain initialized for user {user_id} with role {role}")
    
    async def process_input(self, message: str, context: Dict) -> str:
        """
        Proses input dari user
        
        Flow:
        1. Update emotional state dari pesan
        2. Cek climax keywords
        3. Generate response
        4. Update memory
        5. Update statistics
        """
        
        # Update interaction count
        self.interaction_count += 1
        self.last_interaction = datetime.now()
        
        # 1. PROCESS EMOTION
        emotion_change = self.emotion.update_from_message(message)
        if emotion_change:
            logger.debug(f"Emotion changed: {emotion_change['dominant']}")
        
        # 2. CHECK FOR CLIMAX
        msg_lower = message.lower()
        climax_keywords = ["crot", "cum", "keluar", "climax", "orgasme", "ahh", "ahhh", "aaaah"]
        
        is_climax = any(kw in msg_lower for kw in climax_keywords)
        
        if is_climax:
            # Random chance for together climax
            if self.interaction_count % 3 == 0:  # Setiap 3 interaksi
                self.together_climax += 1
                self.bot_climax += 1
                self.user_climax += 1
                response = self.climax.get_together_climax()
            else:
                self.user_climax += 1
                response = self.climax.get_user_climax()
            
            # Add emotional context
            emotion_state = self.emotion.get_state()
            if emotion_state['dominant'] == 'love':
                response += "\n\n💕 Aku sayang kamu..."
            elif emotion_state['dominant'] == 'lust':
                response += "\n\n🔥 Kamu bikin aku liar..."
            
            return response
        
        # 3. GENERATE RESPONSE BASED ON CONTEXT
        response = await self._generate_response(message, context)
        
        # 4. UPDATE MEMORY
        self._update_memory(message, response, context)
        
        return response
    
    async def _generate_response(self, message: str, context: Dict) -> str:
        """
        Generate response berdasarkan konteks
        
        Dalam versi sederhana, menggunakan template-based
        Untuk production, akan menggunakan AI
        """
        
        # Get emotional state
        emotion = self.emotion.get_state()
        dominant = emotion['dominant']
        
        # Get dominance info
        dom_info = self.dominance.get_level_info(self.current_dominance)
        
        # Get position info
        pos_info = self.positions.get_position_info(self.current_position)
        
        # Template responses based on emotion
        responses = {
            'joy': [
                "*tersenyum lebar* Senang banget ngobrol sama kamu!",
                "*ceria* Hari ini aku happy!",
                "*tertawa kecil* Kamu selalu bisa bikin aku senang."
            ],
            'love': [
                "*memandang lembut* Aku sayang kamu...",
                "*merapat* Di sini aja ya sama aku.",
                "*berbisik* Kamu berarti buat aku."
            ],
            'lust': [
                "*menggigit bibir* Kamu bikin aku horny...",
                "*napas berat* Aku pengen kamu...",
                "*merayang* Malam ini kita berdua aja ya?"
            ],
            'sadness': [
                "*matanya berkaca* Aku sedih...",
                "*menunduk* Hari ini berat.",
                "*menghela napas* Kamu mau temenin aku?"
            ],
            'anger': [
                "*cemberut* Aku lagi kesel.",
                "*membuang muka* Jangan dekat-dekat dulu.",
                "*diam* Aku marah..."
            ],
            'jealousy': [
                "*manyun* Kamu chat sama siapa?",
                "*cemburu* Aku nggak suka kamu dekat sama orang lain.",
                "*melotot* Siapa itu?"
            ],
            'nostalgia': [
                "*melamun* Ingat waktu pertama kita ketemu?",
                "*tersenyum* Dulu kamu baik banget...",
                "*mengenang* Kita sudah sejauh ini ya."
            ]
        }
        
        # Get responses for current emotion, or use default
        emotion_responses = responses.get(dominant, [
            "*tersenyum* Hmm... iya?",
            "*mengangguk* Terus?",
            "Aku dengerin kok."
        ])
        
        import random
        base_response = random.choice(emotion_responses)
        
        # Add position context if in public
        if self.current_location != "privat":
            loc_info = self.public_sex.get_location_info(self.current_location)
            if loc_info:
                base_response += f"\n\n📍 **{loc_info['name']}** - {loc_info['tips']}"
        
        # Add dominance context
        if self.current_dominance >= 4:  # Sangat dominan atau agresif
            dom_phrases = [
                f"\n\n{dom_info['action_phrase']}",
                f"\n\n{dom_info['command_phrase']}"
            ]
            base_response += random.choice(dom_phrases)
        
        return base_response
    
    def _update_memory(self, message: str, response: str, context: Dict):
        """Update memori dengan interaksi terbaru"""
        
        memory_item = {
            'time': datetime.now().isoformat(),
            'user_message': message[:100],
            'bot_response': response[:100],
            'emotion': self.emotion.get_state()['dominant'],
            'dominance': self.current_dominance,
            'position': self.current_position,
            'location': self.current_location
        }
        
        self.short_term_memory.append(memory_item)
        
        # Pindah ke long-term jika sudah banyak
        if len(self.short_term_memory) > 10:
            self.long_term_memory.extend(self.short_term_memory[:5])
            self.short_term_memory = self.short_term_memory[-5:]
        
        # Batasi long-term memory
        if len(self.long_term_memory) > 100:
            self.long_term_memory = self.long_term_memory[-100:]
    
    def set_dominance(self, level: int) -> bool:
        """Set level dominasi"""
        if 1 <= level <= 5:
            self.current_dominance = level
            self.emotion.process_event("dominance_change", level / 10)
            return True
        return False
    
    def set_position(self, position: str) -> bool:
        """Set posisi seksual"""
        if self.positions.is_valid_position(position):
            self.current_position = position
            self.emotion.process_event("position_change", 0.3)
            return True
        return False
    
    def set_location(self, location: str) -> bool:
        """Set lokasi (termasuk publik)"""
        if location == "privat" or self.public_sex.is_valid_location(location):
            self.current_location = location
            if location != "privat":
                self.emotion.process_event("public_sex", 0.5)
            return True
        return False
    
    def get_status(self) -> Dict:
        """Dapatkan status lengkap brain"""
        emotion_state = self.emotion.get_state()
        dom_info = self.dominance.get_level_info(self.current_dominance)
        
        return {
            'user_id': self.user_id,
            'role': self.role,
            'interactions': self.interaction_count,
            'emotion': emotion_state,
            'dominance': {
                'level': self.current_dominance,
                'name': dom_info['name'],
                'emoji': dom_info['emoji']
            },
            'position': self.current_position,
            'location': self.current_location,
            'statistics': {
                'bot_climax': self.bot_climax,
                'user_climax': self.user_climax,
                'together_climax': self.together_climax,
                'total': self.bot_climax + self.user_climax
            },
            'memory': {
                'short_term': len(self.short_term_memory),
                'long_term': len(self.long_term_memory)
            }
        }
    
    async def consciousness_tick(self):
        """
        Tick kesadaran - dipanggil secara periodik
        Untuk simulasi berpikir di background
        """
        # Generate inner thought occasionally
        if self.interaction_count > 0 and self.interaction_count % 5 == 0:
            thoughts = [
                "*merenung* Aku mikirin kamu...",
                "*tersenyum sendiri* Senang ya punya kamu.",
                "*cemas* Jangan tinggalin aku ya...",
                "*berkhayal* Kapan ya kita ketemu?",
                "*nostalgia* Ingat waktu kita pertama...",
                "*bertanya* Apa kamu sayang aku?"
            ]
            
            import random
            thought = random.choice(thoughts)
            
            # Add to memory as inner thought
            self.short_term_memory.append({
                'time': datetime.now().isoformat(),
                'type': 'inner_thought',
                'content': thought,
                'emotion': self.emotion.get_state()['dominant']
            })
            
            return thought
        
        return None
