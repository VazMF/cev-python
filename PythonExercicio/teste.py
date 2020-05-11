from random import choice
from time import sleep
print('\033[1;31m---JOKENPÔ---\033[m')
lista = ['PEDRA', 'PAPEL', 'TESOURA']
jogada = str(input('Faça sua jogada: ')).upper()
computador = choice(lista).upper()
print('Eu escolho \033[32m{}\033[m'.format(computador))
sleep(1)
if jogada == 'PEDRA' and computador == 'PAPEL':
    print('\033[31mGAME OVER!\033[m {} ganha de {}.'.format(computador, jogada))
elif jogada == 'PEDRA' and computador == 'TESOURA':
    print('\033[32mVOCÊ VENCEU!\033[m {} ganha de {}.'.format(jogada, computador))
elif jogada == 'PAPEL' and computador == 'PEDRA':
    print('\033[32mVOCÊ VENCEU!\033[m {} ganha de {}.'.format(jogada, computador))
elif jogada == 'PAPEL' and computador == 'TESOURA':
    print('\033[31mGAME OVER!\033[m {} ganha de {}.'.format(computador, jogada))
elif jogada == 'TESOURA' and computador == 'PEDRA':
    print('\033[31mGAME OVER!\033[m {} ganha de {}.'.format(computador, jogada))
elif jogada == 'TESOURA' and computador == 'PAPEL':
    print('\033[32mVOCÊ VENCEU!\033[m {} ganha de {}.'.format(jogada, computador))
elif jogada == computador:
    print('\033[33mEMPATE!\033[m')
else:
    print('\033[31mERROR!\033[m')
print('\033[1;31m-\033[m' * 13)