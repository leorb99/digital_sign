def mdc(a: int, b: int) -> int:
    if b == 0:
        return a
    return mdc(b, a % b)

def mod_inv(a: int, b: int):
    #https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    gcd, r, alpha, s, beta, t = a, b, 1, 0, 0, 1

    while r != 0:
        q = gcd // r
        gcd, r = r, gcd - q * r
        alpha, s = s, alpha - q * s
        beta, t = t, beta - q * t
    return alpha, beta, gcd, t, s

