# Exercício 053
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

word = str(input('Informe uma frase: '))
newWord = word.upper().replace(' ','')
palindromo = ''

for c in range((len(newWord) - 1), -1, -1):
    palindromo += newWord[c]

if newWord == palindromo:
    print('A frase {} é um palíndromo.'.format(word))
else:
    print('Não é um palíndromo.')
