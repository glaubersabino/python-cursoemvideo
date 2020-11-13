# Exercício 017
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import pow

co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))
hipo = pow(co, 2) + pow(ca, 2)

print('O valor da hipotenusa é de {}.'.format(hipo))
