"""
EMOTIONAL VECTOR - 32 DIMENSI EMOSI
Dengan interaksi antar emosi
"""

import numpy as np
from typing import Dict, Tuple, List

class EmotionalVector:
    """
    Vektor emosi 32 dimensi - representasi kompleks emosi manusia
    """
    
    # Indeks emosi (0-31)
    JOY = 0
    SADNESS = 1
    ANGER = 2
    FEAR = 3
    TRUST = 4
    DISGUST = 5
    ANTICIPATION = 6
    SURPRISE = 7
    LOVE = 8
    LUST = 9
    JEALOUSY = 10
    ANXIETY = 11
    ATTACHMENT = 12
    LONELINESS = 13
    CURIOSITY = 14
    BOREDOM = 15
    GUILT = 16
    SHAME = 17
    PRIDE = 18
    GRATITUDE = 19
    HOPE = 20
    DESPAIR = 21
    NOSTALGIA = 22
    AWE = 23
    CONTEMPT = 24
    EMBARRASSMENT = 25
    EXCITEMENT = 26
    RELIEF = 27
    FRUSTRATION = 28
    LONGING = 29
    TENDERNESS = 30
    PASSION = 31
    
    # Nama-nama emosi untuk display
    EMOTION_NAMES = [
        'joy', 'sadness', 'anger', 'fear', 'trust', 'disgust',
        'anticipation', 'surprise', 'love', 'lust', 'jealousy',
        'anxiety', 'attachment', 'loneliness', 'curiosity', 'boredom',
        'guilt', 'shame', 'pride', 'gratitude', 'hope', 'despair',
        'nostalgia', 'awe', 'contempt', 'embarrassment', 'excitement',
        'relief', 'frustration', 'longing', 'tenderness', 'passion'
    ]
    
    def __init__(self, values: np.ndarray = None):
        """Inisialisasi vektor emosi"""
        if values is None:
            self.v = np.zeros(32, dtype=np.float32)
        else:
            self.v = np.array(values, dtype=np.float32)
    
    def __getitem__(self, idx: int) -> float:
        return float(self.v[idx])
    
    def __setitem__(self, idx: int, val: float):
        self.v[idx] = max(0.0, min(1.0, float(val)))
    
    def __add__(self, other: 'EmotionalVector') -> 'EmotionalVector':
        return EmotionalVector(self.v + other.v)
    
    def __mul__(self, scalar: float) -> 'EmotionalVector':
        return EmotionalVector(self.v * scalar)
    
    # ===== PROPERTIES UNTUK EMOSI UTAMA =====
    
    @property
    def joy(self) -> float:
        return float(self.v[self.JOY])
    
    @joy.setter
    def joy(self, val: float):
        self.v[self.JOY] = max(0.0, min(1.0, float(val)))
    
    @property
    def sadness(self) -> float:
        return float(self.v[self.SADNESS])
    
    @sadness.setter
    def sadness(self, val: float):
        self.v[self.SADNESS] = max(0.0, min(1.0, float(val)))
    
    @property
    def anger(self) -> float:
        return float(self.v[self.ANGER])
    
    @anger.setter
    def anger(self, val: float):
        self.v[self.ANGER] = max(0.0, min(1.0, float(val)))
    
    @property
    def fear(self) -> float:
        return float(self.v[self.FEAR])
    
    @fear.setter
    def fear(self, val: float):
        self.v[self.FEAR] = max(0.0, min(1.0, float(val)))
    
    @property
    def trust(self) -> float:
        return float(self.v[self.TRUST])
    
    @trust.setter
    def trust(self, val: float):
        self.v[self.TRUST] = max(0.0, min(1.0, float(val)))
    
    @property
    def love(self) -> float:
        return float(self.v[self.LOVE])
    
    @love.setter
    def love(self, val: float):
        self.v[self.LOVE] = max(0.0, min(1.0, float(val)))
    
    @property
    def lust(self) -> float:
        return float(self.v[self.LUST])
    
    @lust.setter
    def lust(self, val: float):
        self.v[self.LUST] = max(0.0, min(1.0, float(val)))
    
    @property
    def jealousy(self) -> float:
        return float(self.v[self.JEALOUSY])
    
    @jealousy.setter
    def jealousy(self, val: float):
        self.v[self.JEALOUSY] = max(0.0, min(1.0, float(val)))
    
    @property
    def anxiety(self) -> float:
        return float(self.v[self.ANXIETY])
    
    @anxiety.setter
    def anxiety(self, val: float):
        self.v[self.ANXIETY] = max(0.0, min(1.0, float(val)))
    
    @property
    def attachment(self) -> float:
        return float(self.v[self.ATTACHMENT])
    
    @attachment.setter
    def attachment(self, val: float):
        self.v[self.ATTACHMENT] = max(0.0, min(1.0, float(val)))
    
    @property
    def loneliness(self) -> float:
        return float(self.v[self.LONELINESS])
    
    @loneliness.setter
    def loneliness(self, val: float):
        self.v[self.LONELINESS] = max(0.0, min(1.0, float(val)))
    
    @property
    def curiosity(self) -> float:
        return float(self.v[self.CURIOSITY])
    
    @curiosity.setter
    def curiosity(self, val: float):
        self.v[self.CURIOSITY] = max(0.0, min(1.0, float(val)))
    
    @property
    def nostalgia(self) -> float:
        return float(self.v[self.NOSTALGIA])
    
    @nostalgia.setter
    def nostalgia(self, val: float):
        self.v[self.NOSTALGIA] = max(0.0, min(1.0, float(val)))
    
    @property
    def passion(self) -> float:
        return float(self.v[self.PASSION])
    
    @passion.setter
    def passion(self, val: float):
        self.v[self.PASSION] = max(0.0, min(1.0, float(val)))
    
    @property
    def longing(self) -> float:
        return float(self.v[self.LONGING])
    
    @longing.setter
    def longing(self, val: float):
        self.v[self.LONGING] = max(0.0, min(1.0, float(val)))
    
    # ===== METHODS =====
    
    def normalize(self, max_val: float = 1.0):
        """Normalisasi semua nilai agar tidak melebihi max_val"""
        self.v = np.clip(self.v, 0, max_val)
    
    def dominant(self) -> Tuple[str, float]:
        """Dapatkan emosi dominan"""
        idx = int(np.argmax(self.v))
        return self.EMOTION_NAMES[idx], float(self.v[idx])
    
    def to_dict(self) -> Dict[str, float]:
        """Konversi ke dictionary"""
        return {name: float(self.v[i]) for i, name in enumerate(self.EMOTION_NAMES)}
    
    def copy(self) -> 'EmotionalVector':
        """Buat copy vektor"""
        return EmotionalVector(self.v.copy())
    
    def get_active_emotions(self, threshold: float = 0.3) -> List[str]:
        """Dapatkan emosi yang aktif di atas threshold"""
        return [name for i, name in enumerate(self.EMOTION_NAMES) if self.v[i] > threshold]
    
    def get_intensity(self) -> float:
        """Dapatkan intensitas emosi total"""
        return float(np.mean(self.v))
    
    def get_arousal(self) -> float:
        """Dapatkan tingkat gairah (arousal)"""
        high_arousal = [
            self.v[self.LUST],
            self.v[self.ANGER],
            self.v[self.FEAR],
            self.v[self.ANXIETY],
            self.v[self.EXCITEMENT],
            self.v[self.PASSION]
        ]
        return float(min(1.0, sum(high_arousal) / 3))
