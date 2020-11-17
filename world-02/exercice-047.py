# Exercício 047
# Crie um programa que mostre na tela todos os números pares que estão no
# intervalo entre 1 e 50.

# for c in range(2, 51, 2)
for c in range(1, 51):
    isPar = c % 2
    if isPar == 0:
        print(c)