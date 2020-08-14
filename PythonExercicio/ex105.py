#Faça um programa que tenha uma função nostas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: - Quantidade de notas, - A maior nota; - A menor nota; - A média da turma; - A situação(opcional); Adicionando também as doctrings da função.
#DEFININDO A FUNÇÃO
def notas(* n, sit=False): #define a função notas com um numero indeterminado de notas como parâmetro e o parâmetro sit como false
    #DOCSTRING
    """
    -> Funcao para analisar notas e situacoes de varios alunos
    :param n: aceita varias notas de alunos
    :param sit: valor opcional indicando se deve ou nao mostrar a situacao
    :return: dicionario com varias infromacoes sobre a turma
    """
    r = dict() #inicializa um dicionário vázio r
    r['total'] = len(n) #indice total do dicionário recebe tamanho da lista parâmetro n
    r['maior'] = max(n) #indice maior do dicionário recebe o valor max da lista parâmetro n
    r['menor'] = min(n) #indice menor do dicionário recebe o valor min da lista parâmtro n
    r['media'] = sum(n)/len(n) #indice media do dicionário recebe a soma dos valores de n dividido pelo tamanho
    if sit: #se a situação for true
        if r['media'] >= 7: #se a media for maior ou igual a sete
            r['situação'] = 'BOA' #indice situação no dicionário recebe boa
        elif r['media'] >= 5: #se a média for maior ou igual a 5
            r['situação'] = 'RAZOÁVEL' #indice situação no dicionário recebe razoavel
        else: #senao
            r['situação'] = 'RUIM' #indice situação recebe ruim
    return r #retotna o dicionário r
 


#PROGRAMA PRINCIPAL
resp = notas(7.5, 8.5, 1.5, sit=True) #variavel resposta recebe a função notas com os parâmetros
print(resp) #print o conteúdo da variável resposta
help(notas) #função help para ver a docstring da função criada
