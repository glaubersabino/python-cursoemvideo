# Exercício 078
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for c in range(0, 5):
    n = int(input('Digite um número inteiro: '))
    lista.append(n)

print(f'''
=> O maior número é {max(lista)} e ele se encontra na posição {lista.index(max(lista))}.
=> O menor número é {min(lista)} e ele se encontra na posição {lista.index(min(lista))}.
''')