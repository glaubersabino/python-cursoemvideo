# Exercício 06
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Informe um número: '))
double = num * 2
triple = num * 3
square = num**(1/2)

print('O número informado foi {}.\nO dobro dele é {}.\nO triplo dele é {}.\nA raiz quadrada dele é {:.2f}.'.format(num, double, triple, square))