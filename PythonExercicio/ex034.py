#Escreva uma programa que pergunte o sálario de um funcionário e calcule o valor de seu aumento.
#Para salários superiore a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
from time import sleep
print('\033[31m---AUMENTO SALARIAL---\033[m') #titúlo
salário = float(input('Qual o valor do salário do funcionário? R$')) #input do saaário atual do funcionario
print('\033[33mPROCESSANDO...\033[m')
sleep(1)
if salário <= 1250: #determina que se o valor do input for menor ou igual a 1250
    novo = salário + (salário * 15 / 100) #o aumento será de 15%
else: #determina que se o valor do input for superior a 1250
    novo = salário + (salário * 10 / 100) #o aumento será de 10%
print('Quem ganhava R${:.2f} passa a ganhar \033[4;33mR${:.2f}\033[m'.format(salário, novo)) #mostra o novo salário
print('\033[31m-\033[m' * 22) #fim



