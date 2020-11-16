# Exercício 045
# Crie um programa que faça o computador jogar Jokenpô com você.

import random

print('1 => Pedra\n2 => Papel\n3 => Tesoura')
user = int(input('Informe a opção: '))
computer = random.randrange(1, 4)
print("COMPUTADOR ====> ",  computer)

if user == computer:
    print('Houve um empate.')
elif user == 1:
    if computer == 3:
        print('Você ganhou!')
    else:
        print('O computador ganhou!')
elif user == 2:
    if computer == 1:
        print('Você ganhou!')
    else:
        print('O computador ganhou!')
elif user == 3:
    if computer == 2:
        print('Você ganhou!')
    else:
        print('O computador ganhou!')
else:
    print('O valor informado está incorreto.')

