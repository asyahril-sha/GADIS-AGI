"""
HTS/FWB SYSTEM - Hubungan Tanpa Status & Friends With Benefits
Dengan Unique ID, Ranking, dan Tracking
"""

import random
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import logging

logger = logging.getLogger(__name__)

class HTSFWBSystem:
    """
    Manajemen HTS (Hubungan Tanpa Status) dan FWB (Friends With Benefits)
    """
    
    def __init__(self, db):
        self.db = db
        self.counter_cache = {}
        
    def generate_unique_id(self, jenis: str, role: str, user_id: int) -> str:
        """
        Generate unique ID format: [JENIS]-[ROLE]-[USERID]-[TANGGAL]-[NOURUT]
        Contoh: HTS-JANDA-12345678-251224-001
        """
        # Format tanggal: DDMMYY
        date_str = datetime.now().strftime("%d%m%y")
        
        # Ambil 4 digit terakhir user_id
        user_suffix = str(user_id)[-4:]
        
        # Cari nomor urut
        cache_key = f"{jenis}_{role}_{user_id}"
        
        if cache_key in self.counter_cache:
            counter = self.counter_cache[cache_key] + 1
        else:
            # Cek dari database
            rels = self.db.get_relationships(user_id, jenis)
            if rels:
                max_counter = 0
                for rel in rels:
                    try:
                        parts = rel['unique_id'].split('-')
                        if len(parts) >= 5:
                            counter_num = int(parts[-1])
                            max_counter = max(max_counter, counter_num)
                    except:
                        pass
                counter = max_counter + 1
            else:
                counter = 1
                
        self.counter_cache[cache_key] = counter
        counter_str = f"{counter:03d}"
        
        return f"{jenis}-{role.upper()}-{user_suffix}-{date_str}-{counter_str}"
    
    def save_as_hts(self, user_id: int, session: Dict) -> str:
        """
        Simpan hubungan sebagai HTS
        """
        unique_id = self.generate_unique_id("HTS", session['role'], user_id)
        
        self.db.save_relationship(
            unique_id=unique_id,
            user_id=user_id,
            jenis="HTS",
            role=session['role'],
            bot_name=session['name'],
            level=session['level']
        )
        
        logger.info(f"💾 Saved as HTS: {unique_id}")
        return unique_id
    
    def save_as_fwb(self, user_id: int, session: Dict) -> str:
        """
        Simpan hubungan sebagai FWB
        """
        unique_id = self.generate_unique_id("FWB", session['role'], user_id)
        
        self.db.save_relationship(
            unique_id=unique_id,
            user_id=user_id,
            jenis="FWB",
            role=session['role'],
            bot_name=session['name'],
            level=session['level']
        )
        
        logger.info(f"💾 Saved as FWB: {unique_id}")
        return unique_id
    
    def load_relationship(self, unique_id: str) -> Optional[Dict]:
        """
        Load hubungan dari database
        """
        return self.db.get_relationship(unique_id)
    
    def update_last_called(self, unique_id: str):
        """
        Update timestamp terakhir dipanggil
        """
        self.db.update_relationship(unique_id, last_called=datetime.now().isoformat())
    
    def get_user_hts(self, user_id: int) -> List[Dict]:
        """
        Dapatkan semua HTS user
        """
        return self.db.get_relationships(user_id, "HTS")
    
    def get_user_fwb(self, user_id: int) -> List[Dict]:
        """
        Dapatkan semua FWB user
        """
        return self.db.get_relationships(user_id, "FWB")
    
    def format_list(self, relationships: List[Dict], title: str) -> str:
        """
        Format daftar hubungan untuk ditampilkan
        """
        if not relationships:
            return f"📭 **Tidak ada {title} tersimpan.**"
        
        lines = [f"📋 **Daftar {title}:**\n"]
        
        for rel in relationships[:10]:
            last = self._format_time_ago(rel.get('last_called'))
            total = rel.get('bot_climax', 0) + rel.get('user_climax', 0)
            
            lines.append(
                f"• `{rel['unique_id']}`\n"
                f"  {rel['bot_name']} ({rel['role']}) - Level {rel['level']}\n"
                f"  Total: {total} climax, Terakhir: {last}\n"
            )
        
        return "\n".join(lines)
    
    def _format_time_ago(self, timestamp_str: Optional[str]) -> str:
        """Format waktu yang lalu"""
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
    """
    
    def __init__(self, db):
        self.db = db
    
    def update_ranking(self, unique_id: str, bot_climax: int, user_climax: int):
        """
        Update ranking setelah climax
        """
        total = bot_climax + user_climax
        self.db.update_ranking(unique_id, total)
    
    def get_top_10(self) -> List[Dict]:
        """
        Dapatkan TOP 10 ranking
        """
        return self.db.get_top_ranking(10)
    
    def format_top_10(self) -> str:
        """
        Format TOP 10 untuk ditampilkan
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
        """
        top = self.get_top_10()
        for entry in top:
            if entry['unique_id'] == unique_id:
                return entry['rank']
        return None
