#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
from time import sleep #import do sleep
print('\033[36m----------CONVERSOR DE TEMPERATURA----------\033[m') #titulo
C = int(input('Digite uma temperatura em graus celsius: ')) #input da temperatura em celsius na variavel C
F = ((9 * C) / 5) + 32 #convertento a temperatura em celsius do input para fahrenheit na varivel F
print('\033[36mPROCESSANDO...\033[m') #print do processamento para simular loading
sleep(1) #sleep
print(f'\033[36m{C}°C\033[m equivalem a \033[36m{F}°F\033[m') #resultado formatado
