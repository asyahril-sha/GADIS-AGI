"""
REQUEST QUEUE - Mencegah overload dan async conflict
"""

import asyncio
import logging
from collections import deque
from typing import Callable, Any

logger = logging.getLogger(__name__)

class RequestQueue:
    """
    Antrian request untuk mencegah overload
    
    Fitur:
    - Max concurrent requests
    - Queue untuk pending requests
    - Auto-process
    """
    
    def __init__(self, max_concurrent: int = 3):
        self.queue = deque()
        self.current = 0
        self.max_concurrent = max_concurrent
        self.lock = asyncio.Lock()
        self.total_processed = 0
        self.total_errors = 0
    
    async def process(self, update: Any, handler: Callable, context: Any = None) -> bool:
        """
        Masukkan request ke queue
        
        Returns:
            True jika berhasil diqueue
        """
        self.queue.append((update, handler, context))
        logger.debug(f"Request queued. Queue size: {len(self.queue)}")
        
        # Proses queue
        asyncio.create_task(self._process_queue())
        return True
    
    async def _process_queue(self):
        """Proses antrian"""
        async with self.lock:
            if self.current >= self.max_concurrent:
                return
            
            while self.queue and self.current < self.max_concurrent:
                update, handler, context = self.queue.popleft()
                self.current += 1
                asyncio.create_task(self._handle(update, handler, context))
    
    async def _handle(self, update, handler, context):
        """Handle single request"""
        try:
            logger.debug(f"Processing request. Active: {self.current}")
            await handler(update, context)
            self.total_processed += 1
        except Exception as e:
            logger.error(f"Error processing request: {e}")
            self.total_errors += 1
        finally:
            self.current -= 1
            asyncio.create_task(self._process_queue())
    
    def get_stats(self) -> dict:
        """Dapatkan statistik queue"""
        return {
            "queue_size": len(self.queue),
            "active": self.current,
            "max_concurrent": self.max_concurrent,
            "total_processed": self.total_processed,
            "total_errors": self.total_errors
        }
