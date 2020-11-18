# Exercício 058
# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
# quantos palpites foram necessários para vencer.

from random import randint

p = 0
s = False
while s != True:
    comp = randint(0, 10)
    user = int(input('Digite um número inteiro de 0 a 10: '))

    if user == comp:
        print('Você venceu.')
        p += 1
        s = True
    else:
        print('O computador venceu! Tente novamente.')
        p += 1

print('Foram necessários {} palpites para você vencer!'.format(p))
