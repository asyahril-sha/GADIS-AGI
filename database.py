"""
DATABASE MANAGER - SQLite untuk menyimpan semua data
"""

import sqlite3
import json
import logging
from contextlib import contextmanager
from datetime import datetime
from typing import Dict, List, Optional, Any

logger = logging.getLogger(__name__)

class Database:
    """Database manager untuk semua data bot"""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init_db()
        
    def _init_db(self):
        """Inisialisasi semua tabel database"""
        with self._get_conn() as conn:
            c = conn.cursor()
            
            # ===== TABEL USERS =====
            c.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    first_name TEXT,
                    role TEXT,
                    level INTEGER DEFAULT 1,
                    total_messages INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_active TIMESTAMP
                )
            ''')
            
            # ===== TABEL RELATIONSHIPS (HTS/FWB) =====
            c.execute('''
                CREATE TABLE IF NOT EXISTS relationships (
                    unique_id TEXT PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    jenis TEXT NOT NULL,
                    role TEXT NOT NULL,
                    bot_name TEXT NOT NULL,
                    level INTEGER DEFAULT 1,
                    dominance_level INTEGER DEFAULT 1,
                    bot_climax INTEGER DEFAULT 0,
                    user_climax INTEGER DEFAULT 0,
                    together_climax INTEGER DEFAULT 0,
                    favorite_position TEXT,
                    favorite_area TEXT,
                    total_messages INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_called TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
                )
            ''')
            
            # ===== TABEL CONVERSATIONS =====
            c.execute('''
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    position TEXT,
                    location TEXT,
                    dominance_level INTEGER,
                    emotion TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
                )
            ''')
            
            # ===== TABEL CLIMAX HISTORY =====
            c.execute('''
                CREATE TABLE IF NOT EXISTS climax_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    unique_id TEXT NOT NULL,
                    climax_type TEXT NOT NULL,
                    position TEXT,
                    area TEXT,
                    intensity REAL DEFAULT 1.0,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (unique_id) REFERENCES relationships(unique_id) ON DELETE CASCADE
                )
            ''')
            
            # ===== TABEL RANKING =====
            c.execute('''
                CREATE TABLE IF NOT EXISTS ranking (
                    rank INTEGER PRIMARY KEY AUTOINCREMENT,
                    unique_id TEXT UNIQUE NOT NULL,
                    total_climax INTEGER DEFAULT 0,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (unique_id) REFERENCES relationships(unique_id) ON DELETE CASCADE
                )
            ''')
            
            # ===== TABEL MEMORIES =====
            c.execute('''
                CREATE TABLE IF NOT EXISTS memories (
                    id TEXT PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    content TEXT NOT NULL,
                    memory_type TEXT NOT NULL,
                    importance REAL DEFAULT 0.5,
                    emotion TEXT,
                    context TEXT,
                    created_at TIMESTAMP,
                    last_accessed TIMESTAMP,
                    access_count INTEGER DEFAULT 0,
                    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
                )
            ''')

            # ===== TABEL AI STATES =====
            c.execute('''
                CREATE TABLE IF NOT EXISTS ai_states (
                    admin_id INTEGER PRIMARY KEY,
                    state TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # ===== INDEXES =====
            c.execute('CREATE INDEX IF NOT EXISTS idx_users_active ON users(last_active)')
            c.execute('CREATE INDEX IF NOT EXISTS idx_relationships_user ON relationships(user_id)')
            c.execute('CREATE INDEX IF NOT EXISTS idx_relationships_type ON relationships(jenis)')
            c.execute('CREATE INDEX IF NOT EXISTS idx_conversations_user ON conversations(user_id)')
            c.execute('CREATE INDEX IF NOT EXISTS idx_climax_unique ON climax_history(unique_id)')
            c.execute('CREATE INDEX IF NOT EXISTS idx_memories_user ON memories(user_id)')
            
            conn.commit()
            logger.info("✅ Database initialized")
    
    @contextmanager
    def _get_conn(self):
        """Dapatkan koneksi database"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()
    
    # ===== USER METHODS =====
    
    def save_user(self, user_id: int, username: str = None, first_name: str = None, 
                  role: str = None, level: int = 1):
        """Simpan atau update user"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                INSERT OR REPLACE INTO users 
                (user_id, username, first_name, role, level, last_active)
                VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ''', (user_id, username, first_name, role, level))
            conn.commit()
    
    def get_user(self, user_id: int) -> Optional[Dict]:
        """Ambil data user"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
            row = c.fetchone()
            return dict(row) if row else None
    
    def update_user_level(self, user_id: int, level: int):
        """Update level user"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                UPDATE users 
                SET level = ?, last_active = CURRENT_TIMESTAMP
                WHERE user_id = ?
            ''', (level, user_id))
            conn.commit()
    
    def increment_user_messages(self, user_id: int):
        """Tambah hitungan pesan user"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                UPDATE users 
                SET total_messages = total_messages + 1,
                    last_active = CURRENT_TIMESTAMP
                WHERE user_id = ?
            ''', (user_id,))
            conn.commit()
    
    # ===== RELATIONSHIP METHODS =====
    
    def save_relationship(self, unique_id: str, user_id: int, jenis: str, role: str,
                          bot_name: str, level: int = 1, **kwargs):
        """Simpan hubungan HTS/FWB"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                INSERT OR REPLACE INTO relationships 
                (unique_id, user_id, jenis, role, bot_name, level, 
                 dominance_level, bot_climax, user_climax, together_climax,
                 favorite_position, favorite_area, total_messages, last_called)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ''', (
                unique_id, user_id, jenis, role, bot_name, level,
                kwargs.get('dominance_level', 1),
                kwargs.get('bot_climax', 0),
                kwargs.get('user_climax', 0),
                kwargs.get('together_climax', 0),
                kwargs.get('favorite_position'),
                kwargs.get('favorite_area'),
                kwargs.get('total_messages', 0)
            ))
            conn.commit()
    
    def update_relationship(self, unique_id: str, **kwargs):
        """Update relationship"""
        if not kwargs:
            return
        
        fields = []
        values = []
        for key, value in kwargs.items():
            fields.append(f"{key}=?")
            values.append(value)
        values.append(unique_id)
        
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute(f'''
                UPDATE relationships 
                SET {', '.join(fields)}, last_called = CURRENT_TIMESTAMP
                WHERE unique_id = ?
            ''', values)
            conn.commit()
    
    def get_relationship(self, unique_id: str) -> Optional[Dict]:
        """Ambil relationship by ID"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM relationships WHERE unique_id = ?', (unique_id,))
            row = c.fetchone()
            return dict(row) if row else None
    
    def get_user_relationships(self, user_id: int, jenis: str = None) -> List[Dict]:
        """Ambil semua relationship user"""
        with self._get_conn() as conn:
            c = conn.cursor()
            if jenis:
                c.execute('''
                    SELECT * FROM relationships 
                    WHERE user_id = ? AND jenis = ?
                    ORDER BY last_called DESC
                ''', (user_id, jenis))
            else:
                c.execute('''
                    SELECT * FROM relationships 
                    WHERE user_id = ?
                    ORDER BY last_called DESC
                ''', (user_id,))
            return [dict(row) for row in c.fetchall()]
    
    def delete_relationship(self, unique_id: str):
        """Hapus relationship"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('DELETE FROM relationships WHERE unique_id = ?', (unique_id,))
            conn.commit()
    
    # ===== CONVERSATION METHODS =====
    
    def save_conversation(self, user_id: int, role: str, content: str,
                          position: str = None, location: str = None,
                          dominance_level: int = None, emotion: str = None):
        """Simpan percakapan"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                INSERT INTO conversations 
                (user_id, role, content, position, location, dominance_level, emotion)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, role, content, position, location, dominance_level, emotion))
            conn.commit()
    
    def get_recent_conversations(self, user_id: int, limit: int = 20) -> List[Dict]:
        """Ambil percakapan terbaru"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                SELECT role, content, position, location, dominance_level, emotion, timestamp
                FROM conversations 
                WHERE user_id = ?
                ORDER BY timestamp DESC
                LIMIT ?
            ''', (user_id, limit))
            return [dict(row) for row in c.fetchall()]
    
    # ===== CLIMAX METHODS =====
    
    def save_climax(self, unique_id: str, climax_type: str,
                    position: str = None, area: str = None, intensity: float = 1.0):
        """Simpan history climax"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                INSERT INTO climax_history 
                (unique_id, climax_type, position, area, intensity)
                VALUES (?, ?, ?, ?, ?)
            ''', (unique_id, climax_type, position, area, intensity))
            conn.commit()
    
    def get_climax_history(self, unique_id: str, limit: int = 20) -> List[Dict]:
        """Ambil history climax"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                SELECT climax_type, position, area, intensity, timestamp
                FROM climax_history 
                WHERE unique_id = ?
                ORDER BY timestamp DESC
                LIMIT ?
            ''', (unique_id, limit))
            return [dict(row) for row in c.fetchall()]
    
    # ===== RANKING METHODS =====
    
    def update_ranking(self, unique_id: str, total_climax: int):
        """Update ranking"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                INSERT OR REPLACE INTO ranking (unique_id, total_climax)
                VALUES (?, ?)
            ''', (unique_id, total_climax))
            conn.commit()
    
    def get_top_ranking(self, limit: int = 10) -> List[Dict]:
        """Ambil TOP ranking"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                SELECT r.rank, r.unique_id, r.total_climax,
                       rel.bot_name, rel.role, rel.jenis
                FROM ranking r
                JOIN relationships rel ON r.unique_id = rel.unique_id
                ORDER BY r.total_climax DESC
                LIMIT ?
            ''', (limit,))
            return [dict(row) for row in c.fetchall()]
    
    # ===== MEMORY METHODS =====
    
    def save_memory(self, memory_id: str, user_id: int, content: str,
                    memory_type: str, importance: float = 0.5,
                    emotion: str = None, context: Dict = None):
        """Simpan memori"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                INSERT INTO memories 
                (id, user_id, content, memory_type, importance, emotion, context,
                 created_at, last_accessed, access_count)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                memory_id, user_id, content, memory_type, importance,
                emotion, json.dumps(context) if context else None,
                datetime.now(), datetime.now(), 0
            ))
            conn.commit()
    
    def get_memories(self, user_id: int, limit: int = 50) -> List[Dict]:
        """Ambil memori user"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                SELECT * FROM memories 
                WHERE user_id = ?
                ORDER BY importance DESC, last_accessed DESC
                LIMIT ?
            ''', (user_id, limit))
            return [dict(row) for row in c.fetchall()]
    
    # ===== STATS METHODS =====
    
    def get_total_users(self) -> int:
        """Total users"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('SELECT COUNT(*) FROM users')
            return c.fetchone()[0]
    
    def get_total_messages(self) -> int:
        """Total messages"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('SELECT COUNT(*) FROM conversations')
            return c.fetchone()[0]
    
    def get_total_climax(self) -> int:
        """Total climax"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('SELECT COUNT(*) FROM climax_history')
            return c.fetchone()[0]
    
    def get_today_messages(self) -> int:
        """Messages hari ini"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                SELECT COUNT(*) FROM conversations 
                WHERE date(timestamp) = date('now')
            ''')
            return c.fetchone()[0]
    
    def get_all_users(self) -> List[int]:
        """Semua user ID"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('SELECT user_id FROM users')
            return [row[0] for row in c.fetchall()]
    
    def get_db_stats(self) -> Dict:
        """Statistik database"""
        return {
            'users': self.get_total_users(),
            'messages': self.get_total_messages(),
            'climax': self.get_total_climax(),
            'today_messages': self.get_today_messages()
        }
        
    # ===== AI STATE METHODS =====
    
    def save_ai_state(self, admin_id: int, state: dict) -> bool:
        """Simpan AI state"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                INSERT OR REPLACE INTO ai_states (admin_id, state, updated_at)
                VALUES (?, ?, CURRENT_TIMESTAMP)
            ''', (admin_id, json.dumps(state)))
            conn.commit()
            return True
    
    def load_ai_state(self, admin_id: int) -> Optional[dict]:
        """Load AI state"""
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('SELECT state FROM ai_states WHERE admin_id = ?', (admin_id,))
            row = c.fetchone()
            if row:
                return json.loads(row[0])
            return None
