# Exercício 029
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
# 80KM/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar
# R$7,00 por cada KM acima do limite.

velo = int(input('Informe a velocidade do carro: '))

if velo > 80:
    print('Você foi multado em R${:.2f}'.format((velo - 80) * 7))
else:
    print('Parabéns, continue respeitando as normas de trânsito.')