# Exercício 090
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

name = str(input('Qual é o seu nome? '))
media = float(input('Qual a sua média? '))
status = ''
if media < 5:
    status = 'Reprovado'
elif media >= 5 and media < 7:
    status = 'Recuperação'
else:
    status = 'Aprovado'

alunos = {'nome': name, 'media': media, 'status': status}
for k, v in alunos.items():
    print(f'=> O {k} é igual a {v}.')

