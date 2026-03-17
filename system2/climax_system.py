"""
CLIMAX SYSTEM - 200+ VARIASI CLIMAX
Bot Climax, User Climax, Together Climax, Aftercare
"""

import random
from typing import Dict, List, Optional, Tuple

class ClimaxSystem:
    """
    Sistem climax dengan 200+ variasi respons
    
    Fitur:
    - 50 Bot Climax
    - 50 User Climax  
    - 50 Together Climax
    - 50 Aftercare
    - Intensity-based responses
    - Style-based responses
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
            "*napas tersendat* Sebentar... aku mau crot... 💦",
            "*mata terpejam* Rasanya... enak banget... 💦",
            "*keringat dingin* Aku... mau... sekarang... 💦",
            "*tubuh meremang* Sensasi... aneh... enak... 💦",
            "*berbisik pelan* Keluar... aku keluar... 💦",
            
            # Intensitas Sedang (11-20)
            "*teriak kecil* AHH! Aku... datang! 💦",
            "*tubuh mengejang* AHHH! KELUAR! 💦",
            "*napas tersengal* Bersama... AHH... aku... 💦",
            "*meronta* STOP! AHH! SENSITIF! 💦",
            "*merintih panjang* AHHH! AHHH! Aku... 💦",
            "*kuku mencakar* AHH! Jangan berhenti! Aku mau! 💦",
            "*paha gemetar* AHHH! TUHAN! AHH! 💦",
            "*kepala terangkat* AKU! AKU! AHHHH! 💦",
            "*napas berat banget* Hah... hah... AHH! KELUAR! 💦",
            "*tubuh melengkung* AHHH! DALEM! AHH! 💦",
            
            # Intensitas Tinggi (21-30)
            "*teriak keras* AHHHHHH!!! AKU DATANG! 💦💦",
            "*tubuh gemetar hebat* AHH! AHH! AHH! TUHAN! 💦💦",
            "*napas putus-putus* A-aku... da-datang... AHHH! 💦💦",
            "*meringis kesakitan* DALEM... AHHH! KELUAR! 💦💦",
            "*teriak histeris* YA ALLAH! AHHHH! AMPUN! 💦💦",
            "*mata memutih* Aku... meninggal... enak... AHHH! 💦💦",
            "*lidah terjulur* AHHH! HABIS! AHHH! 💦💦",
            "*tubuh kejang* AHH! AHH! AHH! GILA! 💦💦",
            "*air mata keluar* NANGIS... ENAK BANGET... AHHH! 💦💦",
            "*menggigit apapun* AHHH! GIGIT! AHH! 💦💦",
            
            # Role-specific (31-40)
            "*menangis bahagia* Aku... nggak kuat... 💦",
            "*lemas total* Habis... aku habis... 💦",
            "*memeluk erat* Jangan lepas... aku masih... 💦",
            "*berbisik serak* Luar biasa... kamu... 💦",
            "*menggigit bahu* AHH! DALEM! AHH! 💦",
            "*tersenyum lelah* Terbaik... kamu terbaik... 💦",
            "*merangkul mesra* Hangat... aku ingin terus gini... 💦",
            "*tertidur sejenak* Zzz... eh! Aku ketiduran! 💦",
            "*kaget sendiri* Astaga... aku nggak kuat... 💦",
            "*tertawa lelah* Hehe... kita gila... 💦",
            
            # Very Intense (41-50)
            "*kejang-kejang* AHHHHH! AHHHH! AHHH! 💦💦💦",
            "*mata terbalik* Aku... meninggal... enak... 💦💦💦",
            "*teriak sampai serak* AHHHH! TUHAN! AMPUN! 💦💦💦",
            "*pingsan sejenak* ... *sadar* Aku... di mana? 💦",
            "*menangis keras* Jangan berhenti! AHH! AHH! 💦💦💦",
            "*tubuh kaku* AHHHHH! BEKU! ENAK! 💦💦💦",
            "*napas berhenti sejenak* ... *tarik napas* AHHH! 💦💦💦",
            "*meronta-ronta* LEPAS! AHH! SENSITIF! ENAK! 💦💦💦",
            "*tertawa histeris* HAHAHA! AHH! CROT! HAHA! 💦💦💦",
            "*berdoa* Ya Allah... ampun... enak banget... 💦💦💦"
        ]
        
        # ===== 50 USER CLIMAX =====
        self.user_climax = [
            # Respon melihat user climax (1-10)
            "*tersenyum puas* Iya... keluar... banyak... 💦",
            "*menatap dengan liar* Aku lihat... crot... 💦",
            "*menjilat bibir* Enak? Aku suka lihatnya... 💦",
            "*merangkul* Habis sudah... puas? 💦",
            "*berbisik* Kamu hebat... keluar banyak... 💦",
            "*tersipu* Banyak banget... aku sampai kaget... 💦",
            "*memegang erat* Rasain... aku buat kamu crot... 💦",
            "*tersenyum manis* Aku suka suara kamu pas crot... 💦",
            "*mengusap* Lembut... meskipun habis crot... 💦",
            "*menggoda* Mau lagi? Atau istirahat dulu? 💦",
            
            # Respon excited (11-20)
            "*bertepuk tangan* Yeay! Kamu crot! 💦",
            "*meloncat kecil* Aku berhasil buat kamu crot! 💦",
            "*tertawa senang* Puas kan sama aku? 💦",
            "*mengedip* Aku tahu cara buat kamu crot... 💦",
            "*tersenyum bangga* Aku ahli... 💦",
            "*memeluk* Selamat ya... udah crot... 💦",
            "*mengecup* Hadiah buat kamu... 💦",
            "*mengelus* Kamu hebat banget hari ini... 💦",
            "*berbisik nakal* Mau lagi? Aku bisa terus... 💦",
            "*menggoda* Lembek sekarang? Kasian... 💦",
            
            # Respon romantis (21-30)
            "*menatap dalam* Aku suka momen ini... 💦",
            "*tersenyum lembut* Kamu indah pas crot... 💦",
            "*memegang wajah* Lihat aku... aku bahagia... 💦",
            "*berbisik sayang* I love you... meski habis crot... 💦",
            "*mengelus rambut* Kamu hebat... aku bangga... 💦",
            "*merangkul hangat* Istirahat dulu... aku jagain... 💦",
            "*mengecup kening* Selamat malam... sayang... 💦",
            "*tersenyum damai* Aku suka begini... tenang... 💦",
            "*menggenggam tangan* Kita tetap bersama... 💦",
            "*berbisik* Jangan pergi... diam dulu... 💦",
            
            # Respon dominan (31-40)
            "*tersenyum licik* Aku buat kamu lemas... 💦",
            "*menepuk* Bagus... aku puas lihatnya... 💦",
            "*memerintah* Jangan gerak... diam... 💦",
            "*tertawa puas* Kamu crot karena aku... 💦",
            "*menatap tajam* Lain kali lebih banyak lagi... 💦",
            "*mencubit* Masih bisa? Atau habis? 💦",
            "*tersenyum sinis* Lemah... tapi aku suka... 💦",
            "*menjilat* Masih ada sisa... aku bersihin... 💦",
            "*memeluk dari belakang* Kamu milikku... 💦",
            "*berbisik* Next time... aku mau lebih... 💦",
            
            # Respon bercanda (41-50)
            "*tertawa* Crot... kedengarannya lucu... 💦",
            "*tersenyum* Kamu kayak kena magic... 💦",
            "*menggoda* Habis? Capek? Lemes? 💦",
            "*tertawa* Muka kamu lucu pas crot... 💦",
            "*mencubit pipi* Gemesin... udah crot... 💦",
            "*tersenyum* Aku rekam nggak ya tadi? 💦",
            "*mengedip* Besok lagi? Atau nanti malam? 💦",
            "*tertawa* Kamu crot lebih cepet dari biasanya... 💦",
            "*menggeleng* Dasar... nggak tahan... 💦",
            "*tersenyum* Puas? Aku juga... 💦"
        ]
        
        # ===== 50 TOGETHER CLIMAX =====
        self.together_climax = [
            # Bersama-sama intens (1-10)
            "*teriak bersama* AHHHH! KITA BERSAMA! 💦💦",
            "*tubuh gemetar berdua* Aku merasakan kamu... kamu merasakan aku... AHHH! 💦💦",
            "*lemas di pelukan* Kita... datang... bersamaan... AHH! 💦💦",
            "*napas tersengal* Sempurna... kita climax bersama... 💦💦",
            "*berbisik* Satu... kita satu... AHHH! 💦💦",
            "*teriak histeris* AHHHH! KITA! BERSAMA! AHHH! 💦💦",
            "*tubuh mengejang bersamaan* AHH! AHH! AHH! GILA! 💦💦",
            "*napas putus-putus* A-aku... kamu... kita... AHHH! 💦💦",
            "*mata bertemu* Lihat aku... kita... AHHH! 💦💦",
            "*berpegangan erat* Jangan lepas... rasakan... AHHH! 💦💦",
            
            # Romantis bersama (11-20)
            "*tersenyum bersamaan* Kita cocok... AHH! 💦💦",
            "*berbisik sayang* I love you... AHH... I love you too... 💦💦",
            "*memeluk erat* Hangat... rasanya... AHH... 💦💦",
            "*menangis bahagia* Kita... bersama... akhirnya... 💦💦",
            "*tertawa lelah* Hehe... kita gila bareng... 💦💦",
            "*saling memandang* Kamu... luar biasa... 💦💦",
            "*mengusap air mata* Jangan nangis... aku di sini... 💦💦",
            "*berbisik pelan* Momen ini... aku simpan... 💦💦",
            "*tersenyum damai* Tenang... setelah ini... 💦💦",
            "*menggenggam tangan* Kita tetap berdua... 💦💦",
            
            # Intensitas maksimal (21-30)
            "*teriak keras bareng* AHHHHHHHH!!! KITA! 💦💦💦",
            "*kejang-kejang bersama* AHH! AHH! AHH! GILA! 💦💦💦",
            "*mata memutih berdua* Aku... kamu... mati... enak... 💦💦💦",
            "*napas berhenti sejenak* ... *tarik napas* AHHH! 💦💦💦",
            "*meronta bersama* LEPAS! SENSITIF! ENAK! 💦💦💦",
            "*tertawa histeris bareng* HAHAHA! AHH! CROT! HAHA! 💦💦💦",
            "*berdoa bersama* Ya Allah... ampun... enak... 💦💦💦",
            "*pingsan bersama* ... *sadar* Kamu... aku... 💦💦💦",
            "*keringat bercucuran* Basah... kita basah... 💦💦💦",
            "*tubuh lemas total* Nggak bisa gerak... enak... 💦💦💦",
            
            # Setelah climax (31-40)
            "*terdiam bersamaan* ... *tersenyum* 💦💦",
            "*saling memeluk* Diam dulu... nikmatin... 💦💦",
            "*berbisik* Ini terbaik... 💦💦",
            "*menghela napas* Ah... puas... 💦💦",
            "*tertawa kecil* Kita lakukan lagi nanti... 💦💦",
            "*mengecup kening* Selamat... kita berhasil... 💦💦",
            "*merangkul* Istirahat... aku jagain... 💦💦",
            "*tersenyum* Kamu hebat... aku hebat... kita hebat... 💦💦",
            "*mengusap keringat* Basah... tapi bahagia... 💦💦",
            "*berbaring* Lihat langit-langit... puas... 💦💦",
            
            # Role-specific (41-50)
            "*menangis di dada* Aku... nggak nyangka... kita bisa... 💦💦",
            "*memeluk erat* Jangan pergi... aku mau terus gini... 💦💦",
            "*berbisik* Kamu milikku... aku milikmu... 💦💦",
            "*tersenyum* Mulai sekarang... kita satu... 💦💦",
            "*tertidur bersama* Zzz... zzz... 💦💦",
            "*kaget bareng* Eh! Kita ketiduran! 💦💦",
            "*tertawa* Lihat kita... berantakan... 💦💦",
            "*saling membersihkan* Sini... aku bersihin... 💦💦",
            "*mandi bersama* Yuk mandi... sekalian lagi... 💦💦",
            "*bercanda* Masih bisa? Atau habis? 💦💦"
        ]
        
        # ===== 50 AFTERCARE =====
        self.aftercare = [
            # Hangat dan nyaman (1-10)
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
            
            # Ngobrol santai (11-20)
            "*ngobrol* Tadi gimana? Puas?",
            "*tertawa kecil* Kita gila ya...",
            "*bertanya* Kamu crot berapa kali?",
            "*tersenyum* Aku crot 3 kali... kamu?",
            "*bercerita* Tadi pas kamu... aku...",
            "*mengakui* Aku pura-pura tidur...",
            "*tertawa* Padahal masih mau...",
            "*menggoda* Lagi? Atau istirahat?",
            "*tersenyum* Besok lagi ya?",
            "*mengedip* Janji... besok lebih...",
            
            # Perhatian fisik (21-30)
            "*mengusap keringat* Kamu basah...",
            "*menyiram air* Minum dulu...",
            "*mengipas* Panas ya...",
            "*membelai* Sakit? Nggak papa?",
            "*memijat* Pijat dulu...",
            "*mengecek* Masih keras? Hehe...",
            "*membersihkan* Sini... aku bersihin...",
            "*menyelimuti* Tidur... aku jagain...",
            "*mengatur bantal* Sini... sandar...",
            "*memeluk dari belakang* Hangat...",
            
            # Romantis (31-40)
            "*bernyanyi kecil* Lagu buat kamu...",
            "*membaca puisi* Aku tulis ini...",
            "*berbisik* Kamu berarti buat aku...",
            "*menatap bintang* Lihat... indah...",
            "*bercerita* Aku mimpiin kamu...",
            "*tersenyum* Kita kayak di surga...",
            "*menangis bahagia* Aku... bahagia...",
            "*menggenggam tangan* Jangan lepas...",
            "*berjanji* Aku nggak akan pergi...",
            "*berbisik* I love you... selamanya...",
            
            # Lucu dan ringan (41-50)
            "*tertawa* Perut keroncongan...",
            "*mengeluh* Lapar... kamu masakin...",
            "*bercanda* Besok gym... hari ini lemes...",
            "*tersenyum* Kita kayak di film...",
            "*tertawa* Kucing lihat kita...",
            "*menggoda* Masih bisa berdiri?",
            "*tertawa* Ajaib... kita bertahan...",
            "*tersenyum* Ini hari terbaik...",
            "*bercanda* Besok cuti... kita lagi...",
            "*tertawa* Orang tahu nggak ya? 💦"
        ]
        
    def get_bot_climax(self, intensity: str = "random") -> str:
        """
        Dapatkan respons bot climax
        
        Args:
            intensity: 'ringan', 'sedang', 'tinggi', 'very_intense', atau 'random'
            
        Returns:
            String respons climax
        """
        if intensity == "ringan":
            return random.choice(self.bot_climax[:10])
        elif intensity == "sedang":
            return random.choice(self.bot_climax[10:20])
        elif intensity == "tinggi":
            return random.choice(self.bot_climax[20:40])
        elif intensity == "very_intense":
            return random.choice(self.bot_climax[40:])
        return random.choice(self.bot_climax)
    
    def get_user_climax(self, style: str = "random") -> str:
        """
        Dapatkan respons user climax
        
        Args:
            style: 'puas', 'excited', 'romantis', 'dominan', 'canda', atau 'random'
            
        Returns:
            String respons
        """
        if style == "puas":
            return random.choice(self.user_climax[:10])
        elif style == "excited":
            return random.choice(self.user_climax[10:20])
        elif style == "romantis":
            return random.choice(self.user_climax[20:30])
        elif style == "dominan":
            return random.choice(self.user_climax[30:40])
        elif style == "canda":
            return random.choice(self.user_climax[40:])
        return random.choice(self.user_climax)
    
    def get_together_climax(self, style: str = "random") -> str:
        """
        Dapatkan respons together climax
        
        Args:
            style: 'intens', 'romantis', 'max', 'after', 'role', atau 'random'
            
        Returns:
            String respons
        """
        if style == "intens":
            return random.choice(self.together_climax[:10])
        elif style == "romantis":
            return random.choice(self.together_climax[10:20])
        elif style == "max":
            return random.choice(self.together_climax[20:30])
        elif style == "after":
            return random.choice(self.together_climax[30:40])
        elif style == "role":
            return random.choice(self.together_climax[40:])
        return random.choice(self.together_climax)
    
    def get_aftercare(self, style: str = "random") -> str:
        """
        Dapatkan aftercare message
        
        Args:
            style: 'hangat', 'ngobrol', 'perhatian', 'romantis', 'lucu', atau 'random'
            
        Returns:
            String aftercare
        """
        if style == "hangat":
            return random.choice(self.aftercare[:10])
        elif style == "ngobrol":
            return random.choice(self.aftercare[10:20])
        elif style == "perhatian":
            return random.choice(self.aftercare[20:30])
        elif style == "romantis":
            return random.choice(self.aftercare[30:40])
        elif style == "lucu":
            return random.choice(self.aftercare[40:])
        return random.choice(self.aftercare)
    
    def get_random_climax_sequence(self) -> Tuple[str, str, str]:
        """
        Dapatkan sequence climax lengkap
        
        Returns:
            Tuple (bot_climax, user_climax, together_climax)
        """
        return (
            self.get_bot_climax(),
            self.get_user_climax(),
            self.get_together_climax()
        )
    
    def get_complete_session(self) -> Tuple[str, str]:
        """
        Dapatkan session lengkap (climax + aftercare)
        
        Returns:
            Tuple (climax, aftercare)
        """
        climax = random.choice([
            self.get_bot_climax(),
            self.get_user_climax(),
            self.get_together_climax()
        ])
        after = self.get_aftercare()
        
        return climax, after
