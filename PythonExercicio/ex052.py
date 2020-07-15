#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
print('\033[31m===NÚMEROS=PRIMOS===\033[m') #titulo
num = int(input('Digite um número: ')) #input do numero que vai ser analisado na variavel num
tot = 0 #inicializacao da variavel total com 0
for c in range(1, num + 1): #repeticao comecando em 1 e indo ate o numero inserido no input pelo usuario
    if num % c == 0: #se o numero for divisivel pelo contador da repeticao 
        print('\033[33m', end='') #print para deixar os numeros divisiveis em amarelo
        tot += 1 #total receberao total mais um
    else: #senao for divisivel
        print('\033[31m', end='') #print para deixar os numeros nao divisiveis em vermelho
    print(f'{c} ', end=' ') #print do contador da repeticao
print(f'\n\033[mO número {num} foi divisível {tot} vezes') #print formatado com o numero de vezes que o numero foi divisivel
if tot == 2: #se o total for igual a dois
    print('E por isso ele \033[33mÉ PRIMO\033[m.') #print infotmando que o numero é primo
else: #senao
    print('E por isso ele \033[31mNÃO É PRIMO\033[m.') #print informando que o numero nao é primo
