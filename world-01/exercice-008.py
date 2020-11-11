# Exercício 008
# Escreva um programa que leia um valor em metros e o exiba
# convertido em centímetros e milímetros.

m = float(input('Informe um valor em metros: '))
cm = m * 100
mm = m * 1000

print('O valor de {} metros em cm é {}'.format(m, cm))
print('O valor de {} metros em mm é {}'.format(m, mm))