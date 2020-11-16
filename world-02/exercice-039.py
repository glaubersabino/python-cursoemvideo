# Exercício 039
# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

birth = int(input('Em qual ano você nasceu? '))
year = date.today().year
age = year - birth
ageAlis = 18

if age == ageAlis:
    print('É hora de se alistar no serviço militar!')
elif age < ageAlis:
    print('Você ainda vai se alistar no serviço militar. Faltam {} ano(s).'.format(ageAlis - age))
else:
    print('Você passou do tempo para se alistar no serviço militar. Você está atrasado em {} anos.'.format(age - ageAlis))


