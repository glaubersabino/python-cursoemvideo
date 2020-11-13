# Exercício 027
# Desenvolva um programa que pergunte a distância de uma viagem de KM.
# Calcule o preço da passagem, cobrando R$0.50 por KM para viagens de até 200KM
# e R$0.45 para viagens mais longas.

dist = float(input('Qual foi a distância percorrida na viagem? '))

if dist <= 200:
    valor = dist * 0.50
    print('Sua viagem percorreu {:.2f}KM e custou R${:.2f} reais.'.format(dist, valor))
else:
    valor = dist * 0.45
    print('Sua viagem percorreu {:.2f}KM e custou R${:.2f} reais.'.format(dist, valor))