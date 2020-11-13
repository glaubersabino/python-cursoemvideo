# Exercício 020
# O mesmo professor do desafio anterior quer sortear a ordem de
# apresentação de trabalhos dos alunos. Faça um programa que leia
# o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

aluno01 = str(input('Informe o nome do primeiro aluno: '))
aluno02 = str(input('Informe o nome do segundo aluno: '))
aluno03 = str(input('Informe o nome do terceiro aluno: '))
aluno04 = str(input('Informe o nome do quarto aluno: '))

lista = [aluno01, aluno02, aluno03, aluno04]
shuffle(lista)

print('Os trabalhos serão apresentados na seguinte sequência: ')
print('1 -> {}\n2 -> {}\n3 -> {}\n4 -> {}'.format(lista[0], lista[1], lista[2], lista[3]))