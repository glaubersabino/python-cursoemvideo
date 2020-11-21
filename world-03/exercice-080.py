# Exercício 080
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0:
        lista.append(n)
        print(f'Valor adicionado a posição {c}')
    else:
        p = 0
        for pos, num in enumerate(lista):
            if n > num:
                p = pos + 1

        lista.insert(p, n)
        print(f'Valor adicionado a posição {p}')

print(f'''
=> LISTA ORDENADA DE FORMA CRESCENTE SEM SORT().\n{lista}
''')
