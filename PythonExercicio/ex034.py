#Escreva uma programa que pergunte o sálario de um funcionário e calcule o valor de seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
from time import sleep
print('\033[31m----------------AUMENTO SALARIAL----------------\033[m') #titúlo
salario = float(input('Qual o valor do salário do funcionário? R$')) #input do salário atual do funcionario na variavel salario
print('\033[33mPROCESSANDO...\033[m')
sleep(1)
if salario <= 1250: #se o valor do input for menor ou igual a 1250
    novo = salario + (salario * 15 / 100) #o aumento será de 15%
else: #se o valor do input for superior a 1250
    novo = salario + (salario * 10 / 100) #o aumento será de 10%
print(f'Quem ganhava R${salario:.2f} passa a ganhar \033[4;33mR${novo:.2f}\033[m') #mostra o novo salário
