# Exercício 027
# Faça um programa que leia o nome completo de uma pessoa, mosrtando em
# seguida o primeiro e o último nome separadamente.

name = str(input('Informe o seu nome: '))
nameList = name.split()
first = nameList[0]
last = nameList[len(nameList) - 1]

print('Seu nome é {}'.format(name))
print('Seu primeiro nome é {}'.format(first))
print('Seu último nome é {}'.format(last))