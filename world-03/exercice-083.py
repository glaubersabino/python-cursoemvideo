# Exercício 083
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = str(input('Digite uma expressão que use parênteses: ')).strip().replace(' ', '')
expression = []

for l in exp:
    if l == '(':
        expression.append('(')
    elif l == ')':
        if len(expression) > 0:
            expression.pop()
        else:
            expression.append(')')
            break
if len(expression) == 0:
    print('=> A expressão está correta!')
else:
    print('=> A expressão está incorreta!')
