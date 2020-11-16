# Exercício 041
# A confederação nacional de natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import date

birth = int(input('Em qual ano você nasceu? '))
year = date.today().year
age = year - birth

if age <= 9:
    print('MIRIM')
elif age > 9 and age <= 14:
    print('INFANTIL')
elif age > 14 and age <= 19:
    print('JUNIOR')
elif age == 20:
    print('SÊNIOR')
else:
    print('MASTER')