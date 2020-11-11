# Exercício
# Desenvolva um programa que leia as duas notas
# de um aluno, calcule e mostre a sua média.

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2

print('A média entre {} e {} é {:.2f}.'.format(n1, n2, media))