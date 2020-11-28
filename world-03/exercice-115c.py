# Exercicio 115b
# Vamos criar um menu em Python, usando modularização.

from time import sleep
from modulos.exercice115.menu import menu
import modulos.exercice115.database as database

database.create()
opc = menu()

while opc != 3:
    if opc == 1:
        database.show()
        sleep(1)
    elif opc == 2:
        database.insert()
        sleep(1)
    opc = menu()
