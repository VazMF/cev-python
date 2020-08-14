#Faça um programa que leia o peso de cinco pessoas e no final mostre qual foi o maior e o menor peso lido.
print('\033[33m=-=-=-=MAIOR-E-MENOR-PESO=-=-=-=\033[m') #titulo
maior = menor = 0 #inicializacao das variaveis maior e menor
for p in range(1, 6): #repeticao de 1 ate 5
    peso = float(input(f'Peso da {p}º pessoa: ')) #variavel peso recebe o input do usuario
    if p == 1: #se for a primeira repeticao
        maior = menor = peso #maior recebe o primeiro peso
    else: #senao for a primeira repeticao
        if peso > maior: #se o valor da variavel peso for maior que o valor que ja esta armazenado na variavel maior
            maior = peso #maior recebe o valor da variavel peso
        if peso < menor: #se o valor da variavel peso for menor que o valor que ja esta armazenado na variavel menor
            menor = peso #menor recebe o valor da variavel peso
print(f'O maior peso lido foi \033[33m{maior}kg\033[m') #print mostrando o maior peso lido
print(f'O menor peso lido foi \033[33m{menor}kg\033[m') #print mostrando o menor peso lido
 