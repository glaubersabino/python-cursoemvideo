# Exercício 026
# Faça um programa que leia uma frase pelo teclado e mostre:
# 1 - Quantas vezes aparece a letra "A".
# 2 - Em que posição ela aparece a primeira vez.
# 3 - Em qual posição ela aparece a última vez.

frase = str(input('Digite uma frase: '))
q1 = frase.upper().count('A')
q2 = frase.upper().find('A')
q3 = frase.upper().rfind('A')

print('Quantas vezes aparece a letra "A"? \n{}'.format(q1))
print('Em que posição ela aparece a primeira vez? \n{}'.format(q2))
print('Em qual posição ela aparece a última vez? \n{}'.format(q3))
