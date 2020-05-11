#faça um algoritimo que leia o preço de um produtoe mostre seu novo preço com 5% de desconto
#operadores aritimeticos, aula 07'
from time import sleep
print('\033[1;31m--- CALCULADORA DE DESCONTO---\033[m') #titúlo
p = float(input('Insira o preço do produto em reais: R$')) #input do preço sem desconto
d = (p*5)/100 #calculando o preço com 5% de desconto de acordo com o valor do input
d2 = p-d #descontando do valor original
print('\033[32mPROCESSANDO...\033[m')
sleep(1)
print('Com o desconto de \033[32m5%\033[m o produto que custava \033[32mR${:.2f}\033[m passa a custar \033[32mR${:.2f}\033[m, você economizou \033[32mR${:.2f}\033[m.'.format(p, d2, d))
#resultado
