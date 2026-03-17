"""
CORE PACKAGE - Inisialisasi semua core systems
"""

from core.emotional_vector import EmotionalVector
from core.personality_genome import PersonalityGenome
from core.emotion_engine import EmotionEngine
from core.consciousness import Consciousness
from core.memory_system import MemorySystem, MemoryTrace

__all__ = [
    'EmotionalVector',
    'PersonalityGenome',
    'EmotionEngine',
    'Consciousness',
    'MemorySystem',
    'MemoryTrace'
]
