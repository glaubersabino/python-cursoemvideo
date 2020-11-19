# Exercício 067
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    opc = int(input('Digite um número inteiro: '))
    if opc < 0:
        print('Tabuada encerrada. Obrigado por utilizar nosso software.')
        break
    else:
        print(f'===== TABUADA DE {opc} =====')
        for c in range(1, 11):
            total = opc * c
            print(f'{opc} x {c} = {total}')
