#crie um programa que leia o nome de uma cidade e diga se ela começa com o nome 'SANTO'.
from time import sleep
print('\033[31m---COMEÇA COM SANTO?---\033[m') #titúlo
cid = str(input('Digite o nome da cidade: ')).strip() #input do nome da cidade
print('\033[30mA cidade de {} começa com a palavra Santo?\033[m'.format(cid))
print('\033[32mANALISANDO...\033[m')
sleep(1)
print(cid[:5].upper() == 'SANTO') #procura santo no input
print('\033[31m-\033[m' * 23)




