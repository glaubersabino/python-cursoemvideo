# Exercício 075
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

t = ()
count = 0
par = ()
while count < 4:
    n = int(input('Informe um número: '))
    if n % 2 == 0:
        par += (n,)
    t = t + (n,)
    count += 1

findThree = t.index(3) if 3 in t else 'inexistente'

print(f'''
=> O número 9 apareceu {t.count(9)} vezes.
=> 3 apareceu na posição {findThree}.
=> Os números pares digitados foram {par}.
''')
