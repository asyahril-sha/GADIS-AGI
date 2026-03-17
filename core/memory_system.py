"""
MEMORY SYSTEM - Hippocampus digital
Menyimpan dan mengelola memori jangka panjang
"""

import numpy as np
import sqlite3
import json
import hashlib
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class MemoryTrace:
    """
    Satu trace memori dengan metadata
    """
    
    def __init__(self, content: str, memory_type: str, importance: float = 0.5, 
                 emotion: str = None, context: Dict = None):
        self.id = hashlib.md5(f"{content}{datetime.now()}".encode()).hexdigest()[:16]
        self.content = content
        self.memory_type = memory_type  # 'episodic', 'semantic', 'emotional'
        self.importance = importance
        self.emotion = emotion
        self.context = context or {}
        self.created_at = datetime.now()
        self.last_accessed = datetime.now()
        self.access_count = 0
        self.embedding = self._create_embedding(content)
    
    def _create_embedding(self, text: str) -> np.ndarray:
        """Buat embedding sederhana"""
        # Hash-based embedding (32 dimensi)
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
        
        Faktor:
        - Importance (0.4)
        - Recency (0.3)
        - Access frequency (0.3)
        """
        if current_time is None:
            current_time = datetime.now()
        
        # Recency factor (semakin baru semakin relevan)
        hours_ago = (current_time - self.last_accessed).total_seconds() / 3600
        recency = np.exp(-hours_ago / 24)  # Decay 24 jam
        
        # Frequency factor
        frequency = min(1.0, self.access_count / 20)
        
        # Kombinasi
        relevance = (
            self.importance * 0.4 +
            recency * 0.3 +
            frequency * 0.3
        )
        
        return relevance
    
    def to_dict(self) -> Dict:
        """Konversi ke dictionary"""
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


class MemorySystem:
    """
    Sistem memori jangka panjang - Hippocampus
    
    Fitur:
    - Menyimpan memori dengan embedding
    - Retrieval berdasarkan relevansi
    - Konsolidasi memori penting
    - Forgetting (memori tidak penting hilang)
    """
    
    def __init__(self, db_path: str, user_id: int):
        self.db_path = db_path
        self.user_id = user_id
        self.working_memory: List[MemoryTrace] = []  # Short-term buffer
        self._init_db()
    
    def _init_db(self):
        """Inisialisasi database"""
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
        
        c.execute('CREATE INDEX IF NOT EXISTS idx_user ON memories(user_id)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_importance ON memories(importance)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_created ON memories(created_at)')
        
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
            memory_type: Tipe memori
            importance: Tingkat kepentingan (0-1)
            emotion: Emosi terkait
            context: Konteks tambahan
        
        Returns:
            ID memori
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
        """Hitung tingkat kepentingan memori"""
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
        
        # Kata-kata penting
        important_keywords = [
            'cinta', 'sayang', 'first', 'pertama', 'orgasme', 'climax',
            'rahasia', 'janji', 'sumpah', 'menikah', 'putus', 'selamanya',
            'mati', 'hidup', 'milikku', 'sensitif', 'favorit'
        ]
        
        content_lower = content.lower()
        for word in important_keywords:
            if word in content_lower:
                importance += 0.1
                break
        
        return min(1.0, importance)
    
    def get_relevant_memories(self, query: str, limit: int = 5, 
                             min_importance: float = 0.3) -> List[Dict]:
        """
        Cari memori relevan dengan query
        
        Args:
            query: Kata kunci pencarian
            limit: Jumlah maksimal memori
            min_importance: Minimal importance
        
        Returns:
            List memori relevan
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        # Ambil memori dengan importance di atas threshold
        c.execute('''
            SELECT id, content, memory_type, importance, emotion, context,
                   created_at, last_accessed, access_count
            FROM memories
            WHERE user_id = ? AND importance >= ?
            ORDER BY importance DESC, last_accessed DESC
            LIMIT 20
        ''', (self.user_id, min_importance))
        
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
        """Dapatkan memori dari beberapa jam terakhir"""
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
        """Dapatkan memori penting"""
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
        """Dapatkan memori berdasarkan emosi"""
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
    
    def consolidate(self):
        """
        Konsolidasi memori - pindahkan memori penting ke long-term
        Hapus memori tidak penting
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        # Hapus memori dengan importance rendah dan jarang diakses
        c.execute('''
            DELETE FROM memories
            WHERE user_id = ? AND importance < 0.3 AND access_count < 3
        ''', (self.user_id,))
        
        deleted = c.rowcount
        conn.commit()
        conn.close()
        
        if deleted > 0:
            logger.info(f"🧹 Consolidated {deleted} memories for user {self.user_id}")
    
    def count(self) -> int:
        """Jumlah memori"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM memories WHERE user_id = ?', (self.user_id,))
        count = c.fetchone()[0]
        conn.close()
        return count
    
    def clear(self):
        """Hapus semua memori (hard reset)"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('DELETE FROM memories WHERE user_id = ?', (self.user_id,))
        deleted = c.rowcount
        conn.commit()
        conn.close()
        
        logger.info(f"🗑️ Cleared {deleted} memories for user {self.user_id}")
        return deleted
