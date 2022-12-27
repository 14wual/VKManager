from cryptography.fernet import Fernet

def decrypt(encrypted_password: bytes, key: bytes) -> str:
    try:
        password = ""
        fernet = Fernet(key)
        password = fernet.decrypt(encrypted_password).decode()
    finally:
        return password
