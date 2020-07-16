#faça um programa que jogue par ou ímpar com o computador. o jogo só será interrompido quando o jogador perder. mostrando o total de vitótias consecutivas do jogador.
from random import randint
from time import sleep
print('\033[35m-=-=PAR OU ÍMPAR=5-=-\033[m') #titulo
v = 0 #variavel de vitorias comeca com 0
while True: #loop infinito
    jogador = int(input('Diga um valor: ')) #input do palpite do jogador
    comp = randint(0, 10) #computador randomiza um numero de 0 a 10
    total = jogador + comp #total recebe a soma do palpite do jogador e o numero sorteado pelo computador
    escolha = ' ' #variavel escolha recebe vazio
    while escolha not in 'PI': #loop para só aceitar Par ou Impar na escolha
        escolha = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0] #input do par ou impar
        print('-' * 22) #print para resultado
    print(f'Você jogou \033[35m{jogador}\033[m') #print mostrando o numero escolhido pelo jogador
    print(f'Computador jogou \033[35m{comp}\033[m') #print mostrando o numero sorteado pelo computador
    print('-' * 22) #print de resultado
    print('\033[35mDEU PAR\033[m' if total % 2 == 0 else '\033[35mDEU ÍMPAR\033[m') #print de par ou impar
    if escolha == 'P': #se a escolha for par
        if total % 2 == 0: #se o total for par
            print('Você VENCEU!') #jogador vence
            v += 1 #soma uma vitoria
        else: #senao
            print('Você PERDEU!') #jogador perde
            break #interrompe o while
    elif escolha == 'I': #senao se a escolha for impar
        if total % 2 != 0: #se o total for impar
            print('Você VENCEU!') #jogador vence
            v += 1 #soma uma vitoria
        else: #senao
            print('Você PERDEU!') #jogador perde
            break #interrompe o while
    print('Vamos jogar novamente...') #enquanto o jogador nao perder, o jogo reinicia
    print('-' * 22) #print de resultado
    sleep(2) #sleep para esperar 2s antes de reinicar o loop
print(f'GAME OVER! Você teve \033[35m{v}\033[m vitórias.') #print quando o jogador perde, mostrando as vitorias
