# Exercício 013
# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe o seu salário atual: '))
novoSalario = salario + (salario * 0.15)

print('Parabéns, você ganhou um aumento! Você ganhava R${:.2f} reais e agora passará a ganhar R${:.2f} reais.'.format(salario, novoSalario))