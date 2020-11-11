# Exercício 011
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

lar = float(input('Informe a largura da parede em metros: '))
alt = float(input('Informe a altura da parede em metros: '))
area = lar * alt
qtd = area / 2

print('A área de uma parede com {}m de largura e {}m de altura é igual a {}m². Será necessário {:.2f} litros de tinta para pintá-la.'.format(lar, alt, area, qtd))
