#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo . calcule e mostre o comprimento da hipotenusa
#aula 08, utilizando modulos
from time import sleep #importando o sleep
from math import hypot #importando a função hypot
print('\033[31m------CATETOS E HIPOTENUSA------\033[m') #titúlo
co = float(input('Comprimento do cateto oposto: ')) #input do cateto oposto
ca = float(input('Comprimento do cateto adjacente: ')) #input do cateto adjacente
hi = hypot(co, ca) #cálculo da hipotenusa de acordo com os inputs
print('\033[32mCALCULANDO...\033[m')
sleep(1)
print('Com o cateto oposto medindo \033[32m{}\033[m e o adjacente medindo \033[32m{}\033[m, a hipotenusa vai medir \033[32m{:.2f}\033[m'.format(co, ca, hi)) #resultado
print('\033[31m-\033[m' * 33)
