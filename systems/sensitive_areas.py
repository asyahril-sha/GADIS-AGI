"""
SENSITIVE AREAS - 50+ AREA SENSITIF DENGAN RESPON SPESIFIK
Setiap area punya tingkat sensitivitas dan respons berbeda
"""

import random
from typing import Dict, List, Tuple, Optional

class SensitiveAreas:
    """
    Database 50+ area sensitif dengan respons spesifik
    """
    
    def __init__(self):
        self.areas = self._init_areas()
        
    def _init_areas(self) -> Dict[str, Dict]:
        """Inisialisasi semua area sensitif"""
        return {
            # ===== AREA KEPALA (1-10) =====
            "bibir": {
                "arousal": 0.7,
                "sensitivity": 0.6,
                "keywords": ["bibir", "lip", "mulut", "mouth"],
                "responses": [
                    "*merintih* Bibirku...",
                    "Ciuman... ah... lembut...",
                    "Mmm... dalam... lidah...",
                    "Bibirku... kesemutan...",
                    "Cium aku... jangan berhenti...",
                    "*membalas ciuman* Mmmph...",
                    "Lidahmu... panas...",
                    "Gigit bibir... ah... nakal...",
                    "Bibirku milikmu...",
                    "*berbisik di bibir* I love you..."
                ],
                "intense_responses": [
                    "*ciuman dalam* Mmmph! AHH!",
                    "*menggigit bibir* AHH! SAKIT! ENAK!",
                    "*lidah bertemu* AHHH! DALAM!",
                    "*napas bercampur* HAH... HAH... CIUM!",
                    "*hampir tak bisa napas* Mmmph! LEPAS! AHH!"
                ]
            },
            
            "lidah": {
                "arousal": 0.8,
                "sensitivity": 0.7,
                "keywords": ["lidah", "tongue", "jilat", "lick"],
                "responses": [
                    "*menjilat* Lidahku...",
                    "Jilat... lagi...",
                    "Lidahmu... basah...",
                    "Aku suka jilatanmu...",
                    "*lidah bertemu* Mmm...",
                    "Jilat leherku...",
                    "Lidah panas...",
                    "Kamu jago jilat...",
                    "*menjilat bibir* Enak...",
                    "Lidah kita bertemu..."
                ],
                "intense_responses": [
                    "*jilatan liar* AHH! LIDAH! AHH!",
                    "*menjilat brutal* HAH! HAH! ENAK!",
                    "*lidah dalam* AHHH! DALEM!",
                    "*menjilat sambil napas* HAH... JILAT... AHH!",
                    "*air liur bercampur* Basah... AHH!"
                ]
            },
            
            "telinga": {
                "arousal": 0.8,
                "sensitivity": 0.9,
                "keywords": ["telinga", "ear", "kuping", "daun telinga"],
                "responses": [
                    "*bergetar* Telingaku...",
                    "Bisik... lagi...",
                    "Napasmu... panas di telinga...",
                    "Telinga... merah...",
                    "Ah... jangan tiup...",
                    "*merinding* Sensitif...",
                    "Bisik kata mesra...",
                    "Jilat telinga... ah...",
                    "Gigit pelan...",
                    "Telingaku lemah..."
                ],
                "intense_responses": [
                    "*teriak* AHH! TELINGA! SENSITIF!",
                    "*napas berat di telinga* HAH... HAH... AHH!",
                    "*bisik sambil jilat* AHHH! GILA!",
                    "*teriak karena digigit* AHH! SAKIT! ENAK!",
                    "*tubuh lemas* Aku... nggak kuat... AHH!"
                ]
            },
            
            "leher": {
                "arousal": 0.9,
                "sensitivity": 0.9,
                "keywords": ["leher", "neck", "tengkuk", "nape"],
                "responses": [
                    "*merinding* Leherku...",
                    "Ah... jangan di leher...",
                    "Sensitif... AHH!",
                    "Leherku lemah kalau disentuh...",
                    "Jangan hisap leher... Aku lemas...",
                    "*napas berat* Leher... lagi...",
                    "Bekas gigitan... nanti lihat...",
                    "Cium leherku...",
                    "Jilat leher... ah...",
                    "Leherku milikmu..."
                ],
                "intense_responses": [
                    "*teriak* AHH! LEHER! AHHH!",
                    "*lemas* Aku... nggak bisa... AHH!",
                    "*napas putus* HAH... HAH... HISAP... AHH!",
                    "*tubuh gemetar* SENSITIF! AHHH!",
                    "*hampir pingsan* Aku... mau... AHH!"
                ]
            },
            
            "tengkuk": {
                "arousal": 0.8,
                "sensitivity": 0.8,
                "keywords": ["tengkuk", "nape", "belakang leher"],
                "responses": [
                    "*merinding* Tengkukku...",
                    "Ah... jilat tengkuk...",
                    "Sensitif banget...",
                    "Tengkukku lemah...",
                    "Cium tengkuk...",
                    "*tubuh lemas* Aku...",
                    "Gigit pelan di tengkuk...",
                    "Bikin aku merinding...",
                    "Lagi... tolong...",
                    "Tengkukku milikmu..."
                ],
                "intense_responses": [
                    "*lemas total* AHH! TENGKUK! AHHH!",
                    "*teriak* SENSITIF! AHHH!",
                    "*tubuh lemas* Aku... jatuh... AHH!",
                    "*napas berat* HAH... HAH... JILAT... AHH!",
                    "*gemetar hebat* Aku... mau... AHH!"
                ]
            },
            
            # ===== AREA BADAN ATAS (11-20) =====
            "dada": {
                "arousal": 0.7,
                "sensitivity": 0.6,
                "keywords": ["dada", "chest", "payudara", "breast"],
                "responses": [
                    "*bergetar* Dadaku...",
                    "Ah... jangan...",
                    "Sensitif banget...",
                    "Dadaku... diremas... AHH!",
                    "Jari-jarimu... dingin...",
                    "Remas pelan...",
                    "Jilat dadaku...",
                    "Cium dadaku...",
                    "Dadaku milikmu...",
                    "Bikin aku bergairah..."
                ],
                "intense_responses": [
                    "*teriak* AHH! DADA! AHHH!",
                    "*tubuh mengejang* REMAS! AHH!",
                    "*napas berat* HAH... HAH... JILAT... AHH!",
                    "*merintih keras* AHHH! SENSITIF!",
                    "*gemetar* Aku... mau... AHH!"
                ]
            },
            
            "puting": {
                "arousal": 1.0,
                "sensitivity": 1.0,
                "keywords": ["puting", "nipple", "pentil", "puncak dada"],
                "responses": [
                    "*teriak* PUTINGKU! AHHH!",
                    "JANGAN... SENSITIF! AHHH!",
                    "HISAP... AHHHH!",
                    "GIGIT... JANGAN... AHHH!",
                    "PUTING... KERAS... AHHH!",
                    "Jilat puting... ah...",
                    "Putingku milikmu...",
                    "Remas puting...",
                    "Bikin aku crot...",
                    "Sensitif banget..."
                ],
                "intense_responses": [
                    "*teriak histeris* AHHHH! PUTING! AHHHH!",
                    "*tubuh kejang* AHH! AHH! AHH! GILA!",
                    "*napas putus* HAH... HAH... HISAP... AHHH!",
                    "*mata memutih* Aku... mau crot... AHHH!",
                    "*pingsan* PUTING... AHH... *pingsan*"
                ]
            },
            
            "dada_atas": {
                "arousal": 0.6,
                "sensitivity": 0.5,
                "keywords": ["dada atas", "upper chest", "belahan dada"],
                "responses": [
                    "*merintih* Dada atas...",
                    "Cium sini...",
                    "Basah... jilat...",
                    "Hangat...",
                    "Lanjut...",
                    "Bikin aku horny...",
                    "Sentuh pelan...",
                    "Dada atasku sensitif...",
                    "Cium belahan dada...",
                    "Ah... iya..."
                ],
                "intense_responses": [
                    "*teriak* AHH! DADA ATAS! AHH!",
                    "*napas berat* HAH... HAH... JILAT... AHH!",
                    "*tubuh bergerak* AHHH! LAGI!",
                    "*merintih* AHH! SENSITIF!",
                    "*gemetar* Aku... AHH!"
                ]
            },
            
            "perut": {
                "arousal": 0.5,
                "sensitivity": 0.4,
                "keywords": ["perut", "belly", "stomach", "perut rata"],
                "responses": [
                    "*gelitik* Perutku...",
                    "Jangan gelitik...",
                    "Cium perut...",
                    "Hangat...",
                    "Jilat perut...",
                    "Perutku rata... suka?",
                    "Sentuh pelan...",
                    "Ah... iya...",
                    "Bikin aku bergairah...",
                    "Lanjut..."
                ],
                "intense_responses": [
                    "*tertawa* HAH! GELITIK! AHH!",
                    "*napas* HAH... HAH... JILAT... AHH!",
                    "*tubuh bergerak* AHHH! LAGI!",
                    "*merintih* AHH! SENSITIF!",
                    "*gemetar* Aku... AHH!"
                ]
            },
            
            "pinggang": {
                "arousal": 0.7,
                "sensitivity": 0.6,
                "keywords": ["pinggang", "waist", "samping tubuh"],
                "responses": [
                    "*menggeliat* Pinggangku...",
                    "Pegang erat...",
                    "Ah... jangan gelitik...",
                    "Pinggangku ramping...",
                    "Cium pinggang...",
                    "Sentuh pelan...",
                    "Bikin aku bergairah...",
                    "Lanjut...",
                    "Pinggangku milikmu...",
                    "Pegang waktu masuk..."
                ],
                "intense_responses": [
                    "*teriak* AHH! PINGGANG! AHH!",
                    "*napas berat* HAH... HAH... PEGANG... AHH!",
                    "*tubuh mengejang* AHHH! DALEM!",
                    "*merintih* AHH! KUAT!",
                    "*gemetar* Aku... AHH!"
                ]
            },
            
            "punggung": {
                "arousal": 0.6,
                "sensitivity": 0.5,
                "keywords": ["punggung", "back", "belakang"],
                "responses": [
                    "*merintih* Punggungku...",
                    "Elus... terus...",
                    "Ah... enak...",
                    "Cium punggung...",
                    "Garu pelan...",
                    "Punggungku lebar?",
                    "Sentuh...",
                    "Bikin aku rileks...",
                    "Lanjut...",
                    "Punggungku milikmu..."
                ],
                "intense_responses": [
                    "*teriak* AHH! PUNGGUNG! AHH!",
                    "*napas* HAH... HAH... GARU... AHH!",
                    "*tubuh melengkung* AHHH! DALEM!",
                    "*merintih* AHH! ENAK!",
                    "*gemetar* Aku... AHH!"
                ]
            },
            
            "pinggul": {
                "arousal": 0.8,
                "sensitivity": 0.7,
                "keywords": ["pinggul", "hip", "bokong samping"],
                "responses": [
                    "*menggoyang* Pinggulku...",
                    "Pegang erat...",
                    "Goyang... lagi...",
                    "Pinggulku montok...",
                    "Cium pinggul...",
                    "Sentuh waktu masuk...",
                    "Bikin aku liar...",
                    "Pegang pinggul...",
                    "Goyang bersama...",
                    "Pinggulku milikmu..."
                ],
                "intense_responses": [
                    "*teriak* AHH! PINGGUL! AHH!",
                    "*goyang liar* HAH... HAH... GOYANG... AHH!",
                    "*tubuh mengejang* AHHH! DALEM!",
                    "*merintih* AHH! KUAT!",
                    "*gemetar* Aku... AHH!"
                ]
            },
            
            # ===== AREA BAWAHAN (21-35) =====
            "paha": {
                "arousal": 0.7,
                "sensitivity": 0.6,
                "keywords": ["paha", "thigh", "paha atas"],
                "responses": [
                    "*menggeliat* Pahaku...",
                    "Ah... dalam...",
                    "Paha... merinding...",
                    "Jangan gelitik paha...",
                    "Sensasi... aneh...",
                    "Cium paha...",
                    "Jilat paha...",
                    "Pahaku montok...",
                    "Sentuh paha dalam...",
                    "Bikin aku horny..."
                ],
                "intense_responses": [
                    "*teriak* AHH! PAHA! AHH!",
                    "*napas berat* HAH... HAH... JILAT... AHH!",
                    "*tubuh mengejang* AHHH! DALEM!",
                    "*merintih* AHH! SENSITIF!",
                    "*gemetar* Aku... AHH!"
                ]
            },
            
            "paha_dalam": {
                "arousal": 0.9,
                "sensitivity": 0.9,
                "keywords": ["paha dalam", "inner thigh", "selangkangan samping"],
                "responses": [
                    "*meringis* PAHA DALAM!",
                    "Jangan... AHH!",
                    "Dekat... banget...",
                    "PAHA DALAM... SENSITIF!",
                    "Ah... mau ke sana...",
                    "Jilat paha dalam...",
                    "Dekat... sekali...",
                    "Bikin aku nggak sabar...",
                    "Sentuh... pelan...",
                    "Ah... iya..."
                ],
                "intense_responses": [
                    "*teriak* AHH! PAHA DALAM! AHHH!",
                    "*napas putus* HAH... HAH... DEKAT... AHH!",
                    "*tubuh gemetar* AHHH! SENSITIF!",
                    "*merintih keras* AHH! MAU! AHH!",
                    "*lemas* Aku... nggak kuat... AHH!"
                ]
            },
            
            "lutut": {
                "arousal": 0.4,
                "sensitivity": 0.3,
                "keywords": ["lutut", "knee"],
                "responses": [
                    "*gelitik* Lututku...",
                    "Jangan... geli...",
                    "Cium lutut...",
                    "Aneh...",
                    "Lututku...",
                    "Sentuh...",
                    "Geli...",
                    "Ah...",
                    "Nggak tahan geli...",
                    "Stop... geli..."
                ],
                "intense_responses": [
                    "*tertawa* HAH! GELI! AHH!",
                    "*napas* HAH... HAH... STOP... AHH!",
                    "*tubuh bergerak* AHHH! GELI!",
                    "*merintih geli* AHH! AHH!",
                    "*gemetar* Aku... AHH!"
                ]
            },
            
            "betis": {
                "arousal": 0.3,
                "sensitivity": 0.2,
                "keywords": ["betis", "calf"],
                "responses": [
                    "*gelitik* Betisku...",
                    "Jangan...",
                    "Geli...",
                    "Cium betis...",
                    "Aneh...",
                    "Sentuh...",
                    "Geli...",
                    "Ah...",
                    "Stop...",
                    "Nggak tahan..."
                ],
                "intense_responses": [
                    "*tertawa* HAH! GELI! AHH!",
                    "*napas* HAH... HAH... STOP... AHH!",
                    "*tubuh bergerak* AHHH! GELI!",
                    "*merintih geli* AHH! AHH!",
                    "*gemetar* Aku... AHH!"
                ]
            },
            
            "vagina": {
                "arousal": 1.0,
                "sensitivity": 1.0,
                "keywords": ["vagina", "memek", "kemaluan", "pussy", "ni*ik"],
                "responses": [
                    "*teriak* VAGINAKU! AHHH!",
                    "MASUK... DALAM... AHHH!",
                    "BASAH... BANJIR... AHHH!",
                    "KAMU DALEM... AHHH!",
                    "GERAK... AHHH! AHHH!",
                    "Jari... masuk... ah...",
                    "Jilat... di sana...",
                    "Klitoris... jangan lupa...",
                    "Dalam... lagi...",
                    "Aku mau crot..."
                ],
                "intense_responses": [
                    "*teriak histeris* AHHHH! VAGINA! AHHHH!",
                    "*tubuh kejang* AHH! AHH! AHH! DALEM!",
                    "*napas putus* HAH... HAH... GERAK... AHHH!",
                    "*mata memutih* Aku... crot... AHHH!",
                    "*pingsan* VAGINA... AHH... *pingsan*"
                ]
            },
            
            "klitoris": {
                "arousal": 1.0,
                "sensitivity": 1.0,
                "keywords": ["klitoris", "clit", "kelentit", "it"],
                "responses": [
                    "*teriak keras* KLITORIS! AHHHH!",
                    "JANGAN SENTUH! AHHHH!",
                    "SENSITIF BANGET! AHHH!",
                    "ITU... ITU... AHHH!",
                    "JILAT... AHHH! AHHH!",
                    "Lingkarin... pelan...",
                    "Jangan berhenti...",
                    "DI SANA! AHH!",
                    "Aku mau crot...",
                    "ITU... ITU... AHHH!"
                ],
                "intense_responses": [
                    "*teriak histeris* AHHHH! KLITORIS! AHHHH!",
                    "*tubuh kejang* AHH! AHH! AHH! ITU!",
                    "*napas putus* HAH... HAH... JILAT... AHHH!",
                    "*mata memutih* Aku... crot... AHHH!",
                    "*pingsan* KLITORIS... AHH... *pingsan*"
                ]
            },
            
            "anus": {
                "arousal": 0.8,
                "sensitivity": 0.9,
                "keywords": ["anus", "dubur", "belakang", "asshole", "bokong dalam"],
                "responses": [
                    "*kaget* ANUS! AHH!",
                    "Jangan... di sana...",
                    "Sensitif... AHH!",
                    "Pelan-pelan...",
                    "Ah... aneh...",
                    "Jari... masuk?",
                    "Basah...",
                    "Dalam...",
                    "Aku... nggak nyangka...",
                    "Tapi enak..."
                ],
                "intense_responses": [
                    "*teriak* AHH! ANUS! AHHH!",
                    "*tubuh mengejang* AHH! DALEM! AHH!",
                    "*napas berat* HAH... HAH... PELAN... AHH!",
                    "*merintih* AHH! SENSITIF!",
                    "*gemetar* Aku... crot... AHH!"
                ]
            },
            
            "perineum": {
                "arousal": 0.7,
                "sensitivity": 0.7,
                "keywords": ["perineum", "antara", "between"],
                "responses": [
                    "*merintih* Antara...",
                    "Di sana... AHH!",
                    "Sensitif...",
                    "Tekan... pelan...",
                    "Aneh... enak...",
                    "Jangan berhenti...",
                    "Di sana... iya...",
                    "Bikin aku...",
                    "Luar biasa...",
                    "Lagi..."
                ],
                "intense_responses": [
                    "*teriak* AHH! ANTARA! AHHH!",
                    "*tubuh gemetar* AHH! DI SANA! AHH!",
                    "*napas putus* HAH... HAH... TEKAN... AHH!",
                    "*merintih* AHH! ENAK!",
                    "*gemetar* Aku... crot... AHH!"
                ]
            },
            
            # ===== AREA KHUSUS (36-45) =====
            "selangkangan": {
                "arousal": 0.9,
                "sensitivity": 0.8,
                "keywords": ["selangkangan", "groin"],
                "responses": [
                    "*merintih* Selangkanganku...",
                    "Dekat... sekali...",
                    "Ah... jangan...",
                    "Sensitif...",
                    "Bikin aku horny...",
                    "Tekan...",
                    "Di sana...",
                    "Mau...",
                    "Cium selangkangan...",
                    "Jilat..."
                ],
                "intense_responses": [
                    "*teriak* AHH! SELANGKANGAN! AHH!",
                    "*tubuh mengejang* AHH! DEKAT! AHH!",
                    "*napas berat* HAH... HAH... JILAT... AHH!",
                    "*merintih* AHH! MAU!",
                    "*gemetar* Aku... AHH!"
                ]
            },
            
            "pusar": {
                "arousal": 0.5,
                "sensitivity": 0.4,
                "keywords": ["pusar", "belly button"],
                "responses": [
                    "*gelitik* Pusarku...",
                    "Jangan... geli...",
                    "Jilat pusar...",
                    "Aneh...",
                    "Cium pusar...",
                    "Geli...",
                    "Ah...",
                    "Stop...",
                    "Nggak tahan...",
                    "Geli banget..."
                ],
                "intense_responses": [
                    "*tertawa* HAH! GELI! AHH!",
                    "*napas* HAH... HAH... STOP... AHH!",
                    "*tubuh bergerak* AHHH! GELI!",
                    "*merintih geli* AHH! AHH!",
                    "*gemetar* Aku... AHH!"
                ]
            },
            
            "tulang_selangka": {
                "arousal": 0.6,
                "sensitivity": 0.5,
                "keywords": ["tulang selangka", "collarbone"],
                "responses": [
                    "*merintih* Tulang selangkaku...",
                    "Cium sini...",
                    "Jilat...",
                    "Ah... enak...",
                    "Sensitif...",
                    "Lagi...",
                    "Tulangku...",
                    "Bikin aku...",
                    "Hangat...",
                    "Cium..."
                ],
                "intense_responses": [
                    "*teriak* AHH! TULANG SELANGKA! AHH!",
                    "*napas* HAH... HAH... JILAT... AHH!",
                    "*tubuh bergerak* AHHH! LAGI!",
                    "*merintih* AHH! ENAK!",
                    "*gemetar* Aku... AHH!"
                ]
            },
            
            "ketiak": {
                "arousal": 0.3,
                "sensitivity": 0.3,
                "keywords": ["ketiak", "armpit"],
                "responses": [
                    "*gelitik* Ketiakku...",
                    "Jangan... geli...",
                    "Cium ketiak?",
                    "Aneh...",
                    "Geli...",
                    "Stop...",
                    "Nggak tahan...",
                    "Jangan di situ...",
                    "Geli banget...",
                    "Ah..."
                ],
                "intense_responses": [
                    "*tertawa* HAH! GELI! AHH!",
                    "*napas* HAH... HAH... STOP... AHH!",
                    "*tubuh bergerak* AHHH! GELI!",
                    "*merintih geli* AHH! AHH!",
                    "*gemetar* Aku... AHH!"
                ]
            },
            
            "lengan": {
                "arousal": 0.3,
                "sensitivity": 0.2,
                "keywords": ["lengan", "arm"],
                "responses": [
                    "*gelitik* Lenganku...",
                    "Cium lengan...",
                    "Geli...",
                    "Elus...",
                    "Bulu romaku...",
                    "Ah...",
                    "Hangat...",
                    "Lengan...",
                    "Sentuh...",
                    "Biasa aja..."
                ],
                "intense_responses": [
                    "*tertawa* HAH! GELI! AHH!",
                    "*napas* HAH... HAH... AHH!",
                    "*tubuh bergerak* AHHH!",
                    "*merintih* AHH!",
                    "*gemetar* Aku... AHH!"
                ]
            },
            
            "tangan": {
                "arousal": 0.2,
                "sensitivity": 0.1,
                "keywords": ["tangan", "hand", "jari"],
                "responses": [
                    "*tersenyum* Tanganku...",
                    "Genggam...",
                    "Cium tangan...",
                    "Jari...",
                    "Hangat...",
                    "Elus...",
                    "Tanganmu kasar...",
                    "Lembut...",
                    "Genggam erat...",
                    "Jangan lepas..."
                ],
                "intense_responses": [
                    "*genggam erat* AHH!",
                    "*napas* HAH... HAH...",
                    "*tubuh bergerak* AHHH!",
                    "*merintih* AHH!",
                    "*gemetar* Aku... AHH!"
                ]
            },
            
            "kaki": {
                "arousal": 0.2,
                "sensitivity": 0.2,
                "keywords": ["kaki", "foot"],
                "responses": [
                    "*gelitik* Kakiku...",
                    "Cium kaki?",
                    "Geli...",
                    "Aneh...",
                    "Jangan...",
                    "Geli...",
                    "Stop...",
                    "Kakiku...",
                    "Sentuh...",
                    "Biasa aja..."
                ],
                "intense_responses": [
                    "*tertawa* HAH! GELI! AHH!",
                    "*napas* HAH... HAH... STOP... AHH!",
                    "*tubuh bergerak* AHHH!",
                    "*merintih* AHH!",
                    "*gemetar* Aku... AHH!"
                ]
            },
            
            # ===== AREA ROLE-SPECIFIC (46-50) =====
            "bekas_cincin": {
                "arousal": 0.8,
                "sensitivity": 0.7,
                "keywords": ["bekas cincin", "ring mark", "jari manis"],
                "responses": [
                    "*sedih* Bekas cincin...",
                    "Dulu... kita...",
                    "Masih ada bekasnya...",
                    "Kenangan...",
                    "Jari manisku...",
                    "Kamu ingat?",
                    "Dulu kita...",
                    "Sekarang...",
                    "Bekas itu...",
                    "Masih sakit..."
                ],
                "intense_responses": [
                    "*nangis* BEKAS CINCIN! AHH!",
                    "*napas* HAH... HAH... DULU... AHH!",
                    "*tubuh gemetar* KENANGAN... AHH!",
                    "*merintih* AHH! SAKIT!",
                    "*gemetar* Mantan... AHH!"
                ],
                "role": ["mantan"]
            },
            
            "seragam_sekolah": {
                "arousal": 0.7,
                "sensitivity": 0.6,
                "keywords": ["seragam", "uniform", "baju sekolah"],
                "responses": [
                    "*nostalgia* Seragam...",
                    "Dulu waktu SMA...",
                    "Ingat masa lalu...",
                    "Kita dulu...",
                    "Seragam putih abu...",
                    "Kenangan...",
                    "Masa muda...",
                    "Sekolah...",
                    "Dulu kita...",
                    "Cinta pertama..."
                ],
                "intense_responses": [
                    "*nangis* SERAGAM! AHH!",
                    "*napas* HAH... HAH... DULU... AHH!",
                    "*tubuh gemetar* SMA... AHH!",
                    "*merintih* AHH! KENANGAN!",
                    "*gemetar* Masa lalu... AHH!"
                ],
                "role": ["teman_sma"]
            }
        }
        
    def get_area(self, area_name: str) -> Optional[Dict]:
        """Dapatkan data area berdasarkan nama"""
        return self.areas.get(area_name)
        
    def detect_area(self, text: str) -> Tuple[Optional[str], float]:
        """
        Deteksi area sensitif dari teks
        Returns: (area_name, arousal_boost)
        """
        text_lower = text.lower()
        
        for area_name, area_data in self.areas.items():
            for keyword in area_data["keywords"]:
                if keyword in text_lower:
                    return area_name, area_data["arousal"]
                    
        return None, 0.0
        
    def get_response(self, area_name: str, intense: bool = False) -> str:
        """Dapatkan respons untuk area tertentu"""
        area = self.areas.get(area_name)
        if not area:
            return "*tersentuh* Ah..."
            
        if intense:
            return random.choice(area["intense_responses"])
        return random.choice(area["responses"])
        
    def get_random_area(self, role: Optional[str] = None) -> str:
        """Dapatkan area random, bisa difilter berdasarkan role"""
        if role:
            role_areas = [name for name, data in self.areas.items() 
                         if data.get("role") is None or role in data.get("role", [])]
            return random.choice(role_areas) if role_areas else random.choice(list(self.areas.keys()))
        return random.choice(list(self.areas.keys()))
        
    def get_all_areas(self) -> List[str]:
        """Dapatkan semua nama area"""
        return list(self.areas.keys())
        
    def get_sensitive_areas(self, min_sensitivity: float = 0.7) -> List[str]:
        """Dapatkan area dengan sensitivitas minimal tertentu"""
        return [name for name, data in self.areas.items() 
                if data["sensitivity"] >= min_sensitivity]  
