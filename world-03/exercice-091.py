# Exercício 091
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

results = {}

for c in range(0, 4):
    dado = randint(1, 6)
    results[f"JOGADOR{c + 1}"] = dado
    print(f'O JOGADOR{c + 1} TIROU {dado} NO DADO.')
    sleep(1)

ranking = sorted(results.items(), key=itemgetter(1), reverse=True)

print('=> RANKING DOS JOGADORES <=')
for k, v in enumerate(ranking):
    print(f'{k + 1}º LUGAR => {v[0]} COM {v[1]} PONTOS.')
    sleep(1)
