from src.utils import rotate_left, convert_bytes_to_words

H0 = 0x6a09e667
H1 = 0xbb67ae85
H2 = 0x3c6ef372
H3 = 0xa54ff53a
BLOCK_SIZE = 64
ROUNDS = 16

def process_block(buffer: list, h: list) -> list:
    a = h[0]
    b = h[1]
    c = h[2]
    d = h[3]
    w = convert_bytes_to_words(buffer)

    for i in range(ROUNDS):
        f = (b & c) | ((~b) & d)
        temp = (rotate_left(a, 5) + f + d + w[i]) % 2**32
        d = c
        c = b
        b = a
        a = temp
    h0 = (h[0] + a) % 2**32
    h1 = (h[1] + b) % 2**32
    h2 = (h[2] + c) % 2**32
    h3 = (h[3] + d) % 2**32
    return [h0, h1, h2, h3]

def sha(m: str) -> str:
    buffer = [-1] * BLOCK_SIZE
    h = [H0, H1, H2, H3]
    i = 0
    msg = m.encode('utf-8')
    length = len(msg).to_bytes(8, byteorder='big')
    for byte in msg:
        if i < BLOCK_SIZE:
            buffer[i] = byte
            i += 1
        else:
            h = process_block(buffer, h)
            i = 0
            buffer[i] = byte
            i += 1
    
    buffer[i] = 0x80
    i += 1

    if i > 56:
        while i < BLOCK_SIZE:
            buffer[i] = 0x00
            i += 1
        h = process_block(buffer, h)
        i = 0
    
    while i < 56:
        buffer[i] = 0x00
        i += 1

    for byte, i in zip(length, range(i, len(buffer))):
        buffer[i] = byte * 8

    h = process_block(buffer, h) 
    final_hash = (h[0] ^ h[1] ^ h[2] ^ h[3])
    return f'0x{final_hash:08x}'

# print(sha('abc'))
# print(sha('aBc'))
# print(sha('UnB'))
# print(sha('UNB'))
# print(sha('unb'))