#faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informaçoes possiveis sobre ele
#tipos primritivos e saidas de dados
from time import sleep #importando a função sleep para a simulação de carregamento
print('\033[1;31m---TIPOS PRIMITIVOS---\033[m') #titulo do programa em vermelho e negrito
i1 = input('Digite algo: ') #input da mensagem/número que será analisada
print('\033[32mPROCESSANDO...\033[m') #simulação do carregamento em verde
sleep(1) #sleep funcionando
print('\033[1;30mO tipo primitivo desse valor é\033[m', type(i1)) #analisando o tipo primitivo
print('\033[1;30mÉ um número?\033[m ', i1.isnumeric()) #analisando se é um número
print('\033[1;30mÉ alfanumérico?\033[m ', i1.isalnum()) #analisando se é alfanúmerico
print('\033[1;30mÉ alfabético?\033[m ', i1.isalpha()) #analisando se é alfabético
print('\033[1;30mÉ decimal?\033[m ', i1.isdecimal()) #analisando se é decimal
print('\033[1;30mEstá em minúsculas?\033[m ', i1.islower()) #analisando se está em minúsculas
print('\033[1;30mSó espaços?\033[m ', i1.isspace()) #analisando se só tem espaços
print('\033[1;30mEstá em maiuscúlas?\033[m', i1.isupper()) #analisando se está em maiúsculas
print('\033[1;30mEstá capitalizaada?\033[m', i1.istitle()) #analisando se está capitalizada
