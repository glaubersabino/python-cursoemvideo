# Exercício 056
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No Final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

idadeCount = 0
idadeMaior = 0
idadeMaiorNome = ''
less20 = 0

for c in range(0, 4):
    nome = str(input('Qual é seu nome? '))
    idade = int(input('Qual é a sua idade? '))
    sexo = str(input('Qual é o seu sexo(M ou F)? '))

    idadeCount += idade

    if idadeMaior < idade and sexo == 'M':
        idadeMaior = idade
        idadeMaiorNome = nome
    if sexo == 'F' and idade < 20:
        less20 += 1

print('''
A média de idade do grupo é de {}.
O nome do homem mais velho é {}.
A quantidade de mulheres com menos de 20 anos é de {}.
'''.format(idadeCount / 4, idadeMaiorNome, less20))
