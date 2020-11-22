# Exercício 088
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos
# serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

mega = []

q = int(input('Quantos jogos você quer gerar? '))
for c in range(0, q):
    game = []
    for n in range(0, 6):
        game.append(randint(1, 60))
    mega.append(game)

for pos, game in enumerate(mega):
    print(f'Sorteando jogo {pos + 1}...')
    sleep(1)
    print(game)
