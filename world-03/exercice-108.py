# Exercicio 108
# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os
# números como um valor monetário formatado.

from modulos import exercice107
from modulos import exercice108

n = int(input('> DIGITE UM NÚMERO: '))
print(f'=> O DOBRO DE {exercice108.moeda(n)} É {exercice108.moeda(exercice107.dobro(n))}.')
print(f'=> A METADE DE {exercice108.moeda(n)} É {exercice108.moeda(exercice107.metade(n))}.')
print(f'=> AUMENTO DE 10% DE {exercice108.moeda(n)} É {exercice108.moeda(exercice107.aumentar(n, 10))}.')
print(f'=> REDUÇÃO DE 13% DE {exercice108.moeda(n)} É {exercice108.moeda(exercice107.diminuir(n, 13))}.')
