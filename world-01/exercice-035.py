# Exercício 035
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo.

r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))

cond1 = (r1 + r2) > r3
cond2 = (r1 + r3) > r2
cond3 = (r3 + r2) > r1

if r1 == True and r2 == True and r3 == True:
    print('Os valores {}, {} e {} formam um triângulo.'.format(r1, r2, r3))
else:
    print('Os valores informados não formam um triângulo.')
