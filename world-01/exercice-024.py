# Exercício 024
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não
# com o nome "SANTO".

cidade = str(input('Informe o nome da cidade: '))

if cidade[0:5].upper() == "SANTO":
    print('O nome inicia com SANTO.')
else:
    print('O nome não inicia com SANTO.')