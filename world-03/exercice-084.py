# Exercício 084
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

db = []
maior = []
menor = []

while True:
    nome = str(input('Qual é o seu nome? '))
    peso = float(input('Qual é o seu peso? '))
    pessoa = [nome, peso]
    db.append(pessoa)

    msg = str(input('Você deseja continuar[S/N]? ')).upper()
    while msg not in 'SN':
        print('Opção inválida! Tente novamente.')
        msg = str(input('Você deseja continuar[S/N]? ')).upper()
    if msg == 'N':
        break

for pos, pessoa in enumerate(db):
    if pos == 0:
        maior.append(pessoa)
        menor.append(pessoa)
    else:
        if pessoa[1] > maior[0][1]:
            maior[0] = pessoa
        elif pessoa[1] < menor[0][1]:
            menor[0] = pessoa

print(f'=> Foram cadastradas {len(db)} pessoas.')
print(f'=> A pessoa mais pesada é {maior[0][0]} com {maior[0][1]}Kg.')
print(f'=> A pessoa mais leve é {menor[0][0]} com {menor[0][1]}Kg.')