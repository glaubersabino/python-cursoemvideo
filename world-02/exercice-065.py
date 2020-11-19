# Exercício 065
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
# entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
# se ele quer ou não continuar a digitar valores.

go = True
soma = maior = menor = c = 0

while go:
    n = int(input('Informe um número inteiro: '))
    c += 1
    soma += n

    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    msg = str(input('Você deseja continuar[S/N]?')).upper()
    if msg not in 'SN':
        print('Opção inválida! Tente novamente.')
        msg = str(input('Você deseja continuar[S/N]?')).upper()
    elif msg == 'N':
        go = False

print('''Foram digitados {} números.
=> A média de {}/{} é {}.
=> O maior valor digitado foi {}.
=> O menor valor digitado foi {}.
'''.format(c, soma, c, (soma/c), maior, menor))
