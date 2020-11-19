# Exercício 062
# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
size = termo + (10 - 1) * razao
c = termo
counter = 0
while c <= size:
    print(c)
    c += razao
    counter += 1
    if counter == 10:
        more = int(input('Quantos termos a mais que você quer? '))
        while more > 0:
            c = size + razao
            size = size + (more * razao)
            while c <= size:
                print(c)
                c += razao
            more = int(input('Quantos termos a mais que você quer? '))


