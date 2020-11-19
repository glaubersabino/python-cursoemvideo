# Exercício 070
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = 0
more1000 = 0
less = 0
expensive = ''
c = 0

while True:
    nome = str(input('=> Informe o nome do produto: '))
    preco = float(input('=> Informe o preço do produto: '))

    total += preco
    if preco > 1000:
        more1000 += 1

    if c == 0:
        less = preco
        expensive = nome
        c += 1
    else:
        if preco < less:
            less = preco
            expensive = nome

    msg = str(input('Você deseja continuar[S/N]? ')).upper()
    while msg not in 'SN':
        print('Opção inválida! Tente novamente.')
        msg = str(input('Você deseja continuar[S/N]? ')).upper()

    print('=' * 50)

    if msg == 'N':
        break

print(f'''
O total gasto na compra foi de {total:.2f}
{more1000} produtos custaram mais de R$1000.
O produto mais barato foi {expensive}, custando {less}.
''')
