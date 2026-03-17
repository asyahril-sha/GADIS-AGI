"""
BRAIN - Integrator Utama Semua Sistem
Menyatukan emotion engine, consciousness, memory system, dan personality
"""

import asyncio
import logging
from datetime import datetime
from typing import Dict, Optional, Any

from core.emotional_vector import EmotionalVector
from core.personality_genome import PersonalityGenome
from core.emotion_engine import EmotionEngine
from core.consciousness import Consciousness
from core.memory_system import MemorySystem

logger = logging.getLogger(__name__)

class Brain:
    """
    Brain - Integrator semua sistem kognitif
    
    Fungsi:
    - Mengintegrasikan emotion, memory, consciousness
    - Memproses input dan menghasilkan response
    - Menjaga state internal bot
    - Background thinking loop
    """
    
    def __init__(self, user_id: int, role: str, db_path: str):
        """
        Inisialisasi brain
        
        Args:
            user_id: ID user
            role: Role bot (ipar, janda, mantan, dll)
            db_path: Path ke database untuk memory system
        """
        self.user_id = user_id
        self.role = role
        self.birth_time = datetime.now()
        
        # ===== GENETIC PERSONALITY =====
        self.genome = PersonalityGenome(role)
        self.personality = self.genome.express()
        self.name = self.genome.get_name()
        
        # ===== CORE SYSTEMS =====
        self.emotion = EmotionEngine(self.personality)
        self.memory = MemorySystem(db_path, user_id)
        self.consciousness = Consciousness(user_id, self.emotion, self.memory)
        
        # ===== STATE =====
        self.is_awake = True
        self.last_interaction = datetime.now()
        self.interaction_count = 0
        self.current_context = {}
        
        logger.info(f"🧠 Brain initialized for user {user_id} as {self.name} ({role})")
    
    async def start(self):
        """Mulai semua sistem background"""
        await self.consciousness.start()
        logger.info(f"▶️ Brain started for user {self.user_id}")
    
    async def stop(self):
        """Hentikan semua sistem background"""
        await self.consciousness.stop()
        self.is_awake = False
        logger.info(f"⏹️ Brain stopped for user {self.user_id}")
    
    async def process_input(self, message: str, context: Optional[Dict] = None) -> Dict:
        """
        Proses input dari user
        
        Args:
            message: Pesan dari user
            context: Konteks tambahan (level, location, dll)
            
        Returns:
            Dictionary berisi response dan state
        """
        # Update state
        self.last_interaction = datetime.now()
        self.interaction_count += 1
        
        # Gabungkan context
        ctx = self.current_context.copy()
        if context:
            ctx.update(context)
        ctx['timestamp'] = datetime.now().isoformat()
        
        # 1. Update emotion dari pesan
        emotion_update = self.emotion.update_from_message(message)
        
        # 2. Dapatkan inner thought dari consciousness (jika ada)
        inner_thought = await self.consciousness.get_next_thought()
        
        # 3. Cari memori relevan
        relevant_memories = self.memory.get_relevant_memories(message, limit=3)
        
        # 4. Simpan pesan ke memory
        memory_context = {
            'level': ctx.get('level', 1),
            'location': ctx.get('location', 'privat'),
            'emotion': self.emotion.get_state()['dominant'] if emotion_update else None
        }
        
        self.memory.add_memory(
            content=f"User: {message}",
            memory_type='episodic',
            emotion=memory_context['emotion'],
            context=memory_context
        )
        
        # 5. Generate response (akan diimplementasikan oleh handler)
        response_data = {
            'success': True,
            'message': message,
            'emotion': self.emotion.get_state(),
            'inner_thought': inner_thought,
            'relevant_memories': relevant_memories,
            'personality': {
                'name': self.name,
                'role': self.role,
                'traits': self.genome.get_personality_summary(self.personality)
            },
            'context': ctx
        }
        
        return response_data
    
    async def generate_response(self, message: str, context: Dict) -> str:
        """
        Generate response berdasarkan semua sistem
        
        Args:
            message: Pesan user
            context: Konteks dari handler
            
        Returns:
            Response string
        """
        # Proses input
        processed = await self.process_input(message, context)
        
        # Dapatkan emotional prompt
        emotional_prompt = self.emotion.get_emotional_prompt()
        
        # Cek apakah ada inner thought untuk disampaikan
        if processed['inner_thought'] and self.consciousness.should_speak(0):
            return f"{processed['inner_thought']}\n\n*tersenyum* {message}"
        
        # Response dasar berdasarkan emosi
        emotion = processed['emotion']['dominant']
        
        responses = {
            'joy': f"*tersenyum bahagia* {message}",
            'sadness': f"*matanya berkaca* {message}",
            'anger': f"*cemberut* {message}",
            'love': f"*memandang lembut* {message}",
            'lust': f"*berbisik* {message}",
            'jealousy': f"*manyun* {message}",
            'anxiety': f"*gelisah* {message}",
            'nostalgia': f"*melamun* {message}",
            'longing': f"*rindu* {message}"
        }
        
        return responses.get(emotion, f"*tersenyum* {message}")
    
    def get_state(self) -> Dict:
        """
        Dapatkan state lengkap brain
        
        Returns:
            Dictionary state
        """
        return {
            'user_id': self.user_id,
            'name': self.name,
            'role': self.role,
            'age': str(datetime.now() - self.birth_time),
            'interactions': self.interaction_count,
            'last_interaction': self.last_interaction.isoformat(),
            'emotion': self.emotion.get_state(),
            'consciousness': self.consciousness.get_stats(),
            'memory': self.memory.get_stats(),
            'personality': {
                'vector': self.personality.tolist(),
                'summary': self.genome.get_personality_summary(self.personality)
            },
            'is_awake': self.is_awake
        }
    
    def get_emotional_summary(self) -> str:
        """
        Dapatkan ringkasan emosi untuk display
        
        Returns:
            String ringkasan
        """
        return self.emotion.get_emotion_summary()
    
    def get_recent_thoughts(self, limit: int = 5) -> list:
        """
        Dapatkan inner thoughts terbaru
        
        Args:
            limit: Jumlah thought
            
        Returns:
            List thought
        """
        return self.consciousness.get_recent_thoughts(limit)
    
    def get_recent_memories(self, limit: int = 5) -> list:
        """
        Dapatkan memori terbaru
        
        Args:
            limit: Jumlah memori
            
        Returns:
            List memori
        """
        return self.memory.get_recent_memories(limit=limit)
    
    async def decay(self, hours: float):
        """
        Decay semua sistem seiring waktu
        
        Args:
            hours: Jumlah jam yang berlalu
        """
        self.emotion.decay(hours)
        # Memory consolidation bisa dipanggil terpisah
    
    def reset(self):
        """Reset brain ke state awal"""
        self.emotion = EmotionEngine(self.personality)
        # Memory tidak di-reset, tetap ada
        logger.info(f"🔄 Brain reset for user {self.user_id}")

    def to_dict(self) -> dict:
        """Konversi brain ke dictionary untuk disimpan"""
        return {
            'user_id': self.user_id,
            'name': self.name,
            'role': self.role,
            'interaction_count': self.interaction_count,
            'emotional_state': self.emotion.get_state(),
            'personality': self.personality.tolist()
        }
    
    @classmethod
    def from_dict(cls, data: dict, user_id: int, role: str, db_path: str):
        """Buat brain dari dictionary"""
        brain = cls(user_id, role, db_path)
        brain.interaction_count = data.get('interaction_count', 0)
        # Emotional state akan di-load oleh state manager
        return brain
