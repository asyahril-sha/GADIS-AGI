"""
HELPER FUNCTIONS - Utility functions untuk bot
"""

import random
import re
import hashlib
from datetime import datetime, timedelta
from typing import Union, Optional, List, Dict, Any

def format_time_ago(timestamp: Union[datetime, str, None]) -> str:
    """
    Format timestamp menjadi 'X menit yang lalu'
    
    Args:
        timestamp: Datetime atau string timestamp
        
    Returns:
        String waktu yang lalu
    """
    if not timestamp:
        return "tidak diketahui"
    
    if isinstance(timestamp, str):
        try:
            timestamp = datetime.fromisoformat(timestamp)
        except:
            return "tidak diketahui"
    
    delta = datetime.now() - timestamp
    seconds = int(delta.total_seconds())
    
    if seconds < 10:
        return "baru saja"
    elif seconds < 60:
        return f"{seconds} detik yang lalu"
    elif seconds < 3600:
        minutes = seconds // 60
        return f"{minutes} menit yang lalu"
    elif seconds < 86400:
        hours = seconds // 3600
        return f"{hours} jam yang lalu"
    else:
        days = seconds // 86400
        return f"{days} hari yang lalu"

def sanitize_message(message: str) -> str:
    """
    Bersihkan pesan dari karakter berbahaya
    
    Args:
        message: Pesan input
        
    Returns:
        Pesan yang sudah dibersihkan
    """
    if not message:
        return ""
    message = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', message)
    return message[:2000]

def truncate_text(text: str, max_length: int = 100) -> str:
    """
    Potong teks jika terlalu panjang
    
    Args:
        text: Teks input
        max_length: Panjang maksimal
        
    Returns:
        Teks yang sudah dipotong
    """
    if not text or len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."

def get_random_reaction() -> str:
    """
    Dapatkan reaksi random
    
    Returns:
        String reaksi
    """
    reactions = [
        "*tersenyum*", "*tersipu*", "*tertawa kecil*", "*mengangguk*",
        "*mengedip*", "*merona*", "*melongo*", "*berpikir*",
        "*menghela napas*", "*tersenyum manis*", "*nyengir*",
        "*menggigit bibir*", "*menunduk*", "*menatap tajam*",
        "*berbisik*", "*memeluk diri sendiri*", "*menggeleng*"
    ]
    return random.choice(reactions)

def create_progress_bar(percentage: float, length: int = 10) -> str:
    """
    Buat progress bar visual
    
    Args:
        percentage: Nilai 0-1
        length: Panjang bar
        
    Returns:
        String progress bar
    """
    filled = int(percentage * length)
    return "▓" * filled + "░" * (length - filled)

def generate_unique_id(jenis: str, role: str, user_id: int, counter: int) -> str:
    """
    Generate unique ID untuk HTS/FWB
    
    Args:
        jenis: 'HTS' atau 'FWB'
        role: Nama role
        user_id: ID user
        counter: Nomor urut
        
    Returns:
        Unique ID string
    """
    date_str = datetime.now().strftime("%d%m%y")
    user_suffix = str(user_id)[-4:]
    counter_str = f"{counter:03d}"
    return f"{jenis}-{role.upper()}-{user_suffix}-{date_str}-{counter_str}"

def parse_duration(duration_str: str) -> Optional[int]:
    """
    Parse string durasi ke detik
    
    Args:
        duration_str: String seperti '30m', '2h', '1d'
        
    Returns:
        Durasi dalam detik atau None
    """
    if not duration_str:
        return None
    
    duration_str = duration_str.lower().strip()
    match = re.match(r'^(\d+)([smhd])$', duration_str)
    if not match:
        return None
    
    value = int(match.group(1))
    unit = match.group(2)
    
    if unit == 's':
        return value
    elif unit == 'm':
        return value * 60
    elif unit == 'h':
        return value * 3600
    elif unit == 'd':
        return value * 86400
    return None

def get_time_based_greeting() -> str:
    """
    Dapatkan greeting berdasarkan waktu
    
    Returns:
        String greeting
    """
    hour = datetime.now().hour
    
    if hour < 5:
        return "Selamat dini hari"
    elif hour < 11:
        return "Selamat pagi"
    elif hour < 15:
        return "Selamat siang"
    elif hour < 18:
        return "Selamat sore"
    else:
        return "Selamat malam"

def is_command(text: str) -> bool:
    """
    Cek apakah teks adalah command
    
    Args:
        text: Teks input
        
    Returns:
        True jika command
    """
    return text.startswith('/') if text else False

def extract_command(text: str) -> Optional[str]:
    """
    Ekstrak command dari teks
    
    Args:
        text: Teks input
        
    Returns:
        Nama command atau None
    """
    if not text or not text.startswith('/'):
        return None
    parts = text.split()
    return parts[0][1:]

def format_number(num: int) -> str:
    """
    Format angka dengan pemisah ribuan
    
    Args:
        num: Angka
        
    Returns:
        String terformat
    """
    return f"{num:,}".replace(",", ".")

def safe_divide(a: float, b: float, default: float = 0) -> float:
    """
    Pembagian aman dengan handling division by zero
    
    Args:
        a: Pembilang
        b: Penyebut
        default: Nilai default
        
    Returns:
        Hasil pembagian
    """
    try:
        return a / b if b != 0 else default
    except:
        return default

def chunk_list(lst: List, chunk_size: int):
    """
    Bagi list menjadi potongan-potongan kecil
    
    Args:
        lst: List input
        chunk_size: Ukuran potongan
        
    Yields:
        Potongan list
    """
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

def calculate_bmi(height_cm: int, weight_kg: int) -> float:
    """
    Hitung BMI
    
    Args:
        height_cm: Tinggi dalam cm
        weight_kg: Berat dalam kg
        
    Returns:
        Nilai BMI
    """
    if height_cm <= 0:
        return 0
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)

def get_bmi_category(bmi: float) -> str:
    """
    Dapatkan kategori BMI
    
    Args:
        bmi: Nilai BMI
        
    Returns:
        Kategori BMI
    """
    if bmi < 18.5:
        return "Kurus"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Gemuk"
    else:
        return "Obesitas"

def md5_hash(text: str) -> str:
    """
    Buat MD5 hash dari teks
    
    Args:
        text: Teks input
        
    Returns:
        Hash string
    """
    return hashlib.md5(text.encode()).hexdigest()

def dict_to_json(d: Dict) -> str:
    """
    Konversi dictionary ke JSON string
    
    Args:
        d: Dictionary
        
    Returns:
        JSON string
    """
    import json
    return json.dumps(d, ensure_ascii=False)

def json_to_dict(s: str) -> Dict:
    """
    Konversi JSON string ke dictionary
    
    Args:
        s: JSON string
        
    Returns:
        Dictionary
    """
    import json
    try:
        return json.loads(s)
    except:
        return {}
