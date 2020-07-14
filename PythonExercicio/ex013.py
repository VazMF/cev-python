#faça um algoritimo que leia o salário de um funcionario e mostre seu novo salario com 15% de aumento
print('\033[1;31m---------AUMENTO---------\033[m') #titúlo
sa = float(input('Digite o salário atual do funcionário: R$')) #input do salário atual do funcionário para a variavel sa
a = (sa*15)/100 #calculando aumento sob o valor do input para a variavel a
sn = sa + a #calculando o novo salário com o aumento
print(f'Com o aumento de \033[32m15%\033[m quem ganhava \033[32mR${sa:.2f}\033[m, passa a ganhar \033[32mR${sn:.2f}\033[m, ou seja, \033[32mR${a:.2f}\033[m a mais.') #print formatado com a resposta
