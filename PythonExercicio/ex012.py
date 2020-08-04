#faça um algoritmo que leia o preço de um produtoe mostre seu novo preço com 5% de desconto
print('\033[31m----- CALCULADORA DE DESCONTO -----\033[m') #titúlo
p = float(input('Insira o preço do produto: R$')) #input do preço sem desconto na variavel p
d = (p*5)/100 #calculando o valor do desconto de acordo com o preço e jogando na variavel d
d2 = p-d #descontando do valor originale jogando na variavel d2
print(f'Com o desconto de \033[32m5%\033[m o produto que custava \033[32mR${p:.2f}\033[m passa a custar \033[32mR${d2:.2f}\033[m, você economizou \033[32mR${d:.2f}\033[m.') #print com o resulltado formatado
