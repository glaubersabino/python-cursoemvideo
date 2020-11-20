# Exercício 073
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Corinthians.

serieA = ('Atlético-MG', 'Internacional', 'São Paulo', 'Flamengo', 'Palmeiras', 'Santos', 'Grêmio', 'Fluminense', 'Bahia', 'Athletico-PR', 'Sport Recife', 'Fortaleza', 'Corinthians', 'Ceará SC', 'Atlético-GO', 'Vasco da Gama', 'Bragantino', 'Coritiba', 'Botafogo', 'Goiás')

firstFive = serieA[:5]
lastFour = serieA[-4:]
alpha = sorted(serieA)
cor = serieA.index('Corinthians') + 1

print(f'''
=> Os 5 primeiros times são {firstFive}.
=> Os últimos 4 são {lastFour}.
=> Lista de times ordenados alfabeticamente: {alpha}.
=> O Corinthians está em {cor}º.
''')