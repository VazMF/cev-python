#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
from time import sleep #import sleep
print('\033[36m---ALUGUEL DE CARROS---\033[m') #titúlo
km = float(input('Quantos km foram percorridos com o carro? ')) #input de km percorridos pelo carro na variavek km
d = int(input('Por quantos dias o carro foi alugado? ')) #input dos dias de aluguel na variavel d
print('\033[36mPROCESSANDO...\033[m') #print para simular o processamento
sleep(1) #sleep
print(f'O carro percorreu \033[36m{km}km\033[m em \033[36m{d}\033[m dias, você terá que pagar \033[36mR${(km*0.15)+(d*60)}\033[m') #calculo e resultado
