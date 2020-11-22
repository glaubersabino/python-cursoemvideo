# Exercício 087
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[], [], []]
count = 1
a = 0
b = 0
for pos, c in enumerate(matriz):
    for m in range(0, 3):
        num = int(input(f'Digite o {count} número [{pos}, {m}]: '))
        if num % 2 == 0:
            a += num
        matriz[pos].append(num)
        count += 1

print('*' * 50)
print('{:^50}'.format('MATRIZ'))
for m in matriz:
    print(f'{m}')
print('*' * 50)

print(f'=> A soma de todos os valores pares é {a}.')
for c in matriz:
    b += c[2]
print(f'=> A soma dos valores da terceira coluna é {b}.')
print(f'=> O maior valor da segunda linha é {max(matriz[1])}.')
