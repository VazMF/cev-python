#faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informaçoes possiveis sobre ele
#tipos primritivos e saidas de dados
from time import sleep #importando a o sleep para a simulação de carregamento
print('\033[31m---TIPOS PRIMITIVOS---\033[m') #titulo do programa em vermelho
i1 = input('Digite algo: ') #variavel recebe o input da mensagem/número que será analisada
print('\033[31mPROCESSANDO...\033[m') #simulação do carregamento
sleep(1) #ativacao do sleep
print('O tipo primitivo desse valor é:', type(i1)) #analisando o tipo primitivo
print('É um número?', i1.isnumeric()) #analisando se é um número
print('É alfanumérico?', i1.isalnum()) #analisando se é alfanúmerico
print('É alfabético?', i1.isalpha()) #analisando se é alfabético
print('É decimal?', i1.isdecimal()) #analisando se é decimal
print('Está em minúsculas?', i1.islower()) #analisando se está em minúsculas
print('Só tem espaços?', i1.isspace()) #analisando se só tem espaços
print('Está em maiuscúlas?', i1.isupper()) #analisando se está em maiúsculas
print('Está capitalizada?', i1.istitle()) #analisando se está capitalizada
