# Exercício 100
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
# mostrar a soma entre todos os valores pares sorteados pela função anterior.

def sorteia(lista):
    print('SORTEANDO NÚMEROS...')
    for c in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        print(num, end=' ')
        sleep(1)
    print()


def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A SOMA DOS VALORES PARES DE {lista} É {soma}.')


from random import randint
from time import sleep

numeros = []

sorteia(numeros)
somaPar(numeros)
