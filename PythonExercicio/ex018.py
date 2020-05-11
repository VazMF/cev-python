#faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
#aula 08, utilizando módulos
from math import sin, cos, tan, radians
from time import sleep
print('\033[1;31m---SENO, COSSENO E TANGENTE---\033[m') #titúlo
ang = float(input('Digite o valor do ângulo: ')) #input do ângulo
seno = sin(radians(ang)) #cálculo do seno e convrsão de radianos de acordo com o input
cos = cos(radians(ang)) #cálculo do cosseno e vonversão de radianos
tan = tan(radians(ang)) #cálculo da tangente e conversão de radianos
print('\033[32mCALCULANDO...\033[m')
sleep(1)
print('\033[32mSENO:\033[m {:.2f}'.format(seno)) #resultado do seno
print('\033[32mCOSSENO:\033[m {:.2f}'.format(cos)) #resultado do cosseno
print('\033[32mTANGENTE:\033[m {:.2f}'.format(tan)) #resultado da tangente
print('\033[1;31m-\033[m' * 30)

