# Exercicio 112
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e
# mantenha tudo funcionando.

from modulos.utilidadescev import dado, moeda

resp = dado.leiaDinheiro('=> DIGITE UM VALOR(DINHEIRO): ')
moeda.resumo(resp, 15, 10)
