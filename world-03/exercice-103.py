# Exercício 103
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='desconhecido', gols=0):
    print(f'O JOGADOR {nome.upper()} FEZ {gols} GOL(S) NO CAMPEONATO.')

n = str(input('> INFORME O SEU NOME: '))
g = str(input('> QUANTOS GOLS MARCOU? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)