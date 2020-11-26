# Exercício 099
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(* num):
    print('ANALISANDO OS VALORES INFORMADOS...')
    print(f'FORAM INFORMADOS {len(num)} VALORES AO TODO.')
    for c in num:
        print(c, end=' ')
        sleep(1)
    print()
    if len(num) > 0:
        print(f'=> O MAIOR NÚMERO INFORMADO FOI {max(num)}.')
    else:
        print('=> O MAIOR NÚMERO INFORMADO FOI 0.')


maior(1, 8, 3, 4)
maior(1, 8, 3, 4, 9, 14, 2, 1)
maior(1, 1, 3)
maior()
