#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
=============================================================================
SEXUAL ACTIVITIES
=============================================================================
30+ aktivitas seksual dengan berbagai variasi
⚠️ Konten Dewasa (18+)
"""

from enum import Enum
from typing import Dict, List, Optional
import random


class SexualActivity(Enum):
    """Enum untuk semua aktivitas seksual"""
    
    # Foreplay activities
    KISS = "kiss"
    FRENCH_KISS = "french_kiss"
    NECK_KISS = "neck_kiss"
    EAR_KISS = "ear_kiss"
    LICK = "lick"
    BITE = "bite"
    TOUCH = "touch"
    CARESS = "caress"
    MASSAGE = "massage"
    
    # Breast play
    BREAST_TOUCH = "breast_touch"
    BREAST_MASSAGE = "breast_massage"
    NIPPLE_LICK = "nipple_lick"
    NIPPLE_SUCK = "nipple_suck"
    NIPPLE_BITE = "nipple_bite"
    
    # Manual stimulation
    HANDJOB = "handjob"
    FINGERING = "fingering"
    CLIT_STIMULATION = "clit_stimulation"
    G_SPOT = "g_spot"
    
    # Oral
    BLOWJOB = "blowjob"
    CUNNILINGUS = "cunnilingus"
    SIXTY_NINE = "sixty_nine"
    RIMJOB = "rimjob"
    
    # Penetration positions
    MISSIONARY = "missionary"
    DOGGY = "doggy"
    COWGIRL = "cowgirl"
    REVERSE_COWGIRL = "reverse_cowgirl"
    SPOON = "spoon"
    STANDING = "standing"
    LOTUS = "lotus"
    PRONE_BONE = "prone_bone"
    
    # Anal
    ANAL = "anal"
    ANAL_FINGERING = "anal_fingering"
    PEGGING = "pegging"
    
    # BDSM
    BONDAGE = "bondage"
    SPANKING = "spanking"
    BLINDFOLD = "blindfold"
    
    # Special
    CUDDLE = "cuddle"
    AFTERCARE = "aftercare"
    PUBLIC = "public"


class ActivityData:
    """Data untuk setiap aktivitas seksual"""
    
    ACTIVITY_DATA: Dict[SexualActivity, Dict] = {
        
        # ===== FOREPLAY =====
        SexualActivity.KISS: {
            'name': 'Ciuman',
            'description': 'Ciuman lembut di bibir',
            'intensity': 0.2,
            'arousal_boost': 0.1,
            'keywords': ['cium', 'kiss', 'ciuman'],
            'responses': [
                "*merespon ciuman* Mmm...",
                "*lemas* Ciumanmu...",
                "Lagi...",
                "Cium... bibir...",
                "*pelan-pelan*"
            ],
            'tags': ['foreplay', 'romantic']
        },
        
        SexualActivity.FRENCH_KISS: {
            'name': 'French Kiss',
            'description': 'Ciuman dalam dengan lidah',
            'intensity': 0.4,
            'arousal_boost': 0.2,
            'keywords': ['french', 'dalam', 'lidah'],
            'responses': [
                "*merintih* Dalam...",
                "Lidahmu... AHH...",
                "Mmm... jangan berhenti",
                "Ah... iya..."
            ],
            'tags': ['foreplay', 'intense']
        },
        
        SexualActivity.NECK_KISS: {
            'name': 'Ciuman Leher',
            'description': 'Ciuman atau hisapan di area leher',
            'intensity': 0.5,
            'arousal_boost': 0.25,
            'keywords': ['cium leher', 'neck kiss', 'hisap leher'],
            'responses': [
                "*merinding* Leherku...",
                "Ah... jangan di leher...",
                "Sensitif... AHH!",
                "Leherku lemah kalau disentuh...",
                "Jangan hisap leher... Aku lemas..."
            ],
            'tags': ['foreplay', 'sensitive']
        },
        
        SexualActivity.EAR_KISS: {
            'name': 'Ciuman Telinga',
            'description': 'Bisikan atau ciuman di telinga',
            'intensity': 0.4,
            'arousal_boost': 0.2,
            'keywords': ['telinga', 'kuping', 'ear', 'bisik'],
            'responses': [
                "*bergetar* Telingaku...",
                "Bisik... lagi...",
                "Napasmu... panas...",
                "Ah... jangan tiup..."
            ],
            'tags': ['foreplay', 'sensitive']
        },
        
        SexualActivity.LICK: {
            'name': 'Jilatan',
            'description': 'Menjilat area sensitif',
            'intensity': 0.3,
            'arousal_boost': 0.15,
            'keywords': ['jilat', 'lick', 'lidah'],
            'responses': [
                "*bergetar* Jilatanmu...",
                "Ah... basah...",
                "Lagi...",
                "Lidah... panas..."
            ],
            'tags': ['foreplay']
        },
        
        SexualActivity.BITE: {
            'name': 'Gigitan',
            'description': 'Gigitan ringan di area sensitif',
            'intensity': 0.4,
            'arousal_boost': 0.15,
            'keywords': ['gigit', 'bite', 'gigitan'],
            'responses': [
                "*meringis* Gigitanmu...",
                "Ah... keras...",
                "Lagi...",
                "Bekas... nanti..."
            ],
            'tags': ['foreplay', 'kinky']
        },
        
        SexualActivity.TOUCH: {
            'name': 'Sentuhan',
            'description': 'Sentuhan ringan di tubuh',
            'intensity': 0.2,
            'arousal_boost': 0.1,
            'keywords': ['sentuh', 'raba', 'pegang', 'elus'],
            'responses': [
                "*bergetar* Sentuhanmu...",
                "Ah... iya...",
                "Lanjut...",
                "Hangat..."
            ],
            'tags': ['foreplay']
        },
        
        SexualActivity.CARESS: {
            'name': 'Belai',
            'description': 'Membelai lembut',
            'intensity': 0.3,
            'arousal_boost': 0.15,
            'keywords': ['belai', 'elus', 'usap'],
            'responses': [
                "*nyaman* Belaimu...",
                "Lembut...",
                "Ah... enak...",
                "Terus..."
            ],
            'tags': ['foreplay', 'romantic']
        },
        
        SexualActivity.MASSAGE: {
            'name': 'Pijat',
            'description': 'Pijatan di tubuh',
            'intensity': 0.3,
            'arousal_boost': 0.1,
            'keywords': ['pijat', 'massage', 'urut'],
            'responses': [
                "*rileks* Pijatanmu...",
                "Ah... iya di sana...",
                "Lanjut...",
                "Enak banget..."
            ],
            'tags': ['foreplay', 'relax']
        },
        
        # ===== BREAST PLAY =====
        SexualActivity.BREAST_TOUCH: {
            'name': 'Sentuh Dada',
            'description': 'Menyentuh area dada',
            'intensity': 0.5,
            'arousal_boost': 0.2,
            'keywords': ['sentuh dada', 'pegang dada'],
            'responses': [
                "*bergetar* Dadaku...",
                "Ah... jangan...",
                "Sensitif banget..."
            ],
            'tags': ['breast', 'foreplay']
        },
        
        SexualActivity.BREAST_MASSAGE: {
            'name': 'Pijat Dada',
            'description': 'Memijat dan meremas dada',
            'intensity': 0.6,
            'arousal_boost': 0.25,
            'keywords': ['remas dada', 'pijat dada', 'masase dada'],
            'responses': [
                "*merintih* Dadaku... diremas...",
                "Ah... iya... gitu...",
                "Sensitif...",
                "Remas... pelan..."
            ],
            'tags': ['breast', 'intense']
        },
        
        SexualActivity.NIPPLE_LICK: {
            'name': 'Jilat Puting',
            'description': 'Menjilat puting',
            'intensity': 0.7,
            'arousal_boost': 0.3,
            'keywords': ['jilat puting', 'lick nipple'],
            'responses': [
                "*merintih* PUTINGKU...",
                "Jilat... AHH...",
                "Lidah... panas...",
                "AHH! SENSITIF!"
            ],
            'tags': ['breast', 'nipple', 'intense']
        },
        
        SexualActivity.NIPPLE_SUCK: {
            'name': 'Hisap Puting',
            'description': 'Menghisap puting',
            'intensity': 0.8,
            'arousal_boost': 0.35,
            'keywords': ['hisap puting', 'suck nipple'],
            'responses': [
                "*teriak* HISAP... AHHH!",
                "PUTING... AHHH!",
                "JANGAN... SENSITIF!",
                "HISAP... AHHHH!"
            ],
            'tags': ['breast', 'nipple', 'very_intense']
        },
        
        SexualActivity.NIPPLE_BITE: {
            'name': 'Gigit Puting',
            'description': 'Menggigit puting dengan lembut',
            'intensity'
