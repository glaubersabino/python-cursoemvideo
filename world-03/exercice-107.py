# Exercicio 107
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from modulos import exercice107

n = int(input('> DIGITE UM NÚMERO: '))
print(f'=> O DOBRO DE {n} É {exercice107.dobro(n)}.')
print(f'=> A METADE DE {n} É {exercice107.metade(n)}.')
print(f'=> AUMENTO DE 10% DE {n} É {exercice107.aumentar(n, 10)}.')
print(f'=> REDUÇÃO DE 13% DE {n} É {exercice107.diminuir(n, 13)}.')
