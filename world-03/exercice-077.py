# Exercício 077
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

words = ('crie', 'programa', 'tenha', 'tupla', 'acentos', 'depois', 'mostrar', 'para', 'vogais')

for w in words:
    vogais = ()
    for v in w:
        if v in 'aeiou':
            vogais = vogais + (v,)
    print(f'Na palavra {w.upper()} temos {vogais}.')
