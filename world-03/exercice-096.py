# Exercício 096
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area(largura, altura):
    area = largura * altura
    print(f'A ÁREA DO TERRENO DE {largura}X{altura} É DE {area}m².')


lar = float(input('QUAL A LARGURA DO TERRENO? '))
alt = float(input('QUAL A ALTURA DO TERRENO? '))
area(lar, alt)