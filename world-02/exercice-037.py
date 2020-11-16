# Exercício 037
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 - Binário : 2 - octal : 3 - hexadecimal

num = int(input('Informe um número inteiro: '))
print('Selecione qual será a base de conversão:\n1 => Binário\n2 => Octal\n3 = > Hexadecimal')
num = int(input('=> '))
bin = bin(num)
oct = oct(num)
hex = hex(num)

if num == 1:
    print('{} em binário é {}.'.format(num, bin))
elif num == 2:
    print('{} em Octal é {}.'.format(num, oct))
elif num == 3:
    print('{} em binário é {}.'.format(num, hex))
else:
    print('Opção incorreta. Tente novamente.')
