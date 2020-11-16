# Exercício 036
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
# ele vai pagar. Calcule o valor mensal, sabendo que ela não pode exceder 30% do sálario
# ou então o empréstimo será negado.

valorCasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos você quer pagar a casa? '))
exd = salario * 0.3
prestacao = valorCasa / (anos * 12)

if prestacao >= exd:
    print('Empréstimo negado! O valor da prestação é de {:.2f} e isso corresponde 30% ou mais do seu salário.'.format(prestacao))
else:
    print('Parabéns, seu empréstimo foi aprovado! Você pagará {} parcelas de {:.3f} por total de {} referente ao imóvel.'.format((anos * 12), prestacao, valorCasa))
