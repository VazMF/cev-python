#Faça um program que tenha uma função contador(), que receba três parâmetros: inicio, fim e passo e realize a contagem. Seu programa tem que realizar três contagens: a - de 1 ate 10, de 1 em 1; b - de 10 ate 0, de 2 em 2; c - uma contagem personalizada
from time import sleep
#DEFININDO A FUNÇÃO
def contador(i, f, p): #define a função com 3 parâmetros: inicio, fim, passo
    print('~' * 50) #print da linha para separar
    if p < 0: #se o passo for negativo
        p *= -1 #multiplica o passo por -1, invertendo o sinal para positivo
    if p == 0: #se o passo for 0
        p = 1 #passo recebe 1, pq passo 0 nao existe
    print(f'Contagem de {i} até {f} de {p} em {p}') #print informando os parâmetros da contagem
    sleep(1.5) #sleep por um segundo e meio
    if i < f: #se o inicio for menor que o fim
        cont = i #o contador recebe inicio
        while cont <= f: #enquanto o contador for menor ou igual ao fim
            print(f'{cont} ', end='', flush = True) #print formatado da contagem, sem pular linha e printando numero por numero com o flush
            sleep(0.3) #sleep para printar um numero de cada vez
            cont += p #contador recebe o passo
        print('FIM!') #print de fim
    else: #senao se o inicio for maior que o fim
        cont = i #contador recebe inicio
        while cont >= f: #enquanto o contador for maior ou igual ao fim
            print(f'{cont} ', end='', flush = True) #print formatado com a contagem, sem pular linha e printando numero por numero com o flush
            sleep(0.3) #sleep para esperar antes de printar o prox numero
            cont -= p #contador vai diminuir o valor do passo
        print('FIM!') #print de fim


#PROGRAMA PRINCIPAL
contador(1, 10, 1) #chama a função contador com os parâmetros que estão entre parenteses
contador(10, 0, 2) #chama a função contador com os parâmetros que estão entre parenteses
print('~' * 50) #print de linha para separar
print(f'Agora é a sua vez, personalize a contagem!') #print informando para o user determinar os parâmetros
inicio = int(input('Início: ')) #input do valor de inicio da contagem
fim = int(input('Fim: ')) #input do valor do fim da contagem
passo = int(input('Passo: ')) #input do valor do passo da contagem
contador(inicio, fim, passo) #chamada da função contador pasando os parâmetros lidos
