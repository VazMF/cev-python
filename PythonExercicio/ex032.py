#Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
print('\033[31m---ANO BISSEXTO---\033[m') #titúlo
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: ')) #input do ano que será analisado na variavel ano
if ano == 0: #se a variavel ano for igual a zero o computador analisará o ano atual
    ano = date.today().year #ano recebe a data atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #calculo para ver se o ano é bissexto
    print(f'O ano {ano} é \033[4;33mBISSEXTO\033[m.') #se o if for real
else:
    print(f'O ano {ano} \033[4;33mNÃ0 é BISSEXTO\033[m.') #se o if for falso
print('\033[31m-\033[m' * 18)
