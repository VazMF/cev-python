#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preçi da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
from time import sleep
print('\033[31m---CALCULADORA DE PREÇOS DE PASSAGEM---\033[m') #titúlo
d = int(input('Digite quantos km são necessários para chegar ao seu destino: ')) #input de quantos km vai percorrer
print('\033[33mPROCESSANDO...\033[m')
sleep(1)
if d <=200: #determina que se a o input for menor ou igual a 200 km a conta será feita cobrando 50 sentavos por km
    print('Para percorrer \033[33m{}km\033[m, sua passagem custará \033[4;33mR${:.2f}\033[m'.format(d, (d*0.50)))
else: #determina que caso a afirmaçao acima não seja verdadeira a conta será feita cobrando 45 centavos por km
    print('Para percorrer \033[33m{}km\033[m, sua passagem custará \033[4;33mR${:.2f}\033[m'.format(d, (d*0.45)))
print('\033[31m-\033[m' * 39) #fim
