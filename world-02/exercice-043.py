# Exercício 043
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa
# Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade morbida

from math import pow

peso = float(input('Informe o seu peso: '))
alt = float(input('Informe a sua altura: '))
imc = peso / pow(alt, 2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade morbida')
