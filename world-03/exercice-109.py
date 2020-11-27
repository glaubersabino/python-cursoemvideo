# Exercicio 109
# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

from modulos import exercice107
from modulos import exercice108

n = int(input('> DIGITE UM NÚMERO: '))
print(f'=> O DOBRO DE {exercice108.moeda(n)} É {exercice107.dobro(n, f=True)}.')
print(f'=> A METADE DE {exercice108.moeda(n)} É {exercice107.metade(n, f=True)}.')
print(f'=> AUMENTO DE 10% DE {exercice108.moeda(n)} É {exercice107.aumentar(n, 10, f=True)}.')
print(f'=> REDUÇÃO DE 13% DE {exercice108.moeda(n)} É {exercice107.diminuir(n, 13, f=True)}.')
