#Faça um programa que tenha uma função nostas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: - Quantidade de notas, - A maior nota; - A menor nota; - A média da turma; - A situação(opcional); Adicionando também as doctrings da função.
#DEFININDO A FUNÇÃO
def notas(* n, sit=False):
    """
    -> Funcao para analisar notas e situacoes de varios alunos
    :param n: aceita varias notas de alunos
    :param sit: valor opcional indicando se deve ou nao mostrar a situacao
    :return: dicionario com varias infromacoes sobre a turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r
 


#PROGRAMA PRINCIPAL
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
