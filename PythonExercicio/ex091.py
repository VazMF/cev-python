#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em 
#um dicionário. No final, coloque esses resultados em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

print('-' * 30)
print(f'{"JOGO DOS DADOS":^30}')
print('-' * 30)
jogadas = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
           'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = list()
for k, v in jogadas.items():
    print(f'{k} tirou \033[35m{v}\033[m')
    sleep(1)
print(f'-' * 10, "RANKING", '-' * 10)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° Lugar - {v[0]} com {v[1]} ptos')
    sleep(1)
print('-' * 30)
