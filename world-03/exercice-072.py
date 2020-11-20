# Exercício 072
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    opc = int(input('Digite um número entre 0 e 20: '))

    while True:
        if opc > 0 and opc <= 20:
            break
        else:
            print('Opção inválida! Tente novamente.')
            opc = int(input('Digite um número entre 0 e 20: '))

    print(f'Você digitou {opc} => {num[opc]}.')
