"""
MEMORY SYSTEM - Hippocampus digital
Menyimpan dan mengelola memori jangka panjang
"""

import numpy as np
import sqlite3
import json
import hashlib
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any, Tuple
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class MemoryTrace:
    """
    Satu trace memori dengan metadata lengkap
    
    Attributes:
        id: Unique identifier untuk memori
        content: Isi memori
        memory_type: Tipe memori (episodic, semantic, emotional)
        importance: Tingkat kepentingan 0-1
        emotion: Emosi terkait memori
        context: Konteks tambahan
        created_at: Waktu pembuatan
        last_accessed: Waktu terakhir diakses
        access_count: Jumlah akses
        embedding: Vector embedding untuk similarity search
    """
    
    def __init__(self, content: str, memory_type: str = 'episodic', 
                 importance: float = 0.5, emotion: str = None, 
                 context: Dict = None):
        """
        Inisialisasi memory trace
        
        Args:
            content: Isi memori
            memory_type: Tipe memori
            importance: Tingkat kepentingan
            emotion: Emosi terkait
            context: Konteks tambahan
        """
        self.id = hashlib.md5(f"{content}{datetime.now()}".encode()).hexdigest()[:16]
        self.content = content
        self.memory_type = memory_type  # 'episodic', 'semantic', 'emotional', 'procedural'
        self.importance = importance
        self.emotion = emotion
        self.context = context or {}
        self.created_at = datetime.now()
        self.last_accessed = datetime.now()
        self.access_count = 0
        self.embedding = self._create_embedding(content)
    
    def _create_embedding(self, text: str) -> np.ndarray:
        """
        Buat embedding sederhana dari teks
        Menggunakan hash-based embedding (32 dimensi)
        
        Args:
            text: Teks untuk di-embed
            
        Returns:
            Array 32 dimensi
        """
        # Hash-based embedding sederhana
        hash_obj = hashlib.sha256(text.encode())
        hash_bytes = hash_obj.digest()[:32]
        return np.frombuffer(hash_bytes, dtype=np.uint8) / 255.0
    
    def access(self):
        """Tandai memori diakses"""
        self.last_accessed = datetime.now()
        self.access_count += 1
        # Importance naik sedikit setiap diakses
        self.importance = min(1.0, self.importance + 0.01)
    
    def get_relevance(self, current_time: datetime = None) -> float:
        """
        Hitung relevansi memori saat ini
        
        Faktor yang mempengaruhi:
        - Importance (bobot 0.4)
        - Recency (bobot 0.3) - semakin baru semakin relevan
        - Access frequency (bobot 0.3) - semakin sering diakses semakin relevan
        
        Args:
            current_time: Waktu sekarang (default: now)
            
        Returns:
            Skor relevansi 0-1
        """
        if current_time is None:
            current_time = datetime.now()
        
        # Recency factor (semakin baru semakin relevan)
        hours_ago = (current_time - self.last_accessed).total_seconds() / 3600
        recency = np.exp(-hours_ago / 24)  # Decay 24 jam
        
        # Frequency factor
        frequency = min(1.0, self.access_count / 20)
        
        # Kombinasi dengan bobot
        relevance = (
            self.importance * 0.4 +
            recency * 0.3 +
            frequency * 0.3
        )
        
        return relevance
    
    def to_dict(self) -> Dict:
        """
        Konversi ke dictionary untuk storage
        
        Returns:
            Dictionary representasi memori
        """
        return {
            'id': self.id,
            'content': self.content,
            'type': self.memory_type,
            'importance': self.importance,
            'emotion': self.emotion,
            'context': self.context,
            'created_at': self.created_at.isoformat(),
            'last_accessed': self.last_accessed.isoformat(),
            'access_count': self.access_count
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'MemoryTrace':
        """
        Buat MemoryTrace dari dictionary
        
        Args:
            data: Dictionary data memori
            
        Returns:
            MemoryTrace instance
        """
        trace = cls(
            content=data['content'],
            memory_type=data.get('type', 'episodic'),
            importance=data.get('importance', 0.5),
            emotion=data.get('emotion'),
            context=data.get('context', {})
        )
        trace.id = data['id']
        trace.created_at = datetime.fromisoformat(data['created_at'])
        trace.last_accessed = datetime.fromisoformat(data['last_accessed'])
        trace.access_count = data.get('access_count', 0)
        return trace


class MemorySystem:
    """
    Sistem memori jangka panjang - Hippocampus digital
    
    Fitur:
    - Menyimpan memori dengan embedding
    - Retrieval berdasarkan relevansi
    - Konsolidasi memori penting
    - Forgetting (memori tidak penting hilang)
    - Similarity search
    - Emotional tagging
    """
    
    def __init__(self, db_path: str, user_id: int):
        """
        Inisialisasi memory system
        
        Args:
            db_path: Path ke database SQLite
            user_id: ID user
        """
        self.db_path = db_path
        self.user_id = user_id
        self.working_memory: List[MemoryTrace] = []  # Short-term buffer
        self._init_db()
    
    def _init_db(self):
        """Inisialisasi database memori"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        c.execute('''
            CREATE TABLE IF NOT EXISTS memories (
                id TEXT PRIMARY KEY,
                user_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                memory_type TEXT NOT NULL,
                importance REAL DEFAULT 0.5,
                emotion TEXT,
                context TEXT,
                embedding BLOB,
                created_at TIMESTAMP,
                last_accessed TIMESTAMP,
                access_count INTEGER DEFAULT 0
            )
        ''')
        
        # Index untuk performa query
        c.execute('CREATE INDEX IF NOT EXISTS idx_user ON memories(user_id)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_importance ON memories(importance)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_created ON memories(created_at)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_emotion ON memories(emotion)')
        
        conn.commit()
        conn.close()
        
        logger.info(f"✅ Memory system initialized for user {self.user_id}")
    
    def add_memory(self, content: str, memory_type: str = 'episodic', 
                  importance: float = None, emotion: str = None, 
                  context: Dict = None) -> str:
        """
        Tambah memori baru
        
        Args:
            content: Isi memori
            memory_type: Tipe memori ('episodic', 'semantic', 'emotional', 'procedural')
            importance: Tingkat kepentingan (0-1), otomatis dihitung jika None
            emotion: Emosi terkait memori
            context: Konteks tambahan (level, location, dll)
        
        Returns:
            ID memori yang dibuat
        """
        # Hitung importance jika tidak diberikan
        if importance is None:
            importance = self._calculate_importance(content, context)
        
        # Buat trace memori
        memory = MemoryTrace(content, memory_type, importance, emotion, context)
        
        # Simpan ke database
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        c.execute('''
            INSERT INTO memories 
            (id, user_id, content, memory_type, importance, emotion, context, 
             embedding, created_at, last_accessed, access_count)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            memory.id, self.user_id, memory.content, memory.memory_type,
            memory.importance, memory.emotion, json.dumps(memory.context),
            memory.embedding.tobytes(), memory.created_at, memory.last_accessed,
            memory.access_count
        ))
        
        conn.commit()
        conn.close()
        
        # Tambah ke working memory
        self.working_memory.append(memory)
        if len(self.working_memory) > 10:
            self.working_memory.pop(0)
        
        logger.debug(f"📝 Memory added: {content[:50]}...")
        return memory.id
    
    def _calculate_importance(self, content: str, context: Dict = None) -> float:
        """
        Hitung tingkat kepentingan memori secara otomatis
        
        Faktor yang mempengaruhi:
        - Emosi kuat (+0.2)
        - Climax/orgasme (+0.3)
        - Level tinggi (+0.2)
        - First time experiences (+0.25)
        - Kata kunci penting (+0.1)
        
        Args:
            content: Isi memori
            context: Konteks tambahan
            
        Returns:
            Nilai importance 0-1
        """
        importance = 0.5  # Default
        
        if context:
            # Emosi kuat
            if context.get('emotion_intensity', 0) > 0.7:
                importance += 0.2
            
            # Climax / orgasme
            if context.get('is_climax', False):
                importance += 0.3
            
            # Level tinggi
            if context.get('level', 0) > 8:
                importance += 0.2
            
            # First time experiences
            if context.get('is_first_time', False):
                importance += 0.25
            
            # Public sex (excitement)
            if context.get('is_public', False):
                importance += 0.15
            
            # Position change
            if context.get('position_change', False):
                importance += 0.1
        
        # Kata-kata penting dalam content
        important_keywords = [
            'cinta', 'sayang', 'first', 'pertama', 'orgasme', 'climax',
            'rahasia', 'janji', 'sumpah', 'menikah', 'putus', 'selamanya',
            'mati', 'hidup', 'milikku', 'sensitif', 'favorit', 'crot',
            'together', 'bersama', 'soulmate', 'takdir'
        ]
        
        content_lower = content.lower()
        for word in important_keywords:
            if word in content_lower:
                importance += 0.1
                break
        
        return min(1.0, importance)
    
    def get_relevant_memories(self, query: str, limit: int = 5, 
                             min_importance: float = 0.3,
                             memory_types: List[str] = None) -> List[Dict]:
        """
        Cari memori relevan dengan query
        
        Args:
            query: Kata kunci pencarian
            limit: Jumlah maksimal memori
            min_importance: Minimal importance
            memory_types: Filter tipe memori
            
        Returns:
            List memori relevan
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        # Query dasar
        sql = '''
            SELECT id, content, memory_type, importance, emotion, context,
                   created_at, last_accessed, access_count
            FROM memories
            WHERE user_id = ? AND importance >= ?
        '''
        params = [self.user_id, min_importance]
        
        # Tambah filter tipe memori jika ada
        if memory_types:
            placeholders = ','.join(['?'] * len(memory_types))
            sql += f' AND memory_type IN ({placeholders})'
            params.extend(memory_types)
        
        sql += ' ORDER BY importance DESC, last_accessed DESC LIMIT 20'
        
        c.execute(sql, params)
        rows = c.fetchall()
        conn.close()
        
        # Skoring relevansi
        query_words = set(query.lower().split())
        scored = []
        
        for row in rows:
            memory = {
                'id': row[0],
                'content': row[1],
                'type': row[2],
                'importance': row[3],
                'emotion': row[4],
                'context': json.loads(row[5]) if row[5] else {},
                'created_at': row[6],
                'last_accessed': row[7],
                'access_count': row[8]
            }
            
            # Keyword matching score
            content_words = set(memory['content'].lower().split())
            common_words = query_words.intersection(content_words)
            keyword_score = len(common_words) / max(len(query_words), 1)
            
            # Recency score
            try:
                last = datetime.fromisoformat(memory['last_accessed'])
                hours_ago = (datetime.now() - last).total_seconds() / 3600
                recency = np.exp(-hours_ago / 24)
            except:
                recency = 0.5
            
            # Combined score
            score = (
                memory['importance'] * 0.4 +
                keyword_score * 0.3 +
                recency * 0.3
            )
            
            scored.append((score, memory))
        
        # Sort by score
        scored.sort(key=lambda x: x[0], reverse=True)
        
        # Update access count untuk yang terpilih
        result = []
        for score, memory in scored[:limit]:
            self._update_access_count(memory['id'])
            memory['relevance_score'] = score
            result.append(memory)
        
        return result
    
    def _update_access_count(self, memory_id: str):
        """Update access count memori"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        c.execute('''
            UPDATE memories 
            SET access_count = access_count + 1,
                last_accessed = ?
            WHERE id = ?
        ''', (datetime.now(), memory_id))
        
        conn.commit()
        conn.close()
    
    def get_recent_memories(self, hours: int = 24, limit: int = 10) -> List[Dict]:
        """
        Dapatkan memori dari beberapa jam terakhir
        
        Args:
            hours: Jumlah jam ke belakang
            limit: Jumlah maksimal memori
            
        Returns:
            List memori terbaru
        """
        cutoff = datetime.now() - timedelta(hours=hours)
        
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        c.execute('''
            SELECT id, content, memory_type, importance, emotion, context,
                   created_at, last_accessed, access_count
            FROM memories
            WHERE user_id = ? AND created_at >= ?
            ORDER BY created_at DESC
            LIMIT ?
        ''', (self.user_id, cutoff, limit))
        
        rows = c.fetchall()
        conn.close()
        
        memories = []
        for row in rows:
            memories.append({
                'id': row[0],
                'content': row[1],
                'type': row[2],
                'importance': row[3],
                'emotion': row[4],
                'context': json.loads(row[5]) if row[5] else {},
                'created_at': row[6],
                'last_accessed': row[7],
                'access_count': row[8]
            })
        
        return memories
    
    def get_important_memories(self, threshold: float = 0.7, limit: int = 10) -> List[Dict]:
        """
        Dapatkan memori penting (importance > threshold)
        
        Args:
            threshold: Batas importance
            limit: Jumlah maksimal memori
            
        Returns:
            List memori penting
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        c.execute('''
            SELECT id, content, memory_type, importance, emotion, context,
                   created_at, last_accessed, access_count
            FROM memories
            WHERE user_id = ? AND importance >= ?
            ORDER BY importance DESC, last_accessed DESC
            LIMIT ?
        ''', (self.user_id, threshold, limit))
        
        rows = c.fetchall()
        conn.close()
        
        memories = []
        for row in rows:
            memories.append({
                'id': row[0],
                'content': row[1],
                'type': row[2],
                'importance': row[3],
                'emotion': row[4],
                'context': json.loads(row[5]) if row[5] else {},
                'created_at': row[6],
                'last_accessed': row[7],
                'access_count': row[8]
            })
        
        return memories
    
    def get_memories_by_emotion(self, emotion: str, limit: int = 10) -> List[Dict]:
        """
        Dapatkan memori berdasarkan emosi
        
        Args:
            emotion: Nama emosi
            limit: Jumlah maksimal memori
            
        Returns:
            List memori dengan emosi tertentu
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        c.execute('''
            SELECT id, content, memory_type, importance, emotion, context,
                   created_at, last_accessed, access_count
            FROM memories
            WHERE user_id = ? AND emotion = ?
            ORDER BY importance DESC, created_at DESC
            LIMIT ?
        ''', (self.user_id, emotion, limit))
        
        rows = c.fetchall()
        conn.close()
        
        memories = []
        for row in rows:
            memories.append({
                'id': row[0],
                'content': row[1],
                'type': row[2],
                'importance': row[3],
                'emotion': row[4],
                'context': json.loads(row[5]) if row[5] else {},
                'created_at': row[6],
                'last_accessed': row[7],
                'access_count': row[8]
            })
        
        return memories
    
    def search_similar(self, query_embedding: np.ndarray, limit: int = 5) -> List[Dict]:
        """
        Cari memori dengan embedding similar (cosine similarity)
        
        Args:
            query_embedding: Vector query
            limit: Jumlah maksimal hasil
            
        Returns:
            List memori similar
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        c.execute('''
            SELECT id, content, memory_type, importance, emotion, context,
                   embedding, created_at, last_accessed, access_count
            FROM memories
            WHERE user_id = ? AND embedding IS NOT NULL
            ORDER BY importance DESC
            LIMIT 50
        ''', (self.user_id,))
        
        rows = c.fetchall()
        conn.close()
        
        # Hitung cosine similarity
        scored = []
        for row in rows:
            if row[6]:  # embedding
                emb = np.frombuffer(row[6], dtype=np.uint8) / 255.0
                
                # Cosine similarity
                similarity = np.dot(query_embedding, emb) / (
                    np.linalg.norm(query_embedding) * np.linalg.norm(emb) + 1e-8
                )
                
                memory = {
                    'id': row[0],
                    'content': row[1],
                    'type': row[2],
                    'importance': row[3],
                    'emotion': row[4],
                    'context': json.loads(row[5]) if row[5] else {},
                    'created_at': row[7],
                    'last_accessed': row[8],
                    'access_count': row[9]
                }
                
                # Combined score
                score = similarity * 0.6 + memory['importance'] * 0.4
                scored.append((score, memory))
        
        scored.sort(key=lambda x: x[0], reverse=True)
        return [mem for score, mem in scored[:limit]]
    
    def consolidate(self, days_threshold: int = 30):
        """
        Konsolidasi memori - hapus memori tidak penting
        
        Args:
            days_threshold: Hapus memori lebih lama dari ini dengan importance rendah
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        # Hapus memori dengan importance rendah dan jarang diakses
        cutoff = datetime.now() - timedelta(days=days_threshold)
        
        c.execute('''
            DELETE FROM memories
            WHERE user_id = ? AND importance < 0.3 AND access_count < 3
            AND created_at < ?
        ''', (self.user_id, cutoff))
        
        deleted = c.rowcount
        conn.commit()
        conn.close()
        
        if deleted > 0:
            logger.info(f"🧹 Consolidated {deleted} memories for user {self.user_id}")
    
    def count(self) -> int:
        """
        Jumlah memori user
        
        Returns:
            Total memori
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM memories WHERE user_id = ?', (self.user_id,))
        count = c.fetchone()[0]
        conn.close()
        return count
    
    def clear(self) -> int:
        """
        Hapus semua memori user (hard reset)
        
        Returns:
            Jumlah memori yang dihapus
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('DELETE FROM memories WHERE user_id = ?', (self.user_id,))
        deleted = c.rowcount
        conn.commit()
        conn.close()
        
        logger.info(f"🗑️ Cleared {deleted} memories for user {self.user_id}")
        return deleted
    
    def get_stats(self) -> Dict:
        """
        Dapatkan statistik memori
        
        Returns:
            Dictionary statistik
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        # Total memori
        c.execute('SELECT COUNT(*) FROM memories WHERE user_id = ?', (self.user_id,))
        total = c.fetchone()[0]
        
        # Rata-rata importance
        c.execute('SELECT AVG(importance) FROM memories WHERE user_id = ?', (self.user_id,))
        avg_importance = c.fetchone()[0] or 0
        
        # Memori per tipe
        c.execute('''
            SELECT memory_type, COUNT(*) 
            FROM memories 
            WHERE user_id = ? 
            GROUP BY memory_type
        ''', (self.user_id,))
        by_type = {row[0]: row[1] for row in c.fetchall()}
        
        # Memori per emosi
        c.execute('''
            SELECT emotion, COUNT(*) 
            FROM memories 
            WHERE user_id = ? AND emotion IS NOT NULL
            GROUP BY emotion
            ORDER BY COUNT(*) DESC
            LIMIT 5
        ''', (self.user_id,))
        top_emotions = {row[0]: row[1] for row in c.fetchall()}
        
        conn.close()
        
        return {
            'total': total,
            'avg_importance': round(avg_importance, 2),
            'by_type': by_type,
            'top_emotions': top_emotions,
            'working_memory_size': len(self.working_memory)
        }
