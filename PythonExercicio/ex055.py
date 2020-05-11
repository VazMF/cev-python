#Faça um programa que leia o peso de cinco pessoas e no final mostre qual foi o maior e o menor peso lido.
print('\033[31m=-=MAIOR-E-MENOR-PESO=-=\033[m')
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}º pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi \033[33m{}kg\033[m'.format(maior))
print('O menor peso lido foi \033[33m{}kg\033[m'.format(menor))
