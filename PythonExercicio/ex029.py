#Escreva um programa que leia a velocidade de um carro. Se e;e ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa custará  R$7,00 por cada km acima do limite
from time import sleep
print('\033[35m-------------------CALCULADORA DE MULTAS------------------\033[m') #titúlo
velocidade = int(input('Velocidade do carro: [Km/h] ')) #input da velocidade do carro na variavel velocidade
multa = (velocidade - 80) * 7 #calcula a multa com base nas informações do enunciado
print('\033[35mPROCESSANDO...\033[m')
sleep(1)
if velocidade > 80: #define que se a velocidade informada for maior que 80 será exbido o print abaixo
    print(f'Você está a \033[31m{velocidade}km/h\033[m, o limite da pista é de 80km/h')
    print(f'você \033[4;31mserá multado\033[m no valor de \033[31mR${multa:.2f}!\033[m')
else: #define que se a condição acima não for real o print a ser exibido será esse
    print('Você está dentro do limite de velocidade e \033[4;33mnão será multado\033[m.')
