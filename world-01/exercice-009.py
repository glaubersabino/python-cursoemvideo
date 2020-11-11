# Exercício 009
# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada.

num = int(input('Informe um número inteiro: '))

print('Tabuada de {}.'.format(num))
print('{} x 1 = {}\n'.format(num, num * 1),
      '{} x 2 = {}\n'.format(num, num * 2),
      '{} x 3 = {}\n'.format(num, num * 3),
      '{} x 4 = {}\n'.format(num, num * 4),
      '{} x 5 = {}\n'.format(num, num * 5),
      '{} x 6 = {}\n'.format(num, num * 6),
      '{} x 7 = {}\n'.format(num, num * 7),
      '{} x 8 = {}\n'.format(num, num * 8),
      '{} x 9 = {}\n'.format(num, num * 9),
      '{} x 10 = {}'.format(num, num * 10)
      )
