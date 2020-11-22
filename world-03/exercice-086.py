# Exercício 086
# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]
count = 1
for pos, c in enumerate(matriz):
    for m in range(0, 3):
        num = int(input(f'Digite o {count} número [{pos}, {m}]: '))
        matriz[pos].append(num)
        count += 1

for m in matriz:
    print(f'{m}')