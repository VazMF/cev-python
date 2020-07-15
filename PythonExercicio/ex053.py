#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
print('\033[31m===DETECTOR=DE=PALÍNDROMO===\033[m') #titulo
frase = str(input('Digite uma frase: ')).strip().upper() #lê a frase, tira os espaços e joga ela pra maisuculas
palavras = frase.split() #split na frase, separando palavra por palavra
junto = ''.join(palavras) #junta tudo numa string
inverso = '' #variavel inverso recebe vazio
#inverso = junto[::-1] macete usando o fatiamento sem o for
for letra in range(len(junto) -1, -1, -1): #inverte a frase, indo da última letra até a primeira voltando uma letra
    inverso += junto[letra] 
print(f'O inverso de {junto} é {inverso}')
if inverso == junto: #verifica se é um palindromo
    print('A frase digitada \033[33mé um palíndromo.\033[m')
else:
    print('A frase digitada \033[31mNÃO é um palíndromo\033[m.')
