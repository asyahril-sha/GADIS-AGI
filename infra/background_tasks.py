"""
BACKGROUND TASK SYSTEM - Menjalankan tugas periodik
"""

import asyncio
import logging
from typing import Dict, Callable, Optional

logger = logging.getLogger(__name__)

class BackgroundTaskManager:
    """
    Manajer tugas background
    
    Fitur:
    - Periodic tasks
    - One-time delayed tasks
    - Task cancellation
    - Error handling
    """
    
    def __init__(self):
        self.tasks: Dict[str, asyncio.Task] = {}
        self.running = True
    
    async def start_periodic(self, name: str, interval: int, coro_func, *args, **kwargs):
        """
        Jalankan tugas periodik
        
        Args:
            name: Nama tugas
            interval: Interval dalam detik
            coro_func: Coroutine function
        """
        if name in self.tasks:
            logger.warning(f"Task {name} already running")
            return
        
        async def wrapper():
            while self.running:
                try:
                    await coro_func(*args, **kwargs)
                except asyncio.CancelledError:
                    break
                except Exception as e:
                    logger.error(f"Task {name} error: {e}")
                
                await asyncio.sleep(interval)
        
        task = asyncio.create_task(wrapper(), name=name)
        self.tasks[name] = task
        logger.info(f"Started periodic task: {name} (interval: {interval}s)")
        return task
    
    async def start_delayed(self, name: str, delay: int, coro_func, *args, **kwargs):
        """
        Jalankan tugas setelah delay
        
        Args:
            name: Nama tugas
            delay: Delay dalam detik
            coro_func: Coroutine function
        """
        async def wrapper():
            try:
                await asyncio.sleep(delay)
                await coro_func(*args, **kwargs)
            except asyncio.CancelledError:
                pass
            except Exception as e:
                logger.error(f"Delayed task {name} error: {e}")
            finally:
                if name in self.tasks:
                    del self.tasks[name]
        
        task = asyncio.create_task(wrapper(), name=name)
        self.tasks[name] = task
        logger.info(f"Scheduled delayed task: {name} (delay: {delay}s)")
        return task
    
    async def cancel_task(self, name: str):
        """Batalkan tugas"""
        if name in self.tasks:
            self.tasks[name].cancel()
            try:
                await self.tasks[name]
            except:
                pass
            del self.tasks[name]
            logger.info(f"Cancelled task: {name}")
    
    async def stop_all(self):
        """Hentikan semua tugas"""
        logger.info("Stopping all background tasks...")
        self.running = False
        
        for name, task in list(self.tasks.items()):
            if not task.done():
                task.cancel()
        
        if self.tasks:
            await asyncio.gather(*self.tasks.values(), return_exceptions=True)
        
        self.tasks.clear()
        logger.info("All background tasks stopped")
