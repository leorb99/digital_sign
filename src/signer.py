from src.sha import sha
from src.rsa import crip

def signer(m: str) -> tuple[str, str]:
    try:
        with open(m, 'r', encoding='utf-8') as f:
            m = f.read()
    except FileNotFoundError:
        pass
    digest = sha(m)
    encrypt = hex(crip(int(digest, 16)))
    return m, encrypt
