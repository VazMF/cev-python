#Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
print('\033[31m---ANO BISSEXTO---\033[m') #tutúlo
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: ')) #input do ano que será analisado
if ano == 0: #determina que quando inserido 0 o computador analisará o ano atual
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #calculo para ver se o ano é bissexto
    print('O ano {} é \033[4;33mBISSEXTO\033[m.'.format(ano)) #se o if for real
else:
    print('O ano {} \033[4;33mNÃ0 é BISSEXTO\033[m.'.format(ano)) #se o if for falso
print('\033[31m-\033[m' * 18)
