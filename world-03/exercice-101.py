# Exercício 101
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date

def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        print(f'=> VOCÊ TEM {idade} ANOS. VOTO NEGADO!')
    elif idade < 18 or idade > 59:
        print(f'VOCÊ TEM {idade}. VOTO OPCIONAL!')
    else:
        print(f'VOCÊ TEM {idade}. VOTO OBRIGATÓRIO!')

nasc = int(input('QUAL O ANO DO SEU NASCIMENTO? '))
voto(nasc)