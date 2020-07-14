#Escreva um programa para aprovar o empréstimo bancário de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o empréstimo será negado.
from time import sleep
print('\033[31m---EMPRÉSTIMO BANCÁRIO---\033[m') #titulo
casa = float(input('Valor da casa: R$')) #input do valor da casa na variavel casa
salario = float(input('Salário do comprador: R$')) #input do salario na variavel salario
anos = int(input('Quantos anos de financiamento? ')) #input dos anos na variavel ano
prestacao = casa / (anos * 12) #valor na prestacao da casa na variavel prestacao
minimo = (salario * 30) / 100 #calculo de 30% do salario na variavel minimo
sleep(1) #sleep
if prestacao >= minimo: #se a prestacao for maior ou igual a 30% do salario informado
    print(f'Seu empréstimo foi \033[31mNEGADO!\033[m A parcela seria de R${prestacao:.2f}') #print informando que o emprestimo foi negado
    print(f'você ganha R${salario:.2f}, é muito pouco.')
else: #senao
    print('Seu empréstimo foi \033[33mACEITO!\033[m ') #print infromando que o emprestiomo foi aceito
    print(f'Você terá que pagar R${prestacao:.2f} por mês durante {anos} anos.') #print do valor das parcelas
