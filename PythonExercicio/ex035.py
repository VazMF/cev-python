#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
from time import sleep
print('\033[31m---ANALISADOR DE TRIÂNGULOS---\033[m') #titulo
r1 = float(input('Primeiro segmento: ')) #input do comprimento da primeira reta na variavel r1
r2 = float(input('Segundo segmento: ')) #input do comprimento da segunda reta na variavel r2
r3 = float(input('Terceiro segmento: ')) #inpur do comprimento da terceira reta na variavel r3
print('\033[33mANALISANDO...\033[m')
sleep(1)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: #se r1 for menor que a soma de r2 e r3 e r2 for menor que a soma de r1 e re e r3 for menor que a soma de r1 e r2
    print('Os segmentos acima \033[4;33mPODEM FORMAR\033[m um triângulo!') #mensagem caso o if seja verdadeiro
else:
    print('Os segmentos acima \033[4;31mNÃO PODEM FORMAR\033[m um triângulo.') #mensagem caso o if seja falso
