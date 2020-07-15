#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maior idade e quantas já são maiores.
print('\033[31m===MAIORIDADE===\033[m') #titulo
from datetime import date 
atual = date.today().year #variavel atual recebe a data atual do computador
totmaior = totmenor = 0 #inicializacao das variaveis totmaior e totmenor para armazenar os maiores e menores de idade
for pess in range(1, 8): #repeticao para cada pessoa de 1 ate 7
    nasc = int(input(f'Em que ano a {pess}º pessoa nasceu? ')) #input do ano de nascimento na variavel nasc
    idade = atual - nasc #variavel idade recebe o valor da idade
    if idade >= 21: #se a idade for maior ou igula a 21 (maior idade em USA)
        totmaior += 1 #total de maiores recebe mais um
    else: #senao
        totmenor += 1 #total de menores recebe mais um
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade.') #print formatado com a quantidade de pessoas maiores
print(f'E também tivemos {totmenor} pessoas menores de idade.') #print formatado com a quantidade de pessoa menores
print('\033[31m=\033[m' * 16)
