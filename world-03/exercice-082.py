# Exercício 082
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []

while True:
    n = int(input('Digite um número inteiro: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    msg = str(input('Você deseja continuar[S/N]? ')).upper()
    while msg not in 'SN':
        print('Opção inválida! Tente novamente.')
        msg = str(input('Você deseja continuar[S/N]? ')).upper()

    if msg == 'N':
        break
print(f'''
LISTA COMPLETA => {lista}
LISTA DE PARES => {pares}
LISTA DE ÍMPARES => {impares}
''')
