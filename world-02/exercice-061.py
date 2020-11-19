# Exercício 061
# Refaça o DESAFIO 51, lendo o primeiro zão dtermo e a rae uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
decimo = termo + (10 - 1) * razao

c = termo
while c <= decimo:
    print(c)
    c += razao
