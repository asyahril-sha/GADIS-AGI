"""
EMOTION ENGINE - Amygdala digital
Memproses emosi dengan interaksi kompleks
"""

import numpy as np
from datetime import datetime
from typing import Dict, Optional, List, Tuple
from core.emotional_vector import EmotionalVector

class EmotionEngine:
    """
    Mesin emosi dengan 32 dimensi dan interaksi - Amygdala digital
    
    Fitur:
    - Memproses event dan mengupdate emosi
    - Interaksi antar emosi (joy reduces sadness, dll)
    - Decay emosi seiring waktu
    - Emotional memory
    - Personality baseline
    """
    
    def __init__(self, personality: np.ndarray):
        """
        Inisialisasi emotion engine dengan personality
        
        Args:
            personality: Array 16 dimensi nilai kepribadian
        """
        self.personality = personality
        self.current = EmotionalVector()
        self.baseline = self._create_baseline()
        self.history: List[Dict] = []
        
        # Interaksi antar emosi (e1, e2, strength)
        # e1 mempengaruhi e2 dengan kekuatan strength
        self.interactions = [
            (EmotionalVector.JOY, EmotionalVector.SADNESS, -0.3),      # Joy reduces sadness
            (EmotionalVector.SADNESS, EmotionalVector.JOY, -0.2),      # Sadness reduces joy
            (EmotionalVector.LOVE, EmotionalVector.LUST, 0.2),          # Love increases lust
            (EmotionalVector.LUST, EmotionalVector.PASSION, 0.3),       # Lust increases passion
            (EmotionalVector.ANXIETY, EmotionalVector.LONELINESS, 0.3), # Anxiety increases loneliness
            (EmotionalVector.LONELINESS, EmotionalVector.ANXIETY, 0.2), # Loneliness increases anxiety
            (EmotionalVector.GUILT, EmotionalVector.JOY, -0.2),         # Guilt reduces joy
            (EmotionalVector.NOSTALGIA, EmotionalVector.SADNESS, 0.2),  # Nostalgia increases sadness
            (EmotionalVector.NOSTALGIA, EmotionalVector.LOVE, 0.1),     # Nostalgia increases love
            (EmotionalVector.LONGING, EmotionalVector.ANXIETY, 0.2),    # Longing increases anxiety
            (EmotionalVector.ANGER, EmotionalVector.FEAR, 0.1),         # Anger increases fear
            (EmotionalVector.TRUST, EmotionalVector.LOVE, 0.1),         # Trust increases love
            (EmotionalVector.JEALOUSY, EmotionalVector.ANGER, 0.2),     # Jealousy increases anger
            (EmotionalVector.ATTACHMENT, EmotionalVector.ANXIETY, 0.1), # Attachment increases anxiety
            (EmotionalVector.HOPE, EmotionalVector.JOY, 0.2),           # Hope increases joy
            (EmotionalVector.DESPAIR, EmotionalVector.SADNESS, 0.3),    # Despair increases sadness
            (EmotionalVector.EXCITEMENT, EmotionalVector.LUST, 0.2),    # Excitement increases lust
            (EmotionalVector.RELIEF, EmotionalVector.ANXIETY, -0.3),    # Relief reduces anxiety
        ]
    
    def _create_baseline(self) -> EmotionalVector:
        """
        Buat baseline dari personality
        
        Returns:
            EmotionalVector baseline
        """
        baseline = EmotionalVector()
        
        # Neuroticism -> anxiety, fear, sadness
        baseline.anxiety = self.personality[0] * 0.3
        baseline.fear = self.personality[0] * 0.2
        baseline.sadness = self.personality[0] * 0.1
        
        # Extraversion -> joy, excitement
        baseline.joy = self.personality[1] * 0.3
        baseline.v[EmotionalVector.EXCITEMENT] = self.personality[1] * 0.3
        
        # Openness -> curiosity
        baseline.curiosity = self.personality[2] * 0.4
        
        # Agreeableness -> trust, love
        baseline.trust = self.personality[3] * 0.3
        baseline.love = self.personality[3] * 0.2
        
        # Conscientiousness -> control (boredom lower)
        baseline.boredom = (1 - self.personality[4]) * 0.2
        
        # Emotional depth -> baseline emotions higher
        if self.personality[5] > 0.5:
            baseline.joy *= 1.2
            baseline.sadness *= 1.2
            baseline.anger *= 1.1
        
        # Attachment style
        if self.personality[6] > 0.6:  # Anxious attachment
            baseline.attachment = 0.3
            baseline.anxiety += 0.1
        else:  # Avoidant attachment
            baseline.attachment = 0.1
            baseline.independence = 0.3
        
        # Sexual drive
        baseline.lust = self.personality[7] * 0.4
        baseline.passion = self.personality[7] * 0.3
        
        # Romanticism
        baseline.love += self.personality[8] * 0.2
        baseline.tenderness = self.personality[8] * 0.3
        
        # Possessiveness
        baseline.jealousy = self.personality[9] * 0.2
        
        # Jealousy prone
        baseline.jealousy += self.personality[10] * 0.2
        
        # Empathy
        if self.personality[12] > 0.6:
            baseline.trust += 0.2
            baseline.love += 0.1
        
        # Playfulness
        if self.personality[14] > 0.6:
            baseline.joy += 0.2
            baseline.v[EmotionalVector.PLAYFUL] = 0.3
        
        baseline.normalize()
        return baseline
    
    def process_event(self, event_type: str, intensity: float = 0.5, 
                     context: Dict = None) -> Dict:
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
            "position_change": EmotionalVector(),
            "breakup": EmotionalVector(),
            "reunion": EmotionalVector(),
            "climax": EmotionalVector(),
            "aftercare": EmotionalVector()
        }
        
        # ===== ROMANTIC =====
        effects["romantic"].love = 0.4
        effects["romantic"].joy = 0.3
        effects["romantic"].trust = 0.2
        effects["romantic"].tenderness = 0.3
        effects["romantic"].hope = 0.2
        
        # ===== SEXUAL =====
        effects["sexual"].lust = 0.5
        effects["sexual"].passion = 0.4
        effects["sexual"].v[EmotionalVector.EXCITEMENT] = 0.3
        effects["sexual"].love = 0.2
        
        # ===== CONFLICT =====
        effects["conflict"].anger = 0.4
        effects["conflict"].fear = 0.2
        effects["conflict"].sadness = 0.2
        effects["conflict"].frustration = 0.3
        effects["conflict"].trust = -0.2
        
        # ===== COMPLIMENT =====
        effects["compliment"].joy = 0.3
        effects["compliment"].v[EmotionalVector.PRIDE] = 0.2
        effects["compliment"].love = 0.1
        effects["compliment"].trust = 0.1
        
        # ===== IGNORE =====
        effects["ignore"].sadness = 0.3
        effects["ignore"].loneliness = 0.3
        effects["ignore"].anxiety = 0.2
        effects["ignore"].trust = -0.1
        
        # ===== MEMORY HAPPY =====
        effects["memory_happy"].joy = 0.2
        effects["memory_happy"].nostalgia = 0.3
        effects["memory_happy"].love = 0.1
        effects["memory_happy"].gratitude = 0.2
        
        # ===== MEMORY SAD =====
        effects["memory_sad"].sadness = 0.2
        effects["memory_sad"].nostalgia = 0.3
        effects["memory_sad"].longing = 0.2
        effects["memory_sad"].despair = 0.1
        
        # ===== JEALOUSY =====
        effects["jealousy"].jealousy = 0.5
        effects["jealousy"].anger = 0.2
        effects["jealousy"].anxiety = 0.2
        effects["jealousy"].fear = 0.1
        effects["jealousy"].trust = -0.2
        
        # ===== PUBLIC SEX =====
        effects["public_sex"].v[EmotionalVector.EXCITEMENT] = 0.5
        effects["public_sex"].lust = 0.4
        effects["public_sex"].fear = 0.2  # Takut ketahuan
        effects["public_sex"].passion = 0.3
        
        # ===== POSITION CHANGE =====
        effects["position_change"].v[EmotionalVector.EXCITEMENT] = 0.2
        effects["position_change"].curiosity = 0.3
        effects["position_change"].lust = 0.2
        effects["position_change"].joy = 0.1
        
        # ===== BREAKUP =====
        effects["breakup"].sadness = 0.5
        effects["breakup"].despair = 0.4
        effects["breakup"].loneliness = 0.4
        effects["breakup"].anger = 0.2
        effects["breakup"].trust = -0.4
        effects["breakup"].love = -0.3
        
        # ===== REUNION =====
        effects["reunion"].joy = 0.5
        effects["reunion"].love = 0.4
        effects["reunion"].relief = 0.3
        effects["reunion"].gratitude = 0.2
        
        # ===== CLIMAX =====
        effects["climax"].lust = -0.3  # Turun setelah climax
        effects["climax"].passion = -0.2
        effects["climax"].relief = 0.4
        effects["climax"].joy = 0.3
        effects["climax"].love = 0.2
        
        # ===== AFTERCARE =====
        effects["aftercare"].love = 0.2
        effects["aftercare"].tenderness = 0.4
        effects["aftercare"].gratitude = 0.3
        effects["aftercare"].trust = 0.2
        effects["aftercare"].attachment = 0.1
        
        # Apply effect jika ada
        if event_type in effects:
            effect = effects[event_type] * intensity
            self.current = self.current + effect
        
        # Tambahkan baseline (10%)
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
            'context': context,
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
            # Pengaruh e1 ke e2
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
        # Decay rate: 10% per jam, max 50%
        decay_factor = 1 - min(0.5, 0.1 * hours)
        
        # Current emotion decay
        self.current = self.current * decay_factor
        
        # But baseline tetap
        baseline_contribution = self.baseline * 0.1
        self.current = self.current + baseline_contribution
        
        self.current.normalize()
    
    def get_state(self) -> Dict:
        """
        Dapatkan state emosi saat ini
        
        Returns:
            Dictionary berisi state emosi
        """
        dominant, intensity = self.current.dominant()
        return {
            'vector': self.current.to_dict(),
            'dominant': dominant,
            'intensity': intensity,
            'arousal': self.current.get_arousal(),
            'valence': self.current.get_valence(),
            'active_emotions': self.current.get_active_emotions(),
            'complexity': len(self.current.get_active_emotions(0.2)) / 32
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
        if any(word in msg_lower for word in ['sayang', 'cinta', 'love', '❤️', '💕']):
            return self.process_event("romantic", 0.4)
        
        elif any(word in msg_lower for word in ['horny', 'nafsu', 'seksi', 'hot', '🔥']):
            return self.process_event("sexual", 0.5)
        
        elif any(word in msg_lower for word in ['marah', 'kesal', 'sakit', 'kecewa']):
            return self.process_event("conflict", 0.4)
        
        elif any(word in msg_lower for word in ['kangen', 'rindu', 'miss']):
            return self.process_event("longing", 0.3)
        
        elif any(word in msg_lower for word in ['cantik', 'ganteng', 'baik', 'hebat']):
            return self.process_event("compliment", 0.2)
        
        elif any(word in msg_lower for word in ['ingat', 'dulu', 'masa lalu', 'kenangan']):
            # Random happy or sad memory
            if random.random() < 0.5:
                return self.process_event("memory_happy", 0.3)
            else:
                return self.process_event("memory_sad", 0.3)
        
        elif any(word in msg_lower for word in ['cemburu', 'siapa', 'orang lain']):
            return self.process_event("jealousy", 0.4)
        
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
        arousal = state['arousal']
        valence = state['valence']
        
        # Base prompt berdasarkan emosi dominan
        prompts = {
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
            'longing': "Kamu merindukannya",
            'hope': "Kamu penuh harapan",
            'despair': "Kamu putus asa",
            'gratitude': "Kamu bersyukur",
            'excitement': "Kamu sangat excited"
        }
        
        prompt = prompts.get(dominant, "Kamu dalam keadaan normal")
        
        # Tambah intensitas
        if intensity > 0.7:
            prompt += " dengan intensitas yang sangat kuat"
        elif intensity < 0.3:
            prompt += " dengan intensitas yang ringan"
        
        # Tambah arousal
        if arousal > 0.7:
            prompt += ", sangat bergairah"
        elif arousal < 0.3:
            prompt += ", tenang"
        
        # Tambah valensi
        if valence > 0.3:
            prompt += ", perasaan positif"
        elif valence < -0.3:
            prompt += ", perasaan negatif"
        
        # Tambah info emosi aktif lainnya
        active = state.get('active_emotions', [])
        if len(active) > 1:
            others = [e for e in active if e != dominant][:3]
            if others:
                prompt += f". Juga merasa {', '.join(others)}"
        
        return prompt
    
    def get_emotion_summary(self) -> str:
        """
        Dapatkan ringkasan emosi untuk display
        
        Returns:
            String ringkasan emosi
        """
        state = self.get_state()
        dominant = state['dominant']
        intensity = state['intensity']
        active = state['active_emotions']
        
        # Emoji mapping
        emoji_map = {
            'joy': '😊', 'sadness': '😢', 'anger': '😠', 'fear': '😨',
            'trust': '🤝', 'love': '❤️', 'lust': '🔥', 'jealousy': '💢',
            'anxiety': '😰', 'attachment': '🫂', 'loneliness': '🕊️',
            'curiosity': '🤔', 'nostalgia': '🕰️', 'passion': '💋',
            'longing': '🥺', 'hope': '✨', 'despair': '💔'
        }
        
        emoji = emoji_map.get(dominant, '😐')
        
        # Progress bar untuk intensitas
        bar_length = 10
        filled = int(intensity * bar_length)
        bar = "█" * filled + "░" * (bar_length - filled)
        
        summary = f"{emoji} **{dominant.title()}** {bar} {int(intensity*100)}%\n"
        
        if len(active) > 1:
            others = [f"{emoji_map.get(e, '')} {e}" for e in active if e != dominant][:3]
            summary += f"Juga: {', '.join(others)}"
        
        return summary
