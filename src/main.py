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

# TODO integrar o SHA para gerar o resumo do input
# TODO passar o resumo para a função crip do RSA