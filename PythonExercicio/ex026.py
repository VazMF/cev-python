#faça um programa que leia uma frase e mostre quantas vezes aparece a letra A, em que posição ela aparece na 1 vez e em que posição aparece na última vez
from time import sleep
print('\033[31m---PRIMEIRA E ÚLTIMA OCORRÊNCIA---\033[m') #titúlo
frase = str(input('\033[30mDigite uma frase:\033[m ')).strip().upper() #variavel da frase para input jogada pra upper
print('\033[35mPROCESSANDO...\033[m')
sleep(1)
print('A letra \033[35m"A"\033[m aparece \033[35m{}\033[m vezes.'.format(frase.count('A'))) #mostra a quantidade de vezes que a letra aparece
print('A primeira letra \033[35m"A"\033[m aparece na posição \033[35m{}\033[m.'.format(frase.find('A')+1)) #mostra a primeira ocorrência
print('A última letra \033[35m"A"\033[m aparece na posição \033[35m{}\033[m.'.format(frase.rfind('A')+1)) #última ocorrência
print('\033[31m-\033[m' * 34) #fim


