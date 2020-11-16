# Exercício 044
# Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

produto = float(input('Informe o valor do produto: '))
print('Formas de pagamento: \n1 => À vista dinheiro/cheque\n2 => À vista no cartão\n3 => Em até 2x no cartão\n4 => 3x ou mais no cartão')
pgmt = int(input('Digite a forma de pagamento: '))

formPg1 = produto - (produto * 0.1)
formPg2 = produto - (produto * 0.05)
formPg3 = produto
formPg4 = produto + (produto * 0.2)

if pgmt == 1:
    print('O valor a ser pago é de {:.2f} reais.'.format(formPg1))
elif pgmt == 2:
    print('O valor a ser pago é de {:.2f} reais.'.format(formPg2))
elif pgmt == 3:
    print('O valor a ser pago é de {:.2f} reais.'.format(formPg3))
elif pgmt == 4:
    print('O valor a ser pago é de {:.2f} reais.'.format(formPg4))
else:
    print('Forma de pagamento incorreta, tente novamente.')



