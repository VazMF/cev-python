#Faça um porograma que mostre na tela uma contagem regressiva para o estouro de fogos de artifício , indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for cont in range(10, -1, -1): #para cont de 10 ate -1 regredindo 1
    print(cont) #print conteudo da variavel cont
    sleep(0.5) #sleep por meio segundo
print('\033[33m**BOOM! BOOM! BOOM!**\033[m') #print dos 'fogos'
