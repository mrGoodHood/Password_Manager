from cryptography.fernet import Fernet
import os

FERNET_KEY = os.environ.get("FERNET_KEY").encode()
fernet = Fernet(FERNET_KEY)


def encrypt_password(password: str) -> str:
    return fernet.encrypt(password.encode()).decode()


def decrypt_password(encrypted: str) -> str:
    return fernet.decrypt(encrypted.encode()).decode()
