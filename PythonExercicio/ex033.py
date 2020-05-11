#Faça um programa que leia três números e mostre qual1 é o maior e qual é o menor.
from time import sleep
print('\033[31m---MAIOR E MENOR---\033[m') #titúlo
n1 = int(input('Digite o primeiro número: ')) #input do primeiro numero
n2 = int(input('Digite o segundo número: ')) #input do segundo numero
n3 = int(input('Digite o terceiro número: ')) #input do terceiro numero
# Verificando qual é o menor
menor = n1 #supoem que o menor seja o input do n1
print('\033[33mPROCESSANDO...\033[m')
sleep(1)
if n2 < n1 and n2 < n3: #determina que se o n2 for menor que n1 e n3
    menor = n2 #a variavel menor será substituida por n2
if n3 < n1 and n3 < n2: #determina que se o n3 for menor que n1 e n2
    menor = n3 #a variavel de 'menor' seá substituida por n3
print('O \033[4;33mmenor\033[m número digitado foi {}.'.format(menor)) #mostra o menor número informado pelo input
# Verificando qual é o maior
maior = n2 #supoem que o maior número do input seja n2
if n1 > n2 and n1 > n3: #determina que se n1 for maior que n2 e n3
    maior = n1 #a variavel 'maior' será substituida por n1
if n3 > n2 and n3 > n1: #determina que se n3 for maior que n2 e n1
    maior = n3 #a variavel 'maior' será substituida por n3
print('O \033[4;33mmaior\033[m número digitado foi {}.'.format(maior)) #mostra o maior número do input
print('\033[31m-\033[m' * 19) #fim

