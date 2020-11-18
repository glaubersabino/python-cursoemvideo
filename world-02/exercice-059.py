# Exercício 059
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

s = False
while s != True:
    num1 = float(input('Informe o primeiro valor: '))
    num2 = float(input('Informe o segundo valor: '))
    menu = int(input('''
    Selecione o que deseja fazer com os números informados:
    1 => SOMAR
    2 => MULTIPLICAR
    3 => MAIOR
    4 => NOVOS NÚMEROS
    5 => SAIR DO PROGRAMA
    ==> '''))

    if menu == 5:
        s = True
    elif menu == 1:
        soma = num1 + num2
        print('A soma dos números {} e {} é igual a {}.'.format(num1, num2, soma))
    elif menu == 2:
        mult = num1 * num2
        print('A multiplicação dos números {} e {} é igual a {}.'.format(num1, num2, mult))
    elif menu == 3:
        maior = num1 > num2
        if maior:
            print('O maior número entre {} e {} é {}.'.format(num1, num2, num1))
        else:
            print('O maior número entre {} e {} é {}.'.format(num1, num2, num2))
    elif menu == 4:
        print('Informe novos números...')
        sleep(1)
