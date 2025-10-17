def mod_inv(a: int, b: int):
    #https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    gcd, r, alpha, s, beta, t = a, b, 1, 0, 0, 1

    while r != 0:
        q = gcd // r
        gcd, r = r, gcd - q * r
        alpha, s = s, alpha - q * s
        beta, t = t, beta - q * t
    if gcd != 1:
        raise ValueError("E e Z devem ser coprimos.")
    return alpha % b, gcd

def mod_pow(base: int, exp: int, mod: int) -> int:
    #https://en.wikipedia.org/wiki/Modular_exponentiation
    if mod == 1:
        return 0
    c = 1
    for _ in range(exp):
        c = (c * base) % mod
    return c