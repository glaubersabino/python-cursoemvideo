# Exercício 042
# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))

cond1 = (r1 + r2) > r3
cond2 = (r1 + r3) > r2
cond3 = (r3 + r2) > r1

if cond1 == True and cond2 == True and cond3 == True:
    print('Os valores {}, {} e {} formam um triângulo.'.format(r1, r2, r3))

    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Os valores informados não formam um triângulo.')

