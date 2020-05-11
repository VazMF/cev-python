#faça um programa que jogue par ou ímpar com o computador. o jogo só será interrompido quando o jogador perder. mostrando o total de vitótias consecutivas do jogador.
from random import randint
from time import sleep
print('\033[35m-=-PAR OU ÍMPAR-=-\033[m')
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    comp = randint(0, 10)
    total = jogador + comp
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {comp}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if total % 2 != 0:
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamnte...')
    sleep(2)
print(f'GAME OVER! Você teve {v} vitórias.')
