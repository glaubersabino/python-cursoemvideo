# Exercício 081
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    n = int(input('Digite um número inteiro: '))
    lista.append(n)

    msg = str(input('Você deseja continuar[S/N]? ')).upper()
    while msg not in 'SN':
        print('Opção inválida! Tente novamente.')
        msg = str(input('Você deseja continuar[S/N]? ')).upper()

    if msg == 'N':
        lista.sort(reverse=True)
        break

print(f'=> Foram digitados {len(lista)} números.')
print(f'=> Lista ordenada de forma decrescente:\n{lista}')
if 5 in lista:
    print(f'O número 5 consta na lista na posição {lista.index(5)}')
else:
    print('O número 5 não consta na lista.')