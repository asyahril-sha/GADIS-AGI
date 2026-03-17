import sqlite3
import json
import logging
from contextlib import contextmanager
from datetime import datetime

logger = logging.getLogger(__name__)

class Database:
    """Database manager untuk semua data"""
    
    def __init__(self, db_path):
        self.db_path = db_path
        self._init_db()
        
    def _init_db(self):
        with self._get_conn() as conn:
            c = conn.cursor()
            
            # Users table
            c.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    first_name TEXT,
                    role TEXT,
                    level INTEGER DEFAULT 1,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_active TIMESTAMP
                )
            ''')
            
            # Relationships table (HTS/FWB)
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
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_called TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                )
            ''')
            
            # Conversations table
            c.execute('''
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    position TEXT,
                    location TEXT,
                    dominance_level INTEGER,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                )
            ''')
            
            # Climax history table
            c.execute('''
                CREATE TABLE IF NOT EXISTS climax_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    unique_id TEXT NOT NULL,
                    climax_type TEXT NOT NULL,
                    position TEXT,
                    area TEXT,
                    intensity REAL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (unique_id) REFERENCES relationships(unique_id)
                )
            ''')
            
            # Ranking table
            c.execute('''
                CREATE TABLE IF NOT EXISTS ranking (
                    rank INTEGER PRIMARY KEY AUTOINCREMENT,
                    unique_id TEXT UNIQUE NOT NULL,
                    total_climax INTEGER DEFAULT 0,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (unique_id) REFERENCES relationships(unique_id)
                )
            ''')
            
            conn.commit()
            logger.info("✅ Database initialized")
            
    @contextmanager
    def _get_conn(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()
            
    def save_user(self, user_id, username, first_name, role, level=1):
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                INSERT OR REPLACE INTO users 
                (user_id, username, first_name, role, level, last_active)
                VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ''', (user_id, username, first_name, role, level))
            conn.commit()
            
    def save_relationship(self, unique_id, user_id, jenis, role, bot_name, level=1):
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                INSERT OR REPLACE INTO relationships 
                (unique_id, user_id, jenis, role, bot_name, level, last_called)
                VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ''', (unique_id, user_id, jenis, role, bot_name, level))
            conn.commit()
            
    def update_relationship(self, unique_id, **kwargs):
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
            
    def get_relationships(self, user_id, jenis=None):
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
            
    def get_relationship(self, unique_id):
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM relationships WHERE unique_id = ?', (unique_id,))
            row = c.fetchone()
            return dict(row) if row else None
            
    def save_conversation(self, user_id, role, content, position=None, location=None, dominance_level=None):
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                INSERT INTO conversations 
                (user_id, role, content, position, location, dominance_level)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (user_id, role, content, position, location, dominance_level))
            conn.commit()
            
    def save_climax(self, unique_id, climax_type, position=None, area=None, intensity=1.0):
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                INSERT INTO climax_history 
                (unique_id, climax_type, position, area, intensity)
                VALUES (?, ?, ?, ?, ?)
            ''', (unique_id, climax_type, position, area, intensity))
            conn.commit()
            
    def update_ranking(self, unique_id, total_climax):
        with self._get_conn() as conn:
            c = conn.cursor()
            c.execute('''
                INSERT OR REPLACE INTO ranking (unique_id, total_climax)
                VALUES (?, ?)
            ''', (unique_id, total_climax))
            conn.commit()
            
    def get_top_ranking(self, limit=10):
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
