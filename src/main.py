import sys
from sha import sha
from rsa import crip, decrip

op = None
while op not in [1, 2, -1]:
    op = int(input('Escolha a funcionalidade: \n1 - assinar documento ou texto plano\n2 - validar assinatura\n-1 - sair\n'))
    if op == 1:
        source = input('Insira o caminho para o arquivo ou o texto plano\n')
        try:
            with open(source, 'r', encoding='utf-8') as f:
                m = f.read()
        except FileNotFoundError:
            m = source
        digest = sha(m)
        encrypt = hex(crip(int(digest, 16)))
        print(f'Texto original:\n{m}')
        print(f'Resumo criptografado:\n{encrypt}')

    elif op == 2:
        m = input('Insira a mensagem:\n')
        signature = input('Insira o resumo criptografado:\n')
        digest = sha(m)
        encrypt = hex(crip(int(digest, 16)))
        if encrypt == signature:
            print('Assinatura é válida!')
        else:
            print('Assinatura inválida!')

    elif op == -1:
        sys.exit(1)
    
    else:
        print('Opção inválida!')
        