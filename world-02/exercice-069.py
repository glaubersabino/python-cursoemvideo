# Exercício 069
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

plus18 = 0
male = 0
wUnder20 = 0

while True:
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual é o seu sexo[M/F]? ')).upper()

    while sexo not in 'MF':
        print('Opção inválida! Tente novamente.')
        sexo = str(input('Qual é o seu sexo[M/F]? ')).upper()

    if idade > 18:
        plus18 += 1
    else:
        if sexo == 'F':
            wUnder20 += 1
    if sexo == 'M':
        male += 1

    opc = str(input('Você deseja continuar[S/N]? ')).upper()
    while opc not in 'SN':
        print('Opção inválida! Tente novamente.')
        opc = str(input('Você deseja continuar[S/N]? ')).upper()

    print('=' * 50)

    if opc == 'N':
        break

print(f'''
{plus18} pessoas tem mais de 18 anos.
{male} homens foram cadastrados.
{wUnder20} mulheres tem menos de 20 anos.
''')