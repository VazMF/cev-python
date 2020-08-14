#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em 
#um dicionário. No final, coloque esses resultados em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
print('-' * 30)
print(f'{"< JOGO DOS DADOS >":^30}') #titulo
print('-' * 30)
jogadas = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
           'jogador3': randint(1, 6), 'jogador4': randint(1, 6)} #dicionario com 4 jogadores e cada jogador randomiza um numero de 1 a 6
ranking = list() #inicializa uma lista de ranking
for k, v in jogadas.items(): #repeticao para cada chave e valores nos itens de jogadas
    print(f'{k} tirou \033[35m{v}\033[m') #print informando a jogada
    sleep(1) #sleep de 1s
print(f'-' * 10, "RANKING", '-' * 10) #print de resultado
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking): #repeticao para cada indice e valor na lista ranking
    print(f'{i+1}° Lugar - {v[0]} com {v[1]} ptos') #print do ranking
    sleep(1)
print('-' * 30)
