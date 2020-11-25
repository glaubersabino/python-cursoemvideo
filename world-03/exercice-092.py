# Exercício 092
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

nome = str(input('QUAL É O SEU NOME? '))
nascimento = int(input('QUAL O ANO DO SEU NASCIMENTO? '))
idade = datetime.today().year - nascimento
ctps = int(input('QUAL O NÚMERO DA SUA CTPS [0 SE NÃO TIVER]? '))

inss = {'nome': nome, 'idade': idade, 'ctps': ctps}

if ctps != 0:
    contratacao = int(input('QUAL O ANO DE CONTRATAÇÃO? '))
    salario = float(input('QUAL O SEU SALÁRIO? '))
    aposentadoria = (contratacao + 35) - nascimento
    inss['contratacao'] = contratacao
    inss['salario'] = salario
    inss['aposentadoria'] = aposentadoria

for k, v in inss.items():
    print(f'=> {k} tem o valor de {v}.')
