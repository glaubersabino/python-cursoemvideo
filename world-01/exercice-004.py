# Exercício 004
# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele.

info = input('Digite alguma coisa: ')

print('Tipo primitivo é {}'.format(type(info)))
print('Só tem espaços: {}'.format(info.isspace()))
print('É um número: {}'.format(info.isnumeric()))
print('É alfabético: {}'.format(info.isalpha()))
print('É alfanúmerico: {}'.format(info.isalnum()))
print('Está maiúsculo: {}'.format(info.isupper()))
print('É minúsculo: {}'.format(info.islower()))
print('É capitalizada: {}'.format(info.istitle()))
