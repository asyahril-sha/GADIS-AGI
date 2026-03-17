"""
GADIS AGI ULTIMATE V3.0
Root package initialization
"""

__version__ = '3.0.0'
__author__ = 'GADIS Team'
__description__ = 'Ultimate AI Companion with 9 Roles and HTS/FWB System'

from config import Config
from database import Database

__all__ = ['Config', 'Database']
