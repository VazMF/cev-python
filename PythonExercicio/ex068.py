#faça um programa que jogue par ou ímpar com o computador. o jogo só será interrompido quando o jogador perder. mostrando o total de vitótias consecutivas do jogador.
from random import randint
from time import sleep
print('\033[35m-=-=PAR OU ÍMPAR=5-=-\033[m')
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    comp = randint(0, 10)
    total = jogador + comp
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
        print('-' * 22)
    print(f'Você jogou \033[35m{jogador}\033[m')
    print(f'Computador jogou \033[35m{comp}\033[m')
    print('-' * 22)
    print('\033[35mDEU PAR\033[m' if total % 2 == 0 else '\033[35mDEU ÍMPAR\033[m')
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
    print('Vamos jogar novamente...')
    print('-' * 22)
    sleep(2)
print(f'GAME OVER! Você teve \033[35m{v}\033[m vitórias.')
