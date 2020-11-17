# Exercício 046
# Faça um programa que calcule a soma entre todos os números ímpares que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.

s = 0
for c in range(1, 501):
    isImpar = c % 2
    if isImpar != 0:
        s += c

print('A soma dos números ímpares é {}.'.format(s))