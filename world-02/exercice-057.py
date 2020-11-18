# Exercício 057
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

c = True

while c!= False:
    sexo = str(input('Qual é o seu sexo [M/F]? '))

    if sexo not in 'MF':
        print('Valor inválido!')
    else:
        c = False
        print('O sexo informado foi {}'.format(sexo))