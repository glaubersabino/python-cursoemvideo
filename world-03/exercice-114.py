# Exercicio 114
# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.request


def checkURL(url):
    try:
        status = urllib.request.urlopen(url).getcode()
    except Exception as error:
        print(f'UM ERRO INESPERADO ACONTECEU!\n{error}.')
    else:
        if status == 200:
            print(f'O SITE {url} ESTÁ ONLINE!')
        else:
            print(f'HOUVE UM PROBLEMA PARA ACESSAR O SITE.\nHTTP CODE => {status}')


url = "https://www.google.com"

checkURL(url)
