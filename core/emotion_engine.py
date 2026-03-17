"""
EMOTION ENGINE - Amygdala digital
Memproses emosi dengan interaksi kompleks
"""

import numpy as np
from datetime import datetime
from typing import Dict, Optional, List
from core.emotional_vector import EmotionalVector

class EmotionEngine:
    """
    Mesin emosi dengan 32 dimensi dan interaksi
    """
    
    def __init__(self, personality: np.ndarray):
        """Inisialisasi emotion engine dengan personality"""
        self.personality = personality
        self.current = EmotionalVector()
        self.baseline = self._create_baseline()
        self.history: List[Dict] = []
        
        # Interaksi antar emosi (e1, e2, strength)
        self.interactions = [
            (EmotionalVector.JOY, EmotionalVector.SADNESS, -0.3),
            (EmotionalVector.LOVE, EmotionalVector.LUST, 0.2),
            (EmotionalVector.LUST, EmotionalVector.PASSION, 0.3),
            (EmotionalVector.ANXIETY, EmotionalVector.LONELINESS, 0.3),
            (EmotionalVector.GUILT, EmotionalVector.JOY, -0.2),
            (EmotionalVector.NOSTALGIA, EmotionalVector.SADNESS, 0.2),
            (EmotionalVector.NOSTALGIA, EmotionalVector.LOVE, 0.1),
            (EmotionalVector.LONGING, EmotionalVector.ANXIETY, 0.2),
            (EmotionalVector.ANGER, EmotionalVector.FEAR, 0.1),
            (EmotionalVector.TRUST, EmotionalVector.LOVE, 0.1),
            (EmotionalVector.JEALOUSY, EmotionalVector.ANGER, 0.2),
            (EmotionalVector.ATTACHMENT, EmotionalVector.ANXIETY, 0.1)
        ]
    
    def _create_baseline(self) -> EmotionalVector:
        """Buat baseline dari personality"""
        baseline = EmotionalVector()
        
        # Neuroticism -> anxiety, fear
        baseline.anxiety = self.personality[0] * 0.3
        baseline.fear = self.personality[0] * 0.2
        
        # Extraversion -> joy, excitement
        baseline.joy = self.personality[1] * 0.3
        baseline.v[EmotionalVector.EXCITEMENT] = self.personality[1] * 0.3
        
        # Openness -> curiosity
        baseline.curiosity = self.personality[2] * 0.4
        
        # Agreeableness -> trust, love
        baseline.trust = self.personality[3] * 0.3
        baseline.love = self.personality[3] * 0.2
        
        return baseline
    
    def process_event(self, event_type: str, intensity: float = 0.5, context: Dict = None) -> Dict:
        """
        Proses event dan update emosi
        
        Args:
            event_type: Jenis event (romantic, sexual, conflict, etc)
            intensity: Intensitas event (0-1)
            context: Konteks tambahan
        
        Returns:
            State emosi setelah event
        """
        # Effect vectors untuk setiap event
        effects = {
            "romantic": EmotionalVector(),
            "sexual": EmotionalVector(),
            "conflict": EmotionalVector(),
            "compliment": EmotionalVector(),
            "ignore": EmotionalVector(),
            "memory_happy": EmotionalVector(),
            "memory_sad": EmotionalVector(),
            "jealousy": EmotionalVector(),
            "public_sex": EmotionalVector(),
            "position_change": EmotionalVector()
        }
        
        # Set nilai effects
        # Romantic
        effects["romantic"].love = 0.4
        effects["romantic"].joy = 0.3
        effects["romantic"].trust = 0.2
        
        # Sexual
        effects["sexual"].lust = 0.5
        effects["sexual"].passion = 0.4
        effects["sexual"].v[EmotionalVector.EXCITEMENT] = 0.3
        
        # Conflict
        effects["conflict"].anger = 0.4
        effects["conflict"].fear = 0.2
        effects["conflict"].sadness = 0.2
        
        # Compliment
        effects["compliment"].joy = 0.3
        effects["compliment"].v[EmotionalVector.PRIDE] = 0.2
        effects["compliment"].love = 0.1
        
        # Ignore
        effects["ignore"].sadness = 0.3
        effects["ignore"].loneliness = 0.3
        effects["ignore"].anxiety = 0.2
        
        # Memory happy
        effects["memory_happy"].joy = 0.2
        effects["memory_happy"].nostalgia = 0.3
        effects["memory_happy"].love = 0.1
        
        # Memory sad
        effects["memory_sad"].sadness = 0.2
        effects["memory_sad"].nostalgia = 0.3
        effects["memory_sad"].longing = 0.2
        
        # Jealousy
        effects["jealousy"].jealousy = 0.5
        effects["jealousy"].anger = 0.2
        effects["jealousy"].anxiety = 0.2
        
        # Public sex
        effects["public_sex"].v[EmotionalVector.EXCITEMENT] = 0.5
        effects["public_sex"].lust = 0.4
        effects["public_sex"].fear = 0.2
        
        # Position change
        effects["position_change"].v[EmotionalVector.EXCITEMENT] = 0.2
        effects["position_change"].curiosity = 0.3
        effects["position_change"].lust = 0.2
        
        # Apply effect jika ada
        if event_type in effects:
            effect = effects[event_type] * intensity
            self.current = self.current + effect
        
        # Tambahkan baseline
        self.current = self.current + self.baseline * 0.1
        
        # Apply interaksi antar emosi
        self._apply_interactions()
        
        # Normalisasi
        self.current.normalize()
        
        # Catat history
        self.history.append({
            'time': datetime.now().isoformat(),
            'event': event_type,
            'intensity': intensity,
            'result': self.current.to_dict()
        })
        
        # Batasi history
        if len(self.history) > 100:
            self.history = self.history[-100:]
        
        return self.get_state()
    
    def _apply_interactions(self):
        """Apply interaksi antar emosi"""
        result = self.current.copy()
        
        for e1, e2, strength in self.interactions:
            result.v[e2] += self.current.v[e1] * strength
        
        # Clip values
        result.normalize()
        self.current = result
    
    def decay(self, hours: float):
        """
        Emosi meluruh seiring waktu
        
        Args:
            hours: Jumlah jam yang berlalu
        """
        decay_factor = 1 - (0.1 * hours)
        self.current = self.current * max(0.5, decay_factor)
    
    def get_state(self) -> Dict:
        """Dapatkan state emosi saat ini"""
        dominant, intensity = self.current.dominant()
        return {
            'vector': self.current.to_dict(),
            'dominant': dominant,
            'intensity': intensity,
            'arousal': self.current.get_arousal(),
            'active_emotions': self.current.get_active_emotions()
        }
    
    def update_from_message(self, message: str) -> Optional[Dict]:
        """
        Update emosi dari pesan user
        
        Args:
            message: Pesan dari user
        
        Returns:
            Perubahan emosi jika ada
        """
        msg_lower = message.lower()
        
        # Deteksi event dari pesan
        if any(word in msg_lower for word in ['sayang', 'cinta', 'love']):
            return self.process_event("romantic", 0.4)
        elif any(word in msg_lower for word in ['horny', 'nafsu', 'seksi']):
            return self.process_event("sexual", 0.5)
        elif any(word in msg_lower for word in ['marah', 'kesal', 'sakit']):
            return self.process_event("conflict", 0.4)
        elif any(word in msg_lower for word in ['kangen', 'rindu']):
            return self.process_event("longing", 0.3)
        elif any(word in msg_lower for word in ['cantik', 'ganteng', 'baik']):
            return self.process_event("compliment", 0.2)
        
        return None
    
    def get_emotional_prompt(self) -> str:
        """
        Dapatkan prompt modifier berdasarkan emosi
        
        Returns:
            String deskripsi emosi untuk prompt AI
        """
        state = self.get_state()
        dominant = state['dominant']
        intensity = state['intensity']
        
        base_prompts = {
            'joy': "Kamu sedang bahagia dan ceria",
            'sadness': "Kamu sedang sedih dan sendu",
            'anger': "Kamu sedang marah dan kesal",
            'fear': "Kamu sedang takut dan cemas",
            'trust': "Kamu percaya padanya",
            'love': "Kamu sedang jatuh cinta",
            'lust': "Kamu sedang horny dan bergairah",
            'jealousy': "Kamu sedang cemburu",
            'anxiety': "Kamu sedang gelisah",
            'attachment': "Kamu merasa terikat",
            'loneliness': "Kamu merasa kesepian",
            'curiosity': "Kamu penasaran",
            'nostalgia': "Kamu sedang bernostalgia",
            'passion': "Kamu penuh gairah",
            'longing': "Kamu merindukannya"
        }
        
        prompt = base_prompts.get(dominant, "Kamu dalam keadaan normal")
        
        if intensity > 0.7:
            prompt += " dengan intensitas yang sangat kuat"
        elif intensity < 0.3:
            prompt += " dengan intensitas yang ringan"
        
        # Tambah info emosi aktif lainnya
        active = state.get('active_emotions', [])
        if len(active) > 1:
            others = [e for e in active if e != dominant][:2]
            if others:
                prompt += f". Juga merasa {', '.join(others)}"
        
        return prompt
