# Exercício 097
# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
# mostre uma mensagem com tamanho adaptável. Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def escreva(texto):
    size = len(texto) + 6
    print('~' * size)
    print(f'{texto:^{size}}')
    print('~' * size)

escreva('Curso de Python - Mundo 03')