#Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar  descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário ganhou ou perdeu. #aula10 CONDIÇÕES EM PYTHON
from time import sleep
from random import randint
print('\033[31m---JOGO DA ADIVINHAÇÃO---\033[m') #titúlo
p = int(input('De 0 a 5, em qual número acha que estou pensando? ')) #input do número na variavel p
r = randint(0, 5) #o computador pensa/sorteia um número pelo randint
print('\033[32mPROCESSANDO...\033[m')
sleep(2)
if p == r:
    print(f'\033[33mParabéns! você acertou, Eu pensei justamente no número {r}!\033[m')
else:
    print(f'\033[31mGAME OVER, você perdeu! Na verdade eu pensei no número {r}\033[m.')
