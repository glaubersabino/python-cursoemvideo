# Exercício 098
# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def contador(inicio, fim, passo):
    print(f'=> de {inicio} até {fim}, de {abs(passo)} em {abs(passo)}')

    if fim != 0:
        if fim > 0:
            fim = fim + 1
        else:
            fim = fim - 1
        if fim < inicio:
            passo = passo - (passo * 2)
    else:
        fim = fim - 1

    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(1)
    print()

contador(1, 10, 1)
contador(10, 0, -2)

inicio = int(input('> INFORME O INÍCIO: '))
fim = int(input('> INFORME O FIM: '))
passo = int(input('> INFORME O PASSO: '))
contador(inicio, fim, passo)

