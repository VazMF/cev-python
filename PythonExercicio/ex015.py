#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''
from time import sleep
print('\033[1;32m---ALUGUEL DE CARROS---\033[m') #titúlo
km = float(input('Quantos km foram percorridos com o carro? ')) #input de km percorridos pelo carro
d = int(input('Por quantos dias o carro foi alugado? ')) #dias de aluguel
print('\033[31mPROCESSANDO...\033[m')
sleep(1)
print('O carro percorreu \033[31m{}km\033[m em \033[31m{}\033[m dias, você terá que pagar \033[31mR${}\033[m'.format(km, d, (km*0.15)+(d*60))) #calculo e resultado
