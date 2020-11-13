# Exercício 025
# Crie um programa qe leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Informe o nome da pessoa: '))

if "SILVA" in nome.upper():
    print('A pessoa tem SILVA no nome')
else:
    print('A pessoa não tem SILVA no nome.')