#melhore o jogo do desafio 028, onde o computador vai pensar em um número  entre 0 e 10. só que agora o jogador vai tentar adivinhar até acertar. mostrando no final quantos
#palpites foram necessários para vencer.
from random import randint #import do randint para randomizar a escolha do computador
print('\033[31m=-=JOGO-DA-ADIVINHAÇÃO=-=\033[m') #titulo
comp = randint(0, 10) #computador escolhe um numero aleatorio de 0 a 10
print('Acabei de pensar em um número entre 0 e 10. Será que você consegue adivinhar?')
acertou = False #determina que ngm acertou
tentativas = 0
while not acertou: #enquanto o ngm tiver acertado
    jogador = int(input('Qual seu palpite? ')) #computador pergunta qual seu palpite de numero
    if jogador == comp: #se a resposta do usuario for igual a do computador
        acertou = True #altere acertou para verdadeiro
    else: #caso contrario
        if jogador < comp: #se a respota do jogador for menor que a do computador
            print('Mais... Tente novamente.') #printa para ele chutar um numero maior
        elif jogador > comp: #se a respota do jogador for maior que a do computador
            print('Menos... Tente novamente.') #printa para ele chutar um numero menor
    tentativas += 1 #adiciona uma tentativa a cada jogada, ate o jogador acertar
print('\033[33mParabéns!\033[m Eu realmente pensei no número {}.'.format(comp))
print('Você precisou de {} tentativas para acertar.'.format(tentativas))
