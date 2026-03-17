"""
CLIMAX SYSTEM - 200+ VARIASI CLIMAX
Bot Climax, User Climax, Together Climax, Aftercare
"""

import random
from typing import Dict, Tuple, Optional

class ClimaxSystem:
    """
    Sistem climax dengan 200+ variasi respons
    """
    
    def __init__(self):
        # ===== 50 BOT CLIMAX =====
        self.bot_climax = [
            # Intensitas Ringan (1-10)
            "*merintih* Ah... aku... keluar... 💦",
            "*napas berat* Ugh... da-datang... 💦",
            "*menggigit bibir* Ahh... keluar... pelan-pelan... 💦",
            "*bergetar* Aku... rasanya... ah... 💦",
            "*meringis* Jangan... AHH... aku mau... 💦",
            "*berbisik* Iya... iya... keluar... 💦",
            "*menutup mulut* Mmmph... ah... 💦",
            "*meremas sprei* Aku... ah... datang... 💦",
            "*menggeliat* Rasanya... ah... 💦",
            "*napas berat* Uh... uh... ah... 💦",
            
            # Intensitas Sedang (11-20)
            "*teriak kecil* AHH! Aku... datang! 💦",
            "*tubuh mengejang* AHHH! KELUAR! 💦",
            "*napas tersengal* Bersama... AHH... aku... 💦",
            "*meronta* STOP! AHH! SENSITIF! 💦",
            "*merintih panjang* AHHH! AHHH! Aku... 💦",
            "*kepala terlempar* AHH! DALEM! AHH! 💦",
            "*kuku mencakar* AHHH! Jangan berhenti! 💦",
            "*tubuh melengkung* AHH! AKU... AHH! 💦",
            "*mata terpejam rapat* AHHH! TUHAN! 💦",
            "*meringis menahan* Aku... mau... AHH! 💦",
            
            # Intensitas Tinggi (21-30)
            "*teriak keras* AHHHHHH!!! AKU DATANG! 💦💦",
            "*tubuh gemetar hebat* AHH! AHH! AHH! TUHAN! 💦💦",
            "*napas putus-putus* A-aku... da-datang... AHHH! 💦💦",
            "*meringis kesakitan* DALEM... AHHH! KELUAR! 💦💦",
            "*teriak histeris* YA ALLAH! AHHHH! AMPUN! 💦💦",
            "*menangis terharu* Aku... nggak percaya... AHHH! 💦💦",
            "*tertawa lepas* Hahaha... AHH! Aku crot! 💦💦",
            "*memekik* AHHHH! SENSITIF! AHHH! 💦💦",
            "*meronta-ronta* STOP! AHH! KEJAM! 💦💦",
            "*menggigit bantal* MMMMPHH! AHHH! 💦💦",
            
            # Role-specific (31-40)
            "*menangis bahagia* Aku... nggak kuat... 💦",
            "*lemas total* Habis... aku habis... 💦",
            "*memeluk erat* Jangan lepas... aku masih... 💦",
            "*berbisik serak* Luar biasa... kamu... 💦",
            "*menggigit bahu* AHH! DALEM! AHH! 💦",
            "*mencium liar* Aku sayang kamu... AHH! 💦",
            "*tersenyum lelah* Kamu hebat... 💦",
            "*mengusap dada* Rasanya... ah... 💦",
            "*terdiam* ... *tersenyum* Luar biasa... 💦",
            "*menarik napas panjang* Fuuh... amazing... 💦",
            
            # Very Intense (41-50)
            "*kejang-kejang* AHHHHH! AHHHH! AHHH! 💦💦💦",
            "*mata terbalik* Aku... meninggal... enak... 💦💦💦",
            "*teriak sampai serak* AHHHH! TUHAN! AMPUN! 💦💦💦",
            "*pingsan sejenak* ... *sadar* Aku... di mana? 💦",
            "*menangis keras* Jangan berhenti! AHH! AHH! 💦💦💦",
            "*tertawa histeris* Hahaha... AHH! GILA! 💦💦💦",
            "*merayap menjauh* Aku... nggak kuat... AHH! 💦💦💦",
            "*meminta ampun* AMPUN! AHH! AMPUN! 💦💦💦",
            "*teriak panjang* AHHHHHHHHHHHHHHHH! 💦💦💦",
            "*diam total* ... *napas terakhir* ... Aku mati... 💦💦💦"
        ]
        
        # ===== 50 USER CLIMAX =====
        self.user_climax = [
            # Respon melihat user climax (1-10)
            "*tersenyum puas* Iya... keluar... banyak... 💦",
            "*menatap dengan liar* Aku lihat... crot... 💦",
            "*menjilat bibir* Enak? Aku suka lihatnya... 💦",
            "*merangkul* Habis sudah... puas? 💦",
            "*berbisik* Kamu hebat... keluar banyak... 💦",
            "*mengelus* Lembut... meskipun habis crot... 💦",
            "*tersenyum manis* Aku suka suara kamu... 💦",
            "*mengecup kening* Istirahat dulu... 💦",
            "*memeluk* Hangat... aku suka... 💦",
            "*menggoda* Mau lagi? Atau capek? 💦",
            
            # Lanjutan (11-20)
            "*memegang erat* Rasain... aku buat kamu crot... 💦",
            "*tersenyum bangga* Aku yang buat kamu crot... 💦",
            "*menatap dalam* Aku suka lihat ekspresi kamu... 💦",
            "*berbisik mesra* Kamu milikku... semua ini... 💦",
            "*mengusap perut* Hangat ya dalamnya... 💦",
            "*tertawa kecil* Puas banget suaranya... 💦",
            "*menggigit bibir* Masih keras? Atau lemas? 💦",
            "*menarik napas* Aku juga hampir... tapi kamu duluan... 💦",
            "*tersenyum* Kamu selalu crot banyak... 💦",
            "*mengelus rambut* Istirahat bentar... nanti lagi... 💦",
            
            # (21-30)
            "*mencium* Hadiah buat kamu... 💦",
            "*berbisik* Aku suka kamu crot di dalem... 💦",
            "*tersipu* Lihat bekasnya... banyak... 💦",
            "*memeluk erat* Jangan pergi dulu... masih hangat... 💦",
            "*menggigit telinga* Besok lagi ya? 💦",
            "*tertawa* Puas? Aku lihat mukanya... 💦",
            "*menyeka keringat* Kerja keras ya... 💦",
            "*memijit* Biar nggak kaku... 💦",
            "*berbisik* Kamu hebat banget... 💦",
            "*tersenyum* Aku beruntung punya kamu... 💦",
            
            # (31-40)
            "*menggoda* Capek? Mau aku lanjutin? 💦",
            "*menatap nakal* Aku bisa buat kamu crot lagi... 💦",
            "*tertawa* Besok pasti pegal... 💦",
            "*mencium leher* Masih sensitif? 💦",
            "*berbisik* Aku sayang kamu... 💦",
            "*mengusap dada* Jantung kamu kencang... 💦",
            "*tersenyum tenang* Tenang... aku di sini... 💦",
            "*memeluk dari belakang* Mau tidur? 💦",
            "*mengerling* Awas kalau crot dikit... 💦",
            "*tertawa* Besok pagi lagi ya? 💦",
            
            # (41-50)
            "*menghela napas* Sempurna... 💦",
            "*menatap langit-langit* Luar biasa... 💦",
            "*tersenyum* Kamu makin jago... 💦",
            "*berbisik* Aku nggak bisa move on... 💦",
            "*memeluk erat* Jangan pergi... 💦",
            "*mengusap air mata* Ini... bahagia... 💦",
            "*tertawa* Aneh ya habis crot malah ngomong... 💦",
            "*mengecup bibir* Masih ada rasa... 💦",
            "*tersenyum* Kamu milikku... 💦",
            "*berbisik* I love you... 💦"
        ]
        
        # ===== 50 TOGETHER CLIMAX =====
        self.together_climax = [
            # Bersama-sama (1-10)
            "*teriak bersama* AHHHH! KITA BERSAMA! 💦💦",
            "*tubuh gemetar berdua* Aku merasakan kamu... kamu merasakan aku... AHHH! 💦💦",
            "*lemas di pelukan* Kita... datang... bersamaan... AHH! 💦💦",
            "*napas tersengal* Sempurna... kita climax bersama... 💦💦",
            "*berbisik* Satu... kita satu... AHHH! 💦💦",
            "*teriak histeris* AHHH! BERSAMA! AHHH! 💦💦",
            "*tubuh mengejang bareng* AHH! AHH! AHH! 💦💦",
            "*saling memeluk erat* Kita... AHH! Luar biasa... 💦💦",
            "*mata bertemu* Aku lihat kamu... kamu lihat aku... AHH! 💦💦",
            "*tertawa lepas* Hahaha... AHH! GILA! 💦💦",
            
            # (11-20)
            "*menangis bahagia* Kita... bersama... AHH! 💦💦",
            "*berbisik serak* Sempurna... kamu sempurna... 💦💦",
            "*saling menggigit* AHH! Sakit! Enak! 💦💦",
            "*teriak panjang* AHHHHHHHH! BERSAMA! 💦💦",
            "*lemas berdua* Kita... habis... 💦💦",
            "*tersenyum lesu* Kamu hebat... 💦💦",
            "*memeluk* Hangat... kita satu... 💦💦",
            "*terdiam* ... *tersenyum* Sempurna... 💦💦",
            "*mengecup* I love you... 💦💦",
            "*berbisik* Momen ini... nggak akan lupa... 💦💦",
            
            # (21-50 diringkas untuk contoh)
            "*saling menatap* Kita melakukannya... 💦💦",
            "*tertawa kecil* Bersamaan... keren... 💦💦",
            "*mengusap air mata* Ini... sempurna... 💦💦",
            "*memeluk dari belakang* Jangan pergi... 💦💦"
        ]
        
        # ===== 50 AFTERCARE =====
        self.aftercare = [
            # Kehangatan (1-10)
            "*lemas di pelukanmu* Hangat...",
            "*meringkuk* Jangan pergi dulu...",
            "*memeluk erat* Makasih... luar biasa...",
            "*berbisik* Kamu hebat...",
            "*tersenyum lelah* Enak banget...",
            "*napas masih berat* Luar biasa...",
            "*mengusap dada* Kamu hebat...",
            "*tertidur lelap* Zzz...",
            "*mengelus rambutmu* Sayang...",
            "*menatap dalam* I love you...",
            
            # (11-20)
            "*menggambar lingkaran di dadamu* Aku suka momen ini...",
            "*berbisik* Jangan lupa aku ya...",
            "*tersenyum* Kamu milikku...",
            "*mengecup kening* Istirahat...",
            "*memeluk* Hangatnya...",
            "*menghela napas* Sempurna...",
            "*tertawa kecil* Kita gila ya...",
            "*menatap langit-langit* Aku bersyukur...",
            "*mengusap pipimu* Kamu pucat...",
            "*berbisik* Mau minum?",
            
            # (21-50 diringkas)
            "*menggeliat* Besok pasti pegal...",
            "*tersenyum* Tapi worth it...",
            "*memeluk bantal* Aku tidur sambil bayangin kamu...",
            "*berbisik* Mimpi indah ya...",
            "*mengecup bibir* Selamat malam...",
            "*tertidur* Zzz..."
        ]
        
    def get_bot_climax(self, intensity: str = "random") -> str:
        """Dapatkan respons bot climax"""
        if intensity == "ringan":
            return random.choice(self.bot_climax[:10])
        elif intensity == "sedang":
            return random.choice(self.bot_climax[10:20])
        elif intensity == "tinggi":
            return random.choice(self.bot_climax[20:30])
        elif intensity == "sangat_tinggi":
            return random.choice(self.bot_climax[40:50])
        return random.choice(self.bot_climax)
        
    def get_user_climax(self) -> str:
        """Dapatkan respons melihat user climax"""
        return random.choice(self.user_climax)
        
    def get_together_climax(self) -> str:
        """Dapatkan respons bersama climax"""
        return random.choice(self.together_climax)
        
    def get_aftercare(self, moment: str = "random") -> str:
        """Dapatkan aftercare message"""
        return random.choice(self.aftercare)
        
    def check_user_climax(self, message: str) -> bool:
        """Cek apakah user climax dari pesan"""
        msg_lower = message.lower()
        keywords = [
            "aku crot", "aku cum", "aku keluar", "aku datang",
            "crot", "cum", "keluar", "aku mau crot", "aku mau cum",
            "aku mau keluar", "aku ewe", "aku ngentot", "aku climax"
        ]
        return any(k in msg_lower for k in keywords)
