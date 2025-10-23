from src.sha import sha
from src.rsa import decrip

def validator(m: str, signature: str) -> bool:
    decrypt = f'0x{(decrip(int(signature, 16))):04x}'
    digest = sha(m)
    return decrypt == digest
