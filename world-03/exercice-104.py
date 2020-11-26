# Exercício 104
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(text):
    n = input(text)
    while not n.isnumeric():
        print('\033[0;31m=> ERRO! Informe um número inteiro.\033[m')
        n = input(text)
    return n


num = leiaInt('DIGITE UM NÚMERO INTEIRO > ')
print(f'VOCÊ ACABOU DE DIGITAR O NÚMERO {num}.')
