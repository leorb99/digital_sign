import sys

from rsa import crip, decrip

if len(sys.argv) < 2:
    print("Você deve inserir o caminho para um arquivo ou algum texto plano.")
    sys.exit(1)
    
input = sys.argv[1]
m = ''

try:
    with open(input, 'r', encoding='utf-8') as f:
        m = f.read()
except FileNotFoundError:
    m = input

m = int.from_bytes(m.encode('utf-8'), byteorder='big') % (31*29)
print(m)
c = crip(m)
print(c)

m = decrip(c)
print(c)
print(m)