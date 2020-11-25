# Exercício 093
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

name = str(input('QUAL O NOME DO JOGADOR? ')).upper()
matches = int(input(f'QUANTAS PARTIDAS {name} JOGOU? '))
gols = []
total = 0

for c in range(0, matches):
    g = int(input(f'QUANTOS GOLS {name} FEZ NA PARTIDA {c + 1}? '))
    gols.append(g)
    total += g

data = {'nome': name, 'gols': gols, 'total': total}

print('*' * 50)
print(f'=> O NOME DO JOGADOR É {data["nome"]}')
print(f'{data["nome"]} DISPUTOU {len(data["gols"])} PARTIDAS:')
for k, v in enumerate(data['gols']):
    print(f'-> NA PARTIDA {k + 1}, FEZ {v} GOLS.')
print(f'=> SEU TOTAL DE GOLS FOI DE {total}.')


