# Exercício 022
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1 - O nome com todas as letras maiúsculas
# 2 - O nome com todas minúsculas
# 3 - Quantas letras ao todo (sem considerar espaços)
# 4 - Quantas letras tem o primeiro nome

name = str(input('Qual é o seu nome completo? '))
ma = name.upper()
mi = name.lower()
onlyLetters = name.replace(' ', '')
firstName = name.split()

print('Seu nome é: {}'.format(name))
print('Maiúsculo: {}'.format(ma))
print('Minúsculo: {}'.format(mi))
print('Contagem de letras: {}'.format(len(onlyLetters)))
print('Contagem primeira palavra: {}'.format(len(firstName[0])))