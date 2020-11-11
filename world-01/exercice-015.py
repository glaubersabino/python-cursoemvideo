# Exercício 015
# Escreva um programa que pergunta a quantidade de KM percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$60.00
# por dia e R$0.15 por KM rodado.

km = float(input('Quantos KM foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
total = dias * 60 + km * 0.15

print('O carro foi alugado por {} dias e percorreu {:.2f}km. O valor a ser pago é de R${:.2f} reais.'.format(dias, km, total))