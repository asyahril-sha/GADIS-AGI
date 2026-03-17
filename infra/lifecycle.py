"""
LIFECYCLE MANAGER - Mengatur start/stop bot dengan aman
"""

import asyncio
import logging
from datetime import datetime
from typing import List, Callable

logger = logging.getLogger(__name__)

class LifecycleManager:
    """
    Manajer siklus hidup bot
    
    Fitur:
    - Graceful shutdown
    - Health check
    - Task management
    - Restart handling
    """
    
    def __init__(self):
        self.is_running = False
        self.start_time = None
        self.health_status = "starting"
        self.tasks: List[asyncio.Task] = []
        self.shutdown_hooks: List[Callable] = []
        self._shutdown_event = asyncio.Event()
    
    async def start(self, bot):
        """Mulai bot"""
        self.start_time = datetime.now()
        self.is_running = True
        self.health_status = "running"
        logger.info("🚀 Bot lifecycle started")
        
        # Monitor shutdown event
        asyncio.create_task(self._monitor_shutdown())
    
    async def _monitor_shutdown(self):
        """Monitor shutdown event"""
        await self._shutdown_event.wait()
        logger.info("🔄 Shutdown event received")
        await self.shutdown()
    
    async def shutdown(self):
        """Matikan bot dengan graceful"""
        if not self.is_running:
            return
        
        logger.info("🔄 Graceful shutdown initiated")
        self.health_status = "shutting_down"
        self.is_running = False
        
        # Panggil semua shutdown hooks
        for hook in self.shutdown_hooks:
            try:
                if asyncio.iscoroutinefunction(hook):
                    await hook()
                else:
                    hook()
            except Exception as e:
                logger.error(f"Shutdown hook error: {e}")
        
        # Cancel semua background tasks
        for task in self.tasks:
            if not task.done():
                task.cancel()
        
        if self.tasks:
            await asyncio.gather(*self.tasks, return_exceptions=True)
        
        self.health_status = "stopped"
        logger.info("✅ Bot shutdown complete")
    
    def register_shutdown_hook(self, hook: Callable):
        """Daftarkan fungsi yang akan dipanggil saat shutdown"""
        self.shutdown_hooks.append(hook)
    
    def register_task(self, task: asyncio.Task):
        """Daftarkan background task"""
        self.tasks.append(task)
    
    def health_check(self) -> dict:
        """Dapatkan status kesehatan"""
        uptime = None
        if self.start_time:
            delta = datetime.now() - self.start_time
            hours = delta.total_seconds() / 3600
            uptime = f"{hours:.1f} hours"
        
        return {
            "status": self.health_status,
            "uptime": uptime,
            "tasks": len(self.tasks),
            "running": self.is_running
        }
    
    def request_shutdown(self):
        """Minta shutdown (untuk signal handler)"""
        self._shutdown_event.set()
