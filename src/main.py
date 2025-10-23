from src.signer import signer
from src.validator import validator

op = None
while op != -1:
    op = int(input('Escolha a funcionalidade: \n1 - assinar documento ou texto plano\n2 - validar assinatura\n-1 - sair\n'))
    if op == 1:
        source = input('Insira o caminho para o arquivo ou o texto plano\n')
        m, encrypt = signer(source)
        print(f'Texto original:\n{m}')
        print(f'Resumo criptografado:\n{encrypt}')

    elif op == 2:
        source = input('Insira a mensagem ou o caminho para o arquivo:\n')
        signature = input('Insira o resumo criptografado:\n')
        try:
            with open(source, 'r', encoding='utf-8') as f:
                m = f.read()
        except FileNotFoundError:
            m = source
        if validator(m, signature):
            print('Assinatura é válida!\n')
        else:
            print('Assinatura inválida!\n')

    else:
        if op == -1:
            break
        print('Opção inválida!')
