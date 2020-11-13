# Exercício 019
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

aluno01 = str(input('Informe o nome do primeiro aluno: '))
aluno02 = str(input('Informe o nome do segundo aluno: '))
aluno03 = str(input('Informe o nome do terceiro aluno: '))
aluno04 = str(input('Informe o nome do quarto aluno: '))

lista = [aluno01, aluno02, aluno03, aluno04]

print('O escolhido foi {}.'.format(choice(lista)))
