# Exercício 055
# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for c in range(0, 5):
    peso = float(input('Qual o peso da pessoa {}? '.format(c + 1)))
    if peso > maior:
        maior = peso
    if c == 0:
        menor = peso
    elif peso < menor:
        menor = peso

print('O maior peso é {} e o menor peso é {}.'.format(maior, menor))
