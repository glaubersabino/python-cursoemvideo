# Exercicio 115
# Vamos criar um menu em Python, usando modularização.

from modulos.exercice115.menu import menu
import modulos.exercice115.database as database

database.create()
opc = menu()
