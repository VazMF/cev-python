#crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome
from time import sleep
print('\033[31m---TEM SILVA?---\033[m') #titúlo
nome = str(input('Qual é o seu nome completo? ')).strip() #input do nome completo
print('\033[32mANALISANDO NOME...\033[m')
sleep(1)
print('Seu nome tem Silva? {}'.format('silva' in nome.lower())) #joga o nome pra minúsculas e procura a palavra silva
print('\033[31m-\033[m' * 16) #fim

