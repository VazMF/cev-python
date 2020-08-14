#melhore o jogo do desafio 028, onde o computador vai pensar em um número  entre 0 e 10. só que agora o jogador vai tentar adivinhar até acertar. mostrando no final quantos palpites foram necessários para vencer.
from random import randint #import do randint para randomizar a escolha do computador
print('\033[35m---------------JOGO-DA-ADIVINHAÇÃO 2.0---------------\033[m') #titulo
comp = randint(0, 10) #computador escolhe um numero aleatorio de 0 a 10
print('Acabei de pensar em um número entre 0 e 10...')
print('Será que você consegue adivinhar?')
acertou = False #determina que ngm acertou
tentativas = 0
while not acertou: #enquanto ngm tiver acertado
    jogador = int(input('Qual seu palpite? ')) #computador pergunta qual seu palpite de numero
    if jogador == comp: #se a resposta do usuario for igual a do computador
        acertou = True #altere acertou para verdadeiro
    else: #caso contrario
        if jogador < comp: #se a respota do jogador for menor que a do computador
            print('\033[35mMais... Tente novamente.\033[m') #printa para ele chutar um numero maior
        elif jogador > comp: #se a respota do jogador for maior que a do computador
            print('\033[35mMenos... Tente novamente.\033[m') #printa para ele chutar um numero menor
    tentativas += 1 #adiciona uma tentativa a cada jogada, ate o jogador acertar
print(f'\033[32mParabéns! Eu realmente pensei no número {comp}.\033[m')
print(f'Você precisou de {tentativas} tentativas para acertar.')
