# Exercício 060
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

num = int(input('Informe um número por favor: '))
fact = factorial(num)

print('O número informado foi {} e o seu fatorial é {}.'.format(num, fact))