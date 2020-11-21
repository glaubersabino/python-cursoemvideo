# Exercício 079
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
# valores únicos digitados, em ordem crescente.

num = []

while True:
    n = int(input('Digite um número inteiro: '))
    if n not in num:
        num.append(n)
    else:
        while n in num:
            print('O número já consta na lista, tente novamente')
            n = int(input('Digite um número inteiro: '))

    msg = str(input('Você deseja continuar[S/N]? ')).upper()
    while msg not in 'SN':
        print('Opção inválida! Tente novamente.')
        msg = str(input('Você deseja continuar[S/N]? ')).upper()

    if msg == 'N':
        break

print(f'Lista digitada em ordem crescente:\n=> {num}')