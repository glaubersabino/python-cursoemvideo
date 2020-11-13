# Exercício 021
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# 6.127 vai mostrar 6.

from math import trunc

num = float(input('Informe um número real: '))
int = trunc(num)

print('O número inteiro de {} é {}.'.format(num, int))
