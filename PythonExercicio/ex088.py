#faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos
#jogos serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo. cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print('-' * 36)
print(f'{"MEGA SENA":^36}') #titulo
print('-' * 36)
qtd = int(input('Quantos jogos você quer gerar? ')) #input da quantidade de jogos a ser gerada
tot = 1 #variavel total recebe 1
lista = list() #inicializa uma lista vazia
jogos = list() 
while tot <= qtd: #enquanro o total for menor ou igual o valor da quantidade
    cont = 0 #contador recebe 0
    while True: #looping infinito
        num = randint(1, 60) #randomiza um numero de 1 a 60
        if num not in lista: #se o numero randomizado nao estiver na lista
            lista.append(num) #o numero é apendado na lista
            cont += 1 #contador recebe mais 1
        if cont >= 6: #se o contador for maior ou igual a 6
            break #interrompe o while
    lista.sort() #ordena a lista em ordem crescente
    jogos.append(lista[:]) #lista jogos recebem uma copia de lista
    lista.clear() #limpa a lista a cada repeticao
    tot += 1 #total recebe mais 1
print(f'-' * 8, f' SORTEANDO {qtd} JOGOS', '-' * 8) #print formatado de resultado informando quantos jogos serao sorteado
sleep(1) #sleep por 1s
for i, l in enumerate(jogos): #repeticao para cada indice e linha na lista enumerada de jogos 
    print(f'JOGO {i+1}: {l}') #print do numero do jogo e os numeros sorteados
    sleep(1) #sleep por 1s
print(f'-' * 10, '< BOA SORTE! >', '-' * 10)
