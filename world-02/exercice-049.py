# Exercício 049
# Rafaça o desafio 009 mostrando a tabuada de um número que o usuário
# escolher,só que agora utilizando um laço for.

num = int(input('Informe um número: '))

print('TABUADA DE {}.'.format(num))
for c in range(1, 11):
    total = c * num
    print('{} x {} = {}'.format(c, num, total))