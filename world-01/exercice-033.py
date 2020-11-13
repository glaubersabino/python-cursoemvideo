# Exercício 033
# Faça um programa que leia três números e mostre
# qual é o maior e qual é o menor.

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
lista = [n1, n2, n3]

print('O maior número inserido foi {}.'.format(max(lista)))
print('O menor número inserido foi {}.'.format(min(lista)))
