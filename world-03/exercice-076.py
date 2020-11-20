# Exercício 076
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('Caderno', 3.45, 'Lápis', 2, 'Caneta', 1.5, 'Mochila', 50, 'Lapizeira', 2.63, 'Borracha', 0.56, 'Transferidor', 0.5, 'Régua', 1.95)

print('=' * 50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('=' * 50)

for n in range(0, len(lista), 2):
    point = 50 - (len(lista[n]) + 11)
    print('{0!s:<}'.format(lista[n]), '.' * point, 'R$', '{0:6.2f}'.format(lista[n + 1]))
    # print('.' * 30)