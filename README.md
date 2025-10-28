# Trabalho 1 de Segurança Computacional

## Implementação de assinador digital
Este projeto implementa um sistema de assinatura digital baseado nos algoritmos RSA e SHA (versão simplificada). \
O objetivo é demonstrar, de forma didática, o funcionamento da criptografia assimétrica e da verificação de integridade de mensagens.

### Estrutura 
```bash
src/
├── main.py/
├── rsa.py/
├── sha.py/
├── signer.py/
├── utils.py/
├── validator.py/
```
### Execução
Na pasta do projeto use  ```python -m src.main``` para executar o programa.

### Descrição
+ O SHA simplificado gera um resumo de 16 bits da mensagem.
+ O resumo é criptografado com RSA (chave privada) para gerar a assinatura.
+ O validador descriptografa a assinatura e compara com o hash original.

### Observação

As chaves RSA são definidas estaticamente (hard coded) para fins didáticos, garantindo resultados reprodutíveis. 