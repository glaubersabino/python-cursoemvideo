# Exercício 095
# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
# de detalhes do aproveitamento de cada jogador.

jogadores = []

while True:
    nome = str(input('QUAL É O NOME DO JOGADOR? ')).upper()
    partidas = int(input(f'QUANTAS PARTIDAS {nome} JOGOU? '))
    gols = []
    total = 0
    for c in range(0, partidas):
        g = int(input(f'QUANTOS GOLS {nome} NA PARTIDA {c + 1}? '))
        gols.append(g)
        total += g
    jogador = {'nome': nome, 'gols': gols, 'total': total}
    jogadores.append(jogador)

    msg = str(input('VOCÊ DESEJA CONTINUAR [S/N]? ')).upper()
    while msg not in 'SN':
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
        msg = str(input('VOCÊ DESEJA CONTINUAR [S/N]? ')).upper()
    if msg == 'N':
        break

print('=' * 50)
print('{:^50}'.format('LISTAGEM DE JOGADORES'))
print('=' * 50)
print('{0:<4}'.format('COD'), '{0:<15}'.format('NOME'), '{0:<23}'.format('GOLS'), '{0:>4}'.format('TOTAL'))
print('-' * 50)
for k, v in enumerate(jogadores):
    space = 24 - (len(v['gols']) * 3)
    print('{0:<4}'.format(k), '{0:<15}'.format(v['nome']), '{}'.format(v['gols']), ' ' * int(space), '{}'.format(v['total']))
print('-' * 50)

msg = 0
while msg != 999:
    msg = int(input('ESCOLHA O JOGADOR PARA DETALHAR [999 PARA PARAR]: '))

    if msg >= 0 and msg < len(jogadores):
        print(f'DETALHES SOBRE O JOGADOR {jogadores[msg]["nome"]}')
        for k, v in enumerate(jogadores[msg]['gols']):
            print(f'=> NO JOGO {k + 1} ELE FEZ {v} GOL(S).')
    elif msg == 999:
        print('SOFTWARE ENCERRADO! VOLTE SEMPRE!')
    else:
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE.')
