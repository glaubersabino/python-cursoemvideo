# Exercício 028
# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual o número escolhido
# pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

num = int(input('Digite um número de 0 a 5: '))
bingo = random.randrange(0, 5)

if num == bingo:
    print('Você acertou!')
else:
    print('Você errou, tente novamente!')
