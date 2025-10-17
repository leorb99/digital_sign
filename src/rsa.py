from utils import mod_inv, mod_pow

P = 31
Q = 29
N = P * Q
Z = (P - 1) * (Q - 1)
E = 523
D = mod_inv(E, Z)[0]

def crip(m):
    return mod_pow(m, E, N)

def decrip(c):
    return mod_pow(c, D, N)
