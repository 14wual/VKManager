# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV1.3.8
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

from cryptography.fernet import Fernet

def encrypt(password: str) -> bytes:
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return (encrypted_password, key)
