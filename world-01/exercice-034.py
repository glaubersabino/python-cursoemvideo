# Exercício 034
# Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento.
# Para salários superiores a R$1.250.00, calcule um aumento de 10%.
# Para os inferiores ou iguais o aumento é de 15%.

salario = float(input('Qual é o seu salário? '))

if salario > 1250:
    print('Você recebia {} e agora receberá {} reais (10%).'.format(salario, salario + (salario * 0.1)))
else:
    print('Você recebia {} e agora receberá {} reais (15%).'.format(salario, salario + (salario * 0.15)))