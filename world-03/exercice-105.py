# Exercício 105
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(* notas, situacao=True):
    """
    FUNÇÃO PARA ANALISAR AS NOTAS E SITUAÇÃO DE VÁRIOS ALUNOS.

    :param notas: Uma ou mais notas(Aceita várias)
    :param situacao: Parâmetro opcional, indica se deve mostrar a situação do aluno.
    :return: Retorna um dicionário com as informações do aluno.
    """
    total = len(notas)
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)
    aluno = {'total': total, 'maior': maior, 'menor': menor, 'media': float(format(media, '.2f'))}

    if situacao:
        if media < 5:
            aluno['situacao'] = 'Reprovado'
        elif media < 7:
            aluno['situacao'] = 'Recuperação'
        else:
            aluno['situacao'] = 'Aprovado'

    return aluno


resp1 = notas(2, 5.5, 6, 8)
resp2 = notas(8, 7, 8.5, 9.75, situacao=False)
print(resp1)
print(resp2)
