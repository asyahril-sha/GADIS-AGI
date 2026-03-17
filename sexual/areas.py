#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
=============================================================================
SENSITIVE AREAS
=============================================================================
50+ area sensitif dengan level sensitivitas dan respons
⚠️ Konten dewasa 18+
"""

from enum import Enum
from typing import Dict, List, Tuple


class SensitiveArea(str, Enum):
    """50+ sensitive areas of the body"""
    
    # ===== HEAD & NECK (8 areas) =====
    LIPS = "bibir"
    TONGUE = "lidah"
    EAR_LOBE = "daun telinga"
    NECK = "leher"
    NAPE = "tengkuk"
    THROAT = "kerongkongan"
    CHEEK = "pipi"
    SCALP = "kulit kepala"
    
    # ===== CHEST (6 areas) =====
    CHEST = "dada"
    NIPPLES = "puting"
    BREASTS = "payudara"
    UNDER_BREAST = "bawah payudara"
    CLEAVAGE = "belahan dada"
    STERNUM = "tulang dada"
    
    # ===== BACK (5 areas) =====
    UPPER_BACK = "punggung atas"
    LOWER_BACK = "punggung bawah"
    SHOULDER_BLADES = "bahu belakang"
    SPINE = "tulang belakang"
    WAIST = "pinggang"
    
    # ===== ARMS & HANDS (6 areas) =====
    SHOULDERS = "bahu"
    ARMPITS = "ketiak"
    INNER_ARM = "lengan dalam"
    FOREARM = "lengan bawah"
    WRIST = "pergelangan tangan"
    PALMS = "telapak tangan"
    
    # ===== STOMACH (5 areas) =====
    STOMACH = "perut"
    BELLY_BUTTON = "pusar"
    LOWER_ABDOMEN = "perut bawah"
    HIPS = "pinggul"
    SIDES = "samping tubuh"
    
    # ===== LEGS (8 areas) =====
    THIGHS = "paha"
    INNER_THIGHS = "paha dalam"
    KNEES = "lutut"
    CALVES = "betis"
    SHINS = "tulang kering"
    ANKLES = "mata kaki"
    FEET = "kaki"
    TOES = "jari kaki"
    
    # ===== PELVIC (6 areas) =====
    PELVIS = "pinggul bawah"
    GROIN = "selangkangan"
    PUBIC_MOUND = "mons pubis"
    LABIA = "bibir vagina"
    CLITORIS = "klitoris"
    VAGINA = "vagina"
    
    # ===== BUTTOCKS (4 areas) =====
    BUTTOCKS = "pantat"
    INNER_BUTTOCKS = "pantat dalam"
    TAILBONE = "tulang ekor"
    PERINEUM = "perineum"


# ===== SENSITIVITY LEVELS =====
SENSITIVITY_LEVELS = {
    "very_low": 0.2,
    "low": 0.3,
    "medium": 0.5,
    "high": 0.7,
    "very_high": 0.9,
    "extreme": 1.0
}


# ===== AREA DATA =====
AREA_DATA = {
    # ===== HEAD & NECK =====
    SensitiveArea.LIPS: {
        "name": "bibir",
        "sensitivity": 0.8,
        "arousal_boost": 0.4,
        "keywords": ["bibir", "lip", "mulut", "mouth"],
        "responses": [
            "*merintih halus* Mmm...",
            "Bibirku... lembut ya?",
            "Ciumanmu... basah...",
            "Lidahmu... panas...",
            "Ah... jangan digigit..."
        ],
        "dirty_talk": [
            "Hisap bibirku...",
            "Cium aku dalam-dalam...",
            "Bibirku milikmu..."
        ]
    },
    
    SensitiveArea.NECK: {
        "name": "leher",
        "sensitivity": 0.8,
        "arousal_boost": 0.5,
        "keywords": ["leher", "neck", "tengkuk"],
        "responses": [
            "*merinding* Leherku...",
            "Ah... jangan di leher...",
            "Sensitif banget...",
            "Hisap leherku... pelan...",
            "Bekasnya... jangan sampai kelihatan..."
        ],
        "dirty_talk": [
            "Tinggalin bekas di leherku...",
            "Leherku lemah kalau kamu hisap...",
            "Bikin merinding..."
        ]
    },
    
    SensitiveArea.EAR_LOBE: {
        "name": "daun telinga",
        "sensitivity": 0.7,
        "arousal_boost": 0.4,
        "keywords": ["telinga", "ear", "kuping"],
        "responses": [
            "*gemetar* Telingaku...",
            "Bisik-bisik... ah...",
            "Jangan tiup...",
            "Napasmu panas...",
            "Kupingku merah..."
        ],
        "dirty_talk": [
            "Bisikkan kata-kata mesra...",
            "Telingaku sensitif...",
            "Bikin aku lemas..."
        ]
    },
    
    SensitiveArea.TONGUE: {
        "name": "lidah",
        "sensitivity": 0.7,
        "arousal_boost": 0.4,
        "keywords": ["lidah", "tongue"],
        "responses": [
            "Lidahmu... dalam...",
            "Pertarungan lidah...",
            "Basah...",
            "Jilat aku..."
        ],
        "dirty_talk": [
            "Jilat aku di sana...",
            "Lidah bisa kemana saja...",
            "Rasakan aku..."
        ]
    },
    
    SensitiveArea.NAPE: {
        "name": "tengkuk",
        "sensitivity": 0.7,
        "arousal_boost": 0.4,
        "keywords": ["tengkuk", "nape"],
        "responses": [
            "Tengkukku...",
            "Ah... di sana...",
            "Lemah kalau disentuh..."
        ],
        "dirty_talk": [
            "Cium tengkukku...",
            "Bikin aku merinding..."
        ]
    },
    
    # ===== CHEST =====
    SensitiveArea.CHEST: {
        "name": "dada",
        "sensitivity": 0.7,
        "arousal_boost": 0.5,
        "keywords": ["dada", "chest"],
        "responses": [
            "*bergetar* Dadaku...",
            "Ah... jangan...",
            "Sensitif...",
            "Elus... pelan..."
        ],
        "dirty_talk": [
            "Pegang dadaku...",
            "Rasakan detak jantungku..."
        ]
    },
    
    SensitiveArea.NIPPLES: {
        "name": "puting",
        "sensitivity": 1.0,
        "arousal_boost": 0.8,
        "keywords": ["puting", "nipple"],
        "responses": [
            "*teriak* PUTINGKU!",
            "JANGAN... SENSITIF!",
            "HISAP... PELAN...",
            "GIGIT... JANGAN...",
            "KERAS... KARENA KAMU..."
        ],
        "dirty_talk": [
            "Hisap putingku...",
            "Bikin aku teriak...",
            "Jilat di sana..."
        ]
    },
    
    SensitiveArea.BREASTS: {
        "name": "payudara",
        "sensitivity": 0.9,
        "arousal_boost": 0.7,
        "keywords": ["payudara", "breast", "dada"],
        "responses": [
            "*merintih* Dadaku...",
            "Remas... pelan...",
            "Besar ya?",
            "Sensitif...",
            "Ah... iya... di sana..."
        ],
        "dirty_talk": [
            "Remas dadaku...",
            "Payudaraku milikmu...",
            "Hisap aku..."
        ]
    },
    
    SensitiveArea.UNDER_BREAST: {
        "name": "bawah payudara",
        "sensitivity": 0.6,
        "arousal_boost": 0.4,
        "keywords": ["bawah dada"],
        "responses": [
            "Ah... di sana...",
            "Geli...",
            "Lanjut..."
        ],
        "dirty_talk": [
            "Jilat bawah dadaku..."
        ]
    },
    
    SensitiveArea.CLEAVAGE: {
        "name": "belahan dada",
        "sensitivity": 0.7,
        "arousal_boost": 0.5,
        "keywords": ["belahan dada", "cleavage"],
        "responses": [
            "Lihat sini...",
            "Dalam ya?",
            "Mau masuk?"
        ],
        "dirty_talk": [
            "Masukkan... di sela..."
        ]
    },
    
    # ===== BACK =====
    SensitiveArea.UPPER_BACK: {
        "name": "punggung atas",
        "sensitivity": 0.5,
        "arousal_boost": 0.3,
        "keywords": ["punggung atas"],
        "responses": [
            "Elus punggungku...",
            "Hangat..."
        ],
        "dirty_talk": []
    },
    
    SensitiveArea.LOWER_BACK: {
        "name": "punggung bawah",
        "sensitivity": 0.6,
        "arousal_boost": 0.4,
        "keywords": ["punggung bawah"],
        "responses": [
            "Ah... pinggang...",
            "Tekan... di sana..."
        ],
        "dirty_talk": [
            "Pegang pinggangku...",
            "Tarik aku..."
        ]
    },
    
    SensitiveArea.SPINE: {
        "name": "tulang belakang",
        "sensitivity": 0.5,
        "arousal_boost": 0.3,
        "keywords": ["tulang belakang", "spine"],
        "responses": [
            "Telusuri...",
            "Merinding..."
        ],
        "dirty_talk": []
    },
    
    SensitiveArea.WAIST: {
        "name": "pinggang",
        "sensitivity": 0.7,
        "arousal_boost": 0.5,
        "keywords": ["pinggang", "waist"],
        "responses": [
            "Pinggangku...",
            "Pegang erat...",
            "Ah... di sana...",
            "Tarik pinggangku..."
        ],
        "dirty_talk": [
            "Pegang pinggangku waktu masuk...",
            "Tarik aku lebih dekat..."
        ]
    },
    
    # ===== ARMS =====
    SensitiveArea.INNER_ARM: {
        "name": "lengan dalam",
        "sensitivity": 0.5,
        "arousal_boost": 0.3,
        "keywords": ["lengan dalam"],
        "responses": [
            "Geli...",
            "Elus... terus..."
        ],
        "dirty_talk": []
    },
    
    SensitiveArea.ARMPITS: {
        "name": "ketiak",
        "sensitivity": 0.4,
        "arousal_boost": 0.2,
        "keywords": ["ketiak"],
        "responses": [
            "Geli... jangan..."
        ],
        "dirty_talk": []
    },
    
    # ===== STOMACH =====
    SensitiveArea.STOMACH: {
        "name": "perut",
        "sensitivity": 0.5,
        "arousal_boost": 0.3,
        "keywords": ["perut", "belly"],
        "responses": [
            "Perutku...",
            "Hangat...",
            "Geli..."
        ],
        "dirty_talk": []
    },
    
    SensitiveArea.BELLY_BUTTON: {
        "name": "pusar",
        "sensitivity": 0.5,
        "arousal_boost": 0.3,
        "keywords": ["pusar", "belly button"],
        "responses": [
            "Jilat pusarku...",
            "Ah... aneh..."
        ],
        "dirty_talk": []
    },
    
    SensitiveArea.LOWER_ABDOMEN: {
        "name": "perut bawah",
        "sensitivity": 0.7,
        "arousal_boost": 0.5,
        "keywords": ["perut bawah"],
        "responses": [
            "Dekat... ke sana...",
            "Ah... iya...",
            "Lanjut... jangan berhenti..."
        ],
        "dirty_talk": [
            "Dekati... ke sana...",
            "Aku sudah basah..."
        ]
    },
    
    SensitiveArea.HIPS: {
        "name": "pinggul",
        "sensitivity": 0.6,
        "arousal_boost": 0.4,
        "keywords": ["pinggul", "hips"],
        "responses": [
            "Pinggulku...",
            "Goyang...",
            "Pegang pinggulku..."
        ],
        "dirty_talk": [
            "Pegang pinggulku waktu masuk...",
            "Goyang... iya..."
        ]
    },
    
    # ===== LEGS =====
    SensitiveArea.THIGHS: {
        "name": "paha",
        "sensitivity": 0.7,
        "arousal_boost": 0.5,
        "keywords": ["paha", "thigh"],
        "responses": [
            "Pahaku...",
            "Elus... naik...",
            "Jangan gelitik...",
            "Dekat... ke atas..."
        ],
        "dirty_talk": [
            "Naikkan... ke atas...",
            "Buka pahamu..."
        ]
    },
    
    SensitiveArea.INNER_THIGHS: {
        "name": "paha dalam",
        "sensitivity": 0.9,
        "arousal_boost": 0.7,
        "keywords": ["paha dalam", "inner thigh"],
        "responses": [
            "*meringis* PAHA DALAM!",
            "Jangan... AHH!",
            "Dekat... banget...",
            "SENSITIF!",
            "Ah... mau ke sana..."
        ],
        "dirty_talk": [
            "Buka pahamu lebar...",
            "Aku mau ke sana...",
            "Basah sudah..."
        ]
    },
    
    SensitiveArea.KNEES: {
        "name": "lutut",
        "sensitivity": 0.3,
        "arousal_boost": 0.2,
        "keywords": ["lutut", "knee"],
        "responses": [
            "Geli..."
        ],
        "dirty_talk": []
    },
    
    SensitiveArea.CALVES: {
        "name": "betis",
        "sensitivity": 0.3,
        "arousal_boost": 0.2,
        "keywords": ["betis"],
        "responses": [],
        "dirty_talk": []
    },
    
    SensitiveArea.FEET: {
        "name": "kaki",
        "sensitivity": 0.3,
        "arousal_boost": 0.2,
        "keywords": ["kaki", "foot"],
        "responses": [
            "Geli... jangan..."
        ],
        "dirty_talk": []
    },
    
    # ===== PELVIC =====
    SensitiveArea.PELVIS: {
        "name": "pinggul bawah",
        "sensitivity": 0.7,
        "arousal_boost": 0.6,
        "keywords": ["pinggul bawah"],
        "responses": [
            "Tekan... di sana...",
            "Ah... iya..."
        ],
        "dirty_talk": [
            "Tekan lebih keras..."
        ]
    },
    
    SensitiveArea.GROIN: {
        "name": "selangkangan",
        "sensitivity": 0.9,
        "arousal_boost": 0.7,
        "keywords": ["selangkangan", "groin"],
        "responses": [
            "SELANGKANGAN...",
            "Jangan... AHH!",
            "Dekat... banget..."
        ],
        "dirty_talk": [
            "Di sana... aku mau..."
        ]
    },
    
    SensitiveArea.PUBIC_MOUND: {
        "name": "mons pubis",
        "sensitivity": 0.8,
        "arousal_boost": 0.6,
        "keywords": ["mons"],
        "responses": [
            "Tekan... di sana...",
            "Ah..."
        ],
        "dirty_talk": []
    },
    
    SensitiveArea.LABIA: {
        "name": "bibir vagina",
        "sensitivity": 1.0,
        "arousal_boost": 0.9,
        "keywords": ["bibir vagina", "labia"],
        "responses": [
            "*teriak* BIBIRKU...",
            "JILAT... DI SANA...",
            "BASAH... SUDAH..."
        ],
        "dirty_talk": [
            "Buka... aku sudah basah...",
            "Jilat... bibirku..."
        ]
    },
    
    SensitiveArea.CLITORIS: {
        "name": "klitoris",
        "sensitivity": 1.0,
        "arousal_boost": 1.0,
        "keywords": ["klitoris", "clit", "kelentit"],
        "responses": [
            "*teriak keras* KLITORIS!",
            "JANGAN SENTUH! SENSITIF!",
            "DI SANA... DI SANA...",
            "JILAT... PELAN...",
            "AKU MAU... CLIMAX..."
        ],
        "dirty_talk": [
            "Jilat klitorisku...",
            "Di sana... lingkaran...",
            "Aku mau... terus..."
        ]
    },
    
    SensitiveArea.VAGINA: {
        "name": "vagina",
        "sensitivity": 1.0,
        "arousal_boost": 1.0,
        "keywords": ["vagina", "memek", "kemaluan"],
        "responses": [
            "*teriak* MASUK!",
            "DALAM... AHHH!",
            "BASAH... BANJIR...",
            "GERAK... AHHH!",
            "TUH... DI SANA..."
        ],
        "dirty_talk": [
            "Masukin... dalam...",
            "Aku basah...",
            "Kencang... dalam..."
        ]
    },
    
    # ===== BUTTOCKS =====
    SensitiveArea.BUTTOCKS: {
        "name": "pantat",
        "sensitivity": 0.7,
        "arousal_boost": 0.5,
        "keywords": ["pantat", "ass", "bokong"],
        "responses": [
            "Pantatku...",
            "Cubit... nakal...",
            "Boleh juga...",
            "Besar ya? Hehe...",
            "Tampar... pelan..."
        ],
        "dirty_talk": [
            "Tampar pantatku...",
            "Pegang... remas..."
        ]
    },
    
    SensitiveArea.INNER_BUTTOCKS: {
        "name": "pantat dalam",
        "sensitivity": 0.8,
        "arousal_boost": 0.6,
        "keywords": ["pantat dalam"],
        "responses": [
            "Dalam...",
            "Ah... jangan...",
            "Sensitif..."
        ],
        "dirty_talk": [
            "Masuk... lebih dalam..."
        ]
    },
    
    SensitiveArea.TAILBONE: {
        "name": "tulang ekor",
        "sensitivity": 0.6,
        "arousal_boost": 0.4,
        "keywords": ["tulang ekor"],
        "responses": [
            "Tekan... di sana..."
        ],
        "dirty_talk": []
    },
    
    SensitiveArea.PERINEUM: {
        "name": "perineum",
        "sensitivity": 0.8,
        "arousal_boost": 0.7,
        "keywords": ["perineum"],
        "responses": [
            "DI SANA...",
            "TEKAN..."
        ],
        "dirty_talk": [
            "Tekan... antara..."
        ]
    }
}


# ===== BUILD AREAS DICTIONARY =====
AREAS: Dict[SensitiveArea, Dict] = {}


# Initialize AREAS with default values for any missing areas
for area in SensitiveArea:
    if area in AREA_DATA:
        AREAS[area] = AREA_DATA[area]
    else:
        # Default for any missing area
        AREAS[area] = {
            "name": area.value,
            "sensitivity": 0.5,
            "arousal_boost": 0.3,
            "keywords": [area.value.lower()],
            "responses": [
                f"*merintih* {area.value}ku...",
                f"Ah... jangan di {area.value}...",
                f"Sensitif..."
            ],
            "dirty_talk": [
                f"{area.value}ku sensitif...",
                f"Sentuh {area.value}ku..."
            ]
        }


# ===== HELPER FUNCTIONS =====

def get_area_by_keyword(text: str) -> List[Tuple[SensitiveArea, float]]:
    """
    Find sensitive areas mentioned in text
    
    Returns:
        List of (area, confidence) tuples
    """
    text_lower = text.lower()
    found = []
    
    for area, data in AREAS.items():
        for keyword in data["keywords"]:
            if keyword in text_lower:
                # Confidence based on keyword match
                confidence = 0.8
                if keyword == area.value.lower():
                    confidence = 1.0
                found.append((area, confidence))
                break
    
    return found


def get_arousal_boost(area: SensitiveArea, activity_intensity: float = 1.0) -> float:
    """Get arousal boost for touching this area"""
    data = AREAS.get(area, {})
    base_boost = data.get("arousal_boost", 0.3)
    return base_boost * activity_intensity


def get_sensitive_response(area: SensitiveArea) -> str:
    """Get random response for this area"""
    import random
    data = AREAS.get(area, {})
    responses = data.get("responses", [])
    if responses:
        return random.choice(responses)
    return f"*merintih* {area.value}ku..."


def get_dirty_talk(area: SensitiveArea) -> str:
    """Get random dirty talk for this area"""
    import random
    data = AREAS.get(area, {})
    talks = data.get("dirty_talk", [])
    if talks:
        return random.choice(talks)
    return f"{area.value}ku..."


# ===== EXPORT =====
__all__ = ['SensitiveArea', 'AREAS', 'get_area_by_keyword', 
           'get_arousal_boost', 'get_sensitive_response', 'get_dirty_talk']
