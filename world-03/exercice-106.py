# Exercício 106
# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

def ajuda(text):
    size = len(text) + 36

    print('\033[1:30:44m*' * size)
    print(f'{"ACESSANDO O MANUAL DO COMANDO " + text:^{size}}')
    print('*' * size)
    print('\033[m', end='')

    print('\033[7;30m')
    help('print')
    print('\033[m')


h = str(input('INFORME O COMANDO / FUNÇÃO QUE DESEJA CONSULTAR > '))
while h.upper() != 'FIM':
    ajuda(h)
    h = str(input('INFORME O COMANDO / FUNÇÃO QUE DESEJA CONSULTAR > '))

