#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
from time import sleep
print('\033[33m---CALCULADORA DE PREÇOS DE PASSAGEM---\033[m') #titúlo
d = int(input('Quantos km são necessários para chegar ao seu destino? ')) #input de quantos km vai percorrer na variavel d
print('\033[33mPROCESSANDO...\033[m')
sleep(1)
if d <= 200: #se a o input for menor ou igual a 200 km o preço por km sera 50 centavos
    print(f'Para percorrer \033[33m{d}km\033[m, sua passagem custará \033[4;33mR${d*0.50:.2f}\033[m')
else: #determina que caso a afirmaçao acima não seja verdadeira a conta será feita cobrando 45 centavos por km
    print(f'Para percorrer \033[33m{d}km\033[m, sua passagem custará \033[4;33mR${d*0.45:.2f}\033[m')
