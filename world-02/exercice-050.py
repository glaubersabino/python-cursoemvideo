# Exercício 046
# Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

s = 0
for c in range(0, 6):
    n = int(input('Informe um número inteiro: '))
    isPar = n % 2
    if isPar == 0:
        s += n

print('O resultado da soma dos números pares é {}.'.format(s))