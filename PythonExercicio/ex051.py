#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. E no final, mostre a soma dos 10 primeiros termos da progressão.
print('\033[31m-=10-TERMOS-DE-UMA-PA=-\033[m') #titulo
primeiro = int(input('Primeiro termo: ')) #input do primeiro termo da PA
razão = int(input('Razão: ')) #input da razao da PA
decimo = primeiro + (10 - 1) * razão #formula para calcular o decimo termo da PA
for c in range(primeiro, decimo + razão, razão): #repeticao para mostrar os termos
    print(f'{c} ', end='\033[32m-> \033[m') #print dos termos
print('\033[31mFIM\033[m')
