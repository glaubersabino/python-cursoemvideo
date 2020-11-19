# Exercício 066
# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e
# qual foi a soma entre elas (desconsiderando o flag).

n = int(input('Digite um número inteiro: '))
s = c = 0
while n != 999:
    c += 1
    s += n
    if n == 999:
        break
    else:
        n = int(input('Digite um número inteiro: '))
print(f'''
=> A quantidade de números digitados foi de {c}.
=> A soma entre eles foi de {s}.
''')
