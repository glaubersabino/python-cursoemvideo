# Exercício 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Informe o preço do produto: '))
desc = preco - (preco * 0.05)

print('Você está comprando um produto que custa {} e terá {} de desconto(5%).'.format(preco, desc))