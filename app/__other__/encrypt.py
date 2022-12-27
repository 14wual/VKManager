from cryptography.fernet import Fernet

def encrypt(password: str) -> bytes:
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return (encrypted_password, key)