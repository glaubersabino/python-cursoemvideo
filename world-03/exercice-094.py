# Exercício 094
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em
# um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = []

while True:
    nome = str(input('QUAL É O SEU NOME? '))
    sexo = str(input('QUAL É O SEU SEXO [M/F]? ')).upper()
    while sexo not in 'MF':
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
        sexo = str(input('QUAL É O SEU SEXO [M/F]? ')).upper()
    idade = int(input('QUAL A SUA IDADE? '))

    pessoa = {'nome': nome, 'sexo': sexo, 'idade': idade}
    pessoas.append(pessoa)

    msg = str(input('VOCÊ DESEJA CONTINUAR [S/N]? ')).upper()
    while msg not in 'SN':
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
        msg = str(input('VOCÊ DESEJA CONTINUAR [S/N]? ')).upper()
    if msg == 'N':
        break

print('*' * 50)
print(f'=> A QUANTIDADE DE PESSOAS CADASTRADAS FOI DE {len(pessoas)}.')
s = 0
for c in pessoas:
    s += c['idade']
print(f'=> A MÉDIA DE IDADE DAS {len(pessoas)} PESSOAS É DE {s / len(pessoas)}.')
print(f'=> LISTA DE MULHERES CADASTRADAS:')
for m in pessoas:
    if m['sexo'] == 'F':
        print(f'--> {m["nome"]}')
print(f'=> LISTA DE PESSOAS COM IDADE ACIMA DA MÉDIA:')
for a in pessoas:
    if a['idade'] > (s / len(pessoas)):
        print(f'--> NOME: {a["nome"]} / SEXO: {a["sexo"]} / IDADE: {a["idade"]}.')
