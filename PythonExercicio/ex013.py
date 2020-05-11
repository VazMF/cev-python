#faça um algoritimo que leia o salário de um funcionario e mostre seu novo salario com 15% de aumento
#operadores aritimeticos. aula 07
from time import sleep
print('\033[1;31m---AUMENTO---\033[m') #titúlo
sa = float(input('Digite o salário atual do funcionário: R$')) #input do salário atual do funcionário
a = (sa*15)/100 #calculando aumento sob o valor do input
sn = sa + a #salário com o aumento
print('\033[32mPROCESSANDO...\033[m')
sleep(1)
print('Com o aumento de \033[32m15%\033[m quem ganhava \033[32mR${:.2f}\033[m, passa a ganhar \033[32mR${:.2f}\033[m, ou seja, \033[32mR${:.2f}\033[m a mais.'.format(sa, sn, a))

