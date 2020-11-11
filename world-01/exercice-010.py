# Exercício 010
# Crie um programa que leia quanto dinheiro uma pessoa tem
# na carteira e mostre quantos dólares ela pode comprar. Considere USS 1.00 = R$ 3.27

money = float(input('Quanto você tem na carteira? '))
uss = money / 3.27

print('Com {} reais, você pode comprar {:.2f} dólares.'.format(money, uss))
