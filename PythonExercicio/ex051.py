#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. E no final, mostre a soma dos 10 primeiros termos da progressão.
print('\033[31m-=10-TERMOS-DE-UMA-PA=-\033[m')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo + razão, razão):
    print('{} '.format(c), end='\033[32m-> \033[m')
print('\033[31mFIM\033[m')
