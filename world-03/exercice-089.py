# Exercício 089
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.

boletim = []

while True:
    nome = str(input('Qual o seu nome? '))
    nota1 = float(input('Qual a primeira nota? '))
    nota2 = float(input('Qual a segunda nota? '))
    aluno = [nome, nota1, nota2]
    boletim.append(aluno)

    msg = str(input('Deseja continuar[S/N]? ')).upper()
    if msg == 'N':
        break

print('=' * 30)
print('{:<5}{:<20}{:>5}'.format('No.', 'NOME', 'MÈDIA'))
print('=' * 30)
for pos, aluno in enumerate(boletim):
    print('{:<5}{:<20}{:>5}'.format(pos, aluno[0], (aluno[1] + aluno[2]) / 2))
while True:
    aluno = int(input('Mostra notas de qual aluno[999 encerra o programa]? '))
    if aluno == 999:
        break
    else:
        print(f'As notas de {boletim[aluno][0]} são {boletim[aluno][1:]}')
