# Exercicio 113
# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um
# número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(text):
    while True:
        try:
            n = int(input(text))
        except (TypeError, ValueError):
            print('\033[0;31m=> ERRO! INFORME UM NÚMERO INTEIRO.\033[m')
        except KeyboardInterrupt:
            print('\033[0;33m=> ERRO! O USUÁRIO FINALIZOU O PROGRAMA PELO TECLADO.\033[m')
            break
        else:
            return n
            break


def leiaFloat(text):
    while True:
        try:
            n = float(input(text))
        except (TypeError, ValueError):
            print('\033[0;31m=> ERRO! INFORME UM NÚMERO REAL.\033[m')
        except KeyboardInterrupt:
            print('\033[0;33m=> ERRO! O USUÁRIO FINALIZOU O PROGRAMA PELO TECLADO.\033[m')
            break
        else:
            return n
            break


inteiro = leiaInt('DIGITE UM NÚMERO INTEIRO > ')
flutuante = leiaFloat('DIGITE UM NÚMERO REAL > ')
print(f'VOCÊ ACABOU DE DIGITAR O NÚMERO INTEIRO {inteiro} E O REAL {flutuante}.')