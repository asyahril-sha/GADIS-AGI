"""
HTS/FWB SYSTEM - Hubungan Tanpa Status & Friends With Benefits
Dengan Unique ID, Ranking, dan Tracking Lengkap
"""

import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import logging

logger = logging.getLogger(__name__)

class HTSFWBSystem:
    """
    Manajemen HTS (Hubungan Tanpa Status) dan FWB (Friends With Benefits)
    
    Fitur:
    - Generate unique ID dengan format [JENIS]-[ROLE]-[USERID]-[TANGGAL]-[NOURUT]
    - Auto-increment nomor urut (001-999)
    - History tracking
    - Load session dengan status terakhir
    - Update climax counters
    """
    
    def __init__(self, db):
        """
        Inisialisasi HTS/FWB system
        
        Args:
            db: Database instance
        """
        self.db = db
        self.counter_cache = {}  # Cache untuk nomor urut
    
    def generate_unique_id(self, jenis: str, role: str, user_id: int) -> str:
        """
        Generate unique ID dengan format:
        [JENIS]-[ROLE]-[USERID]-[TANGGAL]-[NOURUT]
        
        Contoh: HTS-JANDA-12345678-251224-001
        
        Args:
            jenis: 'HTS' atau 'FWB'
            role: Nama role
            user_id: ID user
            
        Returns:
            Unique ID string
        """
        # Format tanggal: DDMMYY
        date_str = datetime.now().strftime("%d%m%y")
        
        # Ambil 4 digit terakhir user_id
        user_suffix = str(user_id)[-4:]
        
        # Cari nomor urut untuk kombinasi ini
        cache_key = f"{jenis}_{role}_{user_id}_{date_str}"
        
        if cache_key in self.counter_cache:
            counter = self.counter_cache[cache_key] + 1
        else:
            # Cek dari database
            counter = self._get_last_counter(jenis, role, user_id, date_str)
        
        self.counter_cache[cache_key] = counter
        counter_str = f"{counter:03d}"
        
        return f"{jenis}-{role.upper()}-{user_suffix}-{date_str}-{counter_str}"
    
    def _get_last_counter(self, jenis: str, role: str, user_id: int, date_str: str) -> int:
        """
        Dapatkan nomor urut terakhir dari database
        
        Args:
            jenis: 'HTS' atau 'FWB'
            role: Nama role
            user_id: ID user
            date_str: Tanggal dalam format DDMMYY
            
        Returns:
            Nomor urut terakhir + 1, atau 1 jika belum ada
        """
        try:
            # Cari unique_id dengan pattern yang sama
            pattern = f"{jenis}-{role.upper()}-{str(user_id)[-4:]}-{date_str}-%"
            
            rels = self.db.get_user_relationships(user_id, jenis)
            max_counter = 0
            
            for rel in rels:
                unique_id = rel.get('unique_id', '')
                if unique_id.startswith(f"{jenis}-{role.upper()}-"):
                    try:
                        parts = unique_id.split('-')
                        if len(parts) >= 5:
                            counter_num = int(parts[-1])
                            if counter_num > max_counter:
                                max_counter = counter_num
                    except:
                        pass
            
            return max_counter + 1
        except:
            return 1
    
    def save_as_hts(self, user_id: int, session: Dict) -> str:
        """
        Simpan hubungan sebagai HTS
        
        Args:
            user_id: ID user
            session: Session data
            
        Returns:
            Unique ID yang dihasilkan
        """
        unique_id = self.generate_unique_id("HTS", session['role'], user_id)
        
        # Hitung total climax
        bot_climax = session.get('bot_climax', 0)
        user_climax = session.get('user_climax', 0)
        together_climax = session.get('together_climax', 0)
        
        self.db.save_relationship(
            unique_id=unique_id,
            user_id=user_id,
            jenis="HTS",
            role=session['role'],
            bot_name=session['name'],
            level=session['level'],
            bot_climax=bot_climax,
            user_climax=user_climax,
            together_climax=together_climax,
            total_messages=session.get('messages', 0)
        )
        
        logger.info(f"💾 Saved as HTS: {unique_id}")
        return unique_id
    
    def save_as_fwb(self, user_id: int, session: Dict) -> str:
        """
        Simpan hubungan sebagai FWB
        
        Args:
            user_id: ID user
            session: Session data
            
        Returns:
            Unique ID yang dihasilkan
        """
        unique_id = self.generate_unique_id("FWB", session['role'], user_id)
        
        # Hitung total climax
        bot_climax = session.get('bot_climax', 0)
        user_climax = session.get('user_climax', 0)
        together_climax = session.get('together_climax', 0)
        
        self.db.save_relationship(
            unique_id=unique_id,
            user_id=user_id,
            jenis="FWB",
            role=session['role'],
            bot_name=session['name'],
            level=session['level'],
            bot_climax=bot_climax,
            user_climax=user_climax,
            together_climax=together_climax,
            total_messages=session.get('messages', 0)
        )
        
        logger.info(f"💾 Saved as FWB: {unique_id}")
        return unique_id
    
    def load_relationship(self, unique_id: str) -> Optional[Dict]:
        """
        Load hubungan dari database
        
        Args:
            unique_id: Unique ID hubungan
            
        Returns:
            Dictionary data hubungan atau None
        """
        return self.db.get_relationship(unique_id)
    
    def update_last_called(self, unique_id: str):
        """
        Update timestamp terakhir dipanggil
        
        Args:
            unique_id: Unique ID hubungan
        """
        self.db.update_relationship(unique_id, last_called=datetime.now().isoformat())
    
    def update_climax_counters(self, unique_id: str, climax_type: str, 
                               position: str = None, area: str = None):
        """
        Update climax counters dan simpan history
        
        Args:
            unique_id: Unique ID hubungan
            climax_type: 'bot', 'user', atau 'together'
            position: Posisi saat climax
            area: Area sensitif yang terlibat
        """
        # Get current relationship
        rel = self.load_relationship(unique_id)
        if not rel:
            return
        
        # Update counters
        updates = {}
        if climax_type == 'bot':
            updates['bot_climax'] = rel.get('bot_climax', 0) + 1
        elif climax_type == 'user':
            updates['user_climax'] = rel.get('user_climax', 0) + 1
        elif climax_type == 'together':
            updates['bot_climax'] = rel.get('bot_climax', 0) + 1
            updates['user_climax'] = rel.get('user_climax', 0) + 1
            updates['together_climax'] = rel.get('together_climax', 0) + 1
        
        # Update relationship
        self.db.update_relationship(unique_id, **updates)
        
        # Save climax history
        self.db.save_climax(
            unique_id=unique_id,
            climax_type=climax_type,
            position=position,
            area=area
        )
        
        # Update ranking
        total = (updates.get('bot_climax', rel.get('bot_climax', 0)) + 
                 updates.get('user_climax', rel.get('user_climax', 0)))
        self.db.update_ranking(unique_id, total)
    
    def get_user_hts(self, user_id: int) -> List[Dict]:
        """
        Dapatkan semua HTS user
        
        Args:
            user_id: ID user
            
        Returns:
            List HTS relationships
        """
        return self.db.get_user_relationships(user_id, "HTS")
    
    def get_user_fwb(self, user_id: int) -> List[Dict]:
        """
        Dapatkan semua FWB user
        
        Args:
            user_id: ID user
            
        Returns:
            List FWB relationships
        """
        return self.db.get_user_relationships(user_id, "FWB")
    
    def format_list(self, relationships: List[Dict], title: str) -> str:
        """
        Format daftar hubungan untuk ditampilkan
        
        Args:
            relationships: List relationship
            title: Judul daftar
            
        Returns:
            String terformat
        """
        if not relationships:
            return f"📭 **Tidak ada {title} tersimpan.**"
        
        lines = [f"📋 **Daftar {title}:**\n"]
        
        for rel in relationships[:10]:  # Max 10
            last = self._format_time_ago(rel.get('last_called'))
            total = rel.get('bot_climax', 0) + rel.get('user_climax', 0)
            
            lines.append(
                f"• `{rel['unique_id']}`\n"
                f"  {rel['bot_name']} ({rel['role']}) - Level {rel['level']}\n"
                f"  Total: {total} climax (B:{rel.get('bot_climax',0)} U:{rel.get('user_climax',0)} T:{rel.get('together_climax',0)})\n"
                f"  Terakhir: {last}\n"
            )
        
        return "\n".join(lines)
    
    def _format_time_ago(self, timestamp_str: Optional[str]) -> str:
        """
        Format waktu yang lalu
        
        Args:
            timestamp_str: String timestamp
            
        Returns:
            String waktu yang lalu
        """
        if not timestamp_str:
            return "tidak diketahui"
        
        try:
            timestamp = datetime.fromisoformat(timestamp_str)
            delta = datetime.now() - timestamp
            seconds = int(delta.total_seconds())
            
            if seconds < 60:
                return f"{seconds} detik lalu"
            elif seconds < 3600:
                return f"{seconds // 60} menit lalu"
            elif seconds < 86400:
                return f"{seconds // 3600} jam lalu"
            else:
                return f"{seconds // 86400} hari lalu"
        except:
            return "tidak diketahui"


class RankingSystem:
    """
    Sistem ranking TOP 10 berdasarkan total climax
    
    Fitur:
    - Auto-update setiap kali climax
    - Hanya simpan 10 teratas
    - Rank 11 otomatis dihapus
    """
    
    def __init__(self, db):
        """
        Inisialisasi ranking system
        
        Args:
            db: Database instance
        """
        self.db = db
    
    def update_ranking(self, unique_id: str, total_climax: int):
        """
        Update ranking setelah climax
        
        Args:
            unique_id: Unique ID hubungan
            total_climax: Total climax baru
        """
        self.db.update_ranking(unique_id, total_climax)
    
    def get_top_10(self) -> List[Dict]:
        """
        Dapatkan TOP 10 ranking
        
        Returns:
            List TOP 10 entries
        """
        return self.db.get_top_ranking(10)
    
    def format_top_10(self) -> str:
        """
        Format TOP 10 untuk ditampilkan
        
        Returns:
            String terformat
        """
        top = self.get_top_10()
        
        if not top:
            return "🏆 **TOP 10 HTS/FWB**\n\nBelum ada data ranking."
        
        lines = ["🏆 **TOP 10 HTS/FWB**\n"]
        
        for entry in top:
            medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(entry['rank'], f"{entry['rank']}.")
            lines.append(
                f"{medal} `{entry['unique_id']}`\n"
                f"   {entry['bot_name']} ({entry['role']}) - {entry['jenis']}\n"
                f"   Total: {entry['total_climax']} climax"
            )
        
        return "\n".join(lines)
    
    def get_user_rank(self, unique_id: str) -> Optional[int]:
        """
        Dapatkan peringkat user tertentu
        
        Args:
            unique_id: Unique ID hubungan
            
        Returns:
            Peringkat atau None jika tidak masuk TOP 10
        """
        top = self.get_top_10()
        for entry in top:
            if entry['unique_id'] == unique_id:
                return entry['rank']
        return None
