# encrypt_password.py
import bcrypt

def hash_password(password: str) -> str:
    """Hashes a password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def is_valid(hashed_password: str, password: str) -> bool:
    """Validates a password against a given hash."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
