"""
AI STATE MANAGER - Persistence untuk state AI
"""

import json
import logging
from datetime import datetime
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class AIStateManager:
    """
    Manajer state AI untuk persistence
    
    Fitur:
    - Save emotional state
    - Load emotional state
    - History tracking
    """
    
    def __init__(self, db, admin_id: int):
        self.db = db
        self.admin_id = admin_id
        self.last_save = None
    
    async def save_state(self, brain) -> bool:
        """
        Simpan state AI ke database
        
        Args:
            brain: Brain instance
            
        Returns:
            True jika berhasil
        """
        try:
            state = {
                "admin_id": self.admin_id,
                "emotional_vector": brain.emotion.current.to_dict(),
                "personality": brain.personality.tolist(),
                "consciousness_stats": brain.consciousness.get_stats(),
                "memory_count": brain.memory.count(),
                "last_active": datetime.now().isoformat(),
                "interaction_count": brain.interaction_count
            }
            
            # Simpan ke database (table ai_states)
            await self._save_to_db(state)
            
            self.last_save = datetime.now()
            logger.info(f"✅ AI state saved. Memories: {brain.memory.count()}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to save AI state: {e}")
            return False
    
    async def load_state(self, brain) -> bool:
        """
        Load state AI dari database
        
        Args:
            brain: Brain instance
            
        Returns:
            True jika berhasil
        """
        try:
            state = await self._load_from_db()
            
            if not state:
                logger.info("No previous AI state found")
                return False
            
            # Load emotional vector
            from core.emotional_vector import EmotionalVector
            brain.emotion.current = EmotionalVector.from_dict(state["emotional_vector"])
            
            # Load interaction count
            brain.interaction_count = state.get("interaction_count", 0)
            
            logger.info(f"✅ AI state loaded. Previous interactions: {brain.interaction_count}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to load AI state: {e}")
            return False
    
    async def _save_to_db(self, state: Dict):
        """Internal: simpan ke database"""
        # Buat table jika belum ada
        await self._ensure_table()
        
        # Convert to JSON
        state_json = json.dumps(state)
        
        # Simpan
        conn = self.db._get_conn()
        try:
            c = conn.cursor()
            c.execute('''
                INSERT OR REPLACE INTO ai_states (admin_id, state, updated_at)
                VALUES (?, ?, CURRENT_TIMESTAMP)
            ''', (self.admin_id, state_json))
            conn.commit()
        finally:
            conn.close()
    
    async def _load_from_db(self) -> Optional[Dict]:
        """Internal: load dari database"""
        await self._ensure_table()
        
        conn = self.db._get_conn()
        try:
            c = conn.cursor()
            c.execute('''
                SELECT state FROM ai_states WHERE admin_id = ?
            ''', (self.admin_id,))
            row = c.fetchone()
            
            if row:
                return json.loads(row[0])
            return None
        finally:
            conn.close()
    
    async def _ensure_table(self):
        """Pastikan table ada"""
        conn = self.db._get_conn()
        try:
            c = conn.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS ai_states (
                    admin_id INTEGER PRIMARY KEY,
                    state TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
        finally:
            conn.close()
