# Exercício 074
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

t = ()

for c in range(0, 5):
    n = (randint(1, 10),)
    t = t + n

maior = max(t)
menor = min(t)

print(f'''
=> Listagem da Tupla = {t}.
=> Menor número da tupla é {menor}.
=> Maior número da tupla é {maior}.
''')
