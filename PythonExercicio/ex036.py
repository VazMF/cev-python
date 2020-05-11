#Escreva um programa para aprovar o empréstimo bancário de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o empréstimo será negado.
from time import sleep
print('\033[31m---EMPRÉSTIMO BANCÁRIO---\033[m')
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
mínimo = (salario * 30) / 100
sleep(1)
if prestacao >= mínimo:
    print('Seu empréstimo foi \033[31mNEGADO!\033[m A parcela seria de R${:.2f}'.format(prestacao))
    print('você ganha R${:.2f}, é muito pouco.'.format(salario))
else:
    print('Seu empréstimo foi \033[33mACEITO!\033[m ')
    print('Você terá que pagar R${:.2f} por mês durante {} anos.'.format(prestacao, anos))
print('\033[31m-\033[m' * 25)

