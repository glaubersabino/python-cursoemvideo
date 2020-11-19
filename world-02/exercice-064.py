# Exercício 064
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
# usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = 0
c = True
count = 0

while c:
    n = int(input('Digite um número inteiro[999 para finalizar]: '))
    if n == 999:
        c = False
    else:
        count += 1
        soma += n

print('Você informou {} números e a soma deles é igual a {}.'.format(count, soma))