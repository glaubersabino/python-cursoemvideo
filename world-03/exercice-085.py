# Exercício 085
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]

for c in range(0, 7):
    n = int(input('Informe um número inteiro: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

lista[0].sort()
lista[1].sort()

print(f'''
=> Os números pares são {lista[0]}.
=> Os números impares são {lista[1]}.
''')