#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
from time import sleep
print('\033[1;31m---CONVERSOR DE TEMPERATURA---\033[m') #titúlo
C = int(input('Digite uma temperatura em graus celsius: ')) #input da temperatura em celsius
F = ((9 * C) / 5) + 32 #convertento a temperatura em celsius do input para fahrenheit
print('\033[36mPROCESSANDO...\033[m')
sleep(1)
print('\033[36m{}°C\033[m equivalem a \033[36m{}°F\033[m'.format(C, F)) #resultado
