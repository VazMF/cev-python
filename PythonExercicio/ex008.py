#escreva um programa que leia um valor em metros e o exiba convertido em cm e em mm
from time import sleep #sleep
print('\033[31m----CONVERSOR DE MEDIDAS----\033[m') #titúlo
m = int(input('Digite um valor em metros: ')) #input do valor em metros em uma variavel m
print('\033[31mPROCESSANDO...\033[m') #print simulacao do processamento
sleep(1) #sleep
print(f'QUILÔMETROS:  {m / 1000}km') #transformando m em km, dividindo o input pot 1000
print(f'CENTÍMETROS: {m * 100}cm') #transformando m em cm, multiplicando o input  por 100
print(f'DECÍMETROS: {m * 10}dc') #transformando m em dc, multiplicando o input por 10
print(f'DECÂMETROS: {m / 10}dam') #transformando m em dam, dividindo o input por 10
print(f'MILÍMETROS: {m * 1000}mm') #transformando m em mm, multiplicando o input por 1000
print(f'HECTÔMETROS: {m / 100}hm') #transformando m em hm, dividindo o input por 100
