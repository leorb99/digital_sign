def mod_inv(a: int, b: int) -> int:
    #https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    gcd, r, alpha, s, beta, t = a, b, 1, 0, 0, 1

    while r != 0:
        q = gcd // r
        gcd, r = r, gcd - q * r
        alpha, s = s, alpha - q * s
        beta, t = t, beta - q * t
    if gcd != 1:
        raise ValueError("E e Z devem ser coprimos.")
    return alpha % b

def mod_pow(base: int, exp: int, mod: int) -> int:
    #https://en.wikipedia.org/wiki/Modular_exponentiation
    if mod == 1:
        return 0
    c = 1
    for _ in range(exp):
        c = (c * base) % mod
    return c

def rotate_left(n: int, bits: int) -> int:
    bits %= 32
    return ((n << bits) | (n >> (32 - bits))) & 0xFFFFFFFF

def convert_bytes_to_words(bytes: list[int]) -> list[int]:
    if len(bytes) != 64:
        raise ValueError("A lista deve ter exatamente 64 elementos (bytes).")
    
    words = [(
        (bytes[i] << 24) | 
        (bytes[i+1] << 16) | 
        (bytes[i+2] << 8) | 
        bytes[i+3]
    ) for i in range(0, len(bytes), 4)]
    
    return words