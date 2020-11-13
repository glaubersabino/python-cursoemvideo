# Exercício 018
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

ang = float(input('Informe o ângulo: '))
seno = sin(radians(ang))
cose = cos(radians(ang))
tang = tan(radians(ang))

print('Para o ângulo de 30º temos:\nSeno => {}, Cosseno => {}, Tangente => {}'.format(seno, cose, tang))