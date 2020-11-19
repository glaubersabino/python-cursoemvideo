# Exercício 068
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

win = 0

while True:
    player = int(input('Digite um número: '))
    opc = str(input('Par ou Ímpar[P/I]? ')).upper()
    comp = randint(0, 10)
    result = player + comp

    while opc not in 'PI':
        print('Opção inválida! Tente novamente.')
        opc = str(input('Par ou Ímpar[P/I]? ')).upper()

    if result % 2 == 0:
        if opc == 'P':
            win += 1
            print(f'=> Você venceu! Parabéns!\n=> {player} + {comp} = {result} ==> PAR')
    else:
        print(f'=> Game Over! Hahahahah\n=> {player} + {comp} = {result} ==> ÍMPAR')
        break
print(f'Você conseguiu vencer {win} vezes consecutivas.')
