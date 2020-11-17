# Exercício 054
# Crie um programa que leia o ano de nascimento de sete pessoas
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maior = 0
menor = 0
ano = date.today().year

for c in range(0, 7):
    nasc = int(input('Qual o ano que a pessoa {} nasceu? '.format(c + 1)))
    if ano - nasc >= 18:
        maior += 1
    else:
        menor += 1

print('''
{}/7 pessoas são maiores de idade.
{}/7 pessoas são menores de idade.
'''.format(maior, menor))