from src.sha import sha
from src.rsa import decrip

def validator(m: str, signature: str) -> bool:
    if not signature.startswith('0x'):
        raise ValueError('A assinatura deve estar no formato de número hexadecimal (0x12abcdef)')
    decrypt = f'0x{(decrip(int(signature, 16))):08x}'
    digest = sha(m)
    return decrypt == digest
