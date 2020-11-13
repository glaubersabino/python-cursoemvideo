# Exercício 032
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Informe um ano no formato(XXXX): '))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano não é BISSEXTO.')