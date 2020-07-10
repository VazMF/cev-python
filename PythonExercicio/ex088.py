#faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos
#jogos serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo. cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print('-' * 36)
print(f'{"MEGA SENA":^36}')
print('-' * 36)
qtd = int(input('Quantos jogos você quer gerar? '))
tot = 1
lista = list()
jogos = list()
while tot <= qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-' * 8, f' SORTEANDO {qtd} JOGOS', '-' * 8)
sleep(1)
for i, l in enumerate(jogos):
    print(f'JOGO {i+1}: {l}')
    sleep(1)
print(f'-' * 10, '< BOA SORTE! >', '-' * 10)
