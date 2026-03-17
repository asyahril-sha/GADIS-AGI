"""
EMOTIONAL SCHEDULER - Update emosi periodik
"""

import asyncio
import logging
import random
from datetime import datetime
from typing import Optional

logger = logging.getLogger(__name__)

class EmotionalScheduler:
    """
    Penjadwal update emosi
    
    Fitur:
    - Emotional decay over time
    - Random mood swings
    - Memory-triggered emotions
    """
    
    def __init__(self, emotion_engine):
        self.emotion = emotion_engine
        self.last_update = datetime.now()
        self.update_interval = 300  # 5 menit
        self.running = False
    
    async def start(self):
        """Mulai scheduler"""
        self.running = True
        self.last_update = datetime.now()
        
        while self.running:
            await asyncio.sleep(self.update_interval)
            await self._tick()
    
    async def _tick(self):
        """Update periodik"""
        now = datetime.now()
        hours_passed = (now - self.last_update).total_seconds() / 3600
        
        if hours_passed > 0:
            # Emotional decay
            self.emotion.decay(hours_passed)
            
            # Random mood swing (30% chance)
            if random.random() < 0.3:
                events = ["nostalgia", "longing", "hope", "anxiety"]
                event = random.choice(events)
                self.emotion.process_event(event, 0.1)
                logger.debug(f"Random mood swing: {event}")
            
            # Memory-triggered emotions (10% chance)
            if random.random() < 0.1:
                self.emotion.process_event("memory_happy", 0.1)
            
            self.last_update = now
            logger.debug(f"Emotional tick completed. Hours passed: {hours_passed:.2f}")
    
    async def stop(self):
        """Hentikan scheduler"""
        self.running = False
        logger.info("Emotional scheduler stopped")
