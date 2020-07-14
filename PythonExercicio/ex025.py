#crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome
from time import sleep #import do sleep
print('\033[31m---TEM SILVA?---\033[m') #titúlo
nome = str(input('Qual é o seu nome completo? ')).strip() #input do nome completo na variavel nome
print('\033[31mANALISANDO NOME...\033[m') #print para a simulacao de analise
sleep(1) #sleep
print(f'Seu nome tem Silva? {"silva" in nome.lower()}') #joga o nome pra minúsculas e procura a palavra silva
print('\033[31m-\033[m' * 16) #fim
