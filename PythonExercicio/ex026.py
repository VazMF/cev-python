#faça um programa que leia uma frase e mostre quantas vezes aparece a letra A, em que posição ela aparece na 1 vez e em que posição aparece na última vez
from time import sleep #import do sleep
print('\033[35m---PRIMEIRA E ÚLTIMA OCORRÊNCIA---\033[m') #titúlo
frase = str(input('Digite uma frase: ')).strip().upper() #variavel da frase para input jogada pra upper
print('\033[35mPROCESSANDO...\033[m') #print para simular processamento
sleep(1) #sleep
print(f'A letra \033[35m"A"\033[m aparece \033[35m{frase.count("A")}\033[m vezes.') #mostra a quantidade de vezes que a letra aparece
print(f'A primeira letra \033[35m"A"\033[m aparece na posição \033[35m{frase.find("A")+1}\033[m.') #mostra a primeira ocorrência
print(f'A última letra \033[35m"A"\033[m aparece na posição \033[35m{frase.rfind("A")+1}\033[m.') #última ocorrência
