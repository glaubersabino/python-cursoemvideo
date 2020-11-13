# Exercício 030
# Crie um programa que leia um número inteiro e mostre na sua tela se ele
# é PAR ou ÍMPAR.

num = int(input('Informe um número inteiro: '))

if num % 2 == 0:
    print('O número {} é PAR.'.format(num))
else:
    print('O número {} é ÍMPAR.'.format(num))