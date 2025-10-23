from src.utils import mod_inv, mod_pow

P = 257
Q = 263
N = P * Q
Z = (P - 1) * (Q - 1)
E = 523
D = mod_inv(E, Z)

def crip(m: int) -> int:
    if not (0 <= m < N):
        raise ValueError("Mensagem fora do intervalo válido (0 <= m < N)")
    return mod_pow(m, E, N)

def decrip(c: int) -> int:
    if not (0 <= c < N):
        raise ValueError("Cifra fora do intervalo válido (0 <= c < N)")
    return mod_pow(c, D, N)
