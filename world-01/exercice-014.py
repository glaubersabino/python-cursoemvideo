# Exercício 014
# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

temp = float(input('Informe a temperatura em ºC(Celsius): '))
f = (temp * 9/5) + 32

print('A conversão de {:.2f}ºC para Fahrenheit é {:.2f}ºF.'.format(temp, f))