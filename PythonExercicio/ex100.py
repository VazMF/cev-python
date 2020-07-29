#Faça um programq eu tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números e va colocá-los dentro da lista, a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from random import randint
from time import sleep
#DEFININDO A FUNÇÃO
def sorteio(lista): #define a função com o parâmetro lista
    for cont in range(0, 5): #repetição de 1 a 5
        lista.append(randint(1, 10)) #append de um valor randomizado de 1 a 10 na lista
    print('Sorteando 5 valores: ', end='') #print informando que os valores serão sorteados
    for v in lista: #repetição para cada valor na lista
        print(f'{v} ', end='', flush = True) #print mostrando o valor 
        sleep(0.3) #sleep para mostrar o prox valor


def somaPar(lista): #define outra função tb com o parâmetro lista
    print('\nOs valores pares da lista são: ', end='') #print dos informando os valores pares da lista serão exibidos
    soma = 0 #inicializa uma variavel soma com zero
    for v in lista: #repetição para cada valor na lista
        if v % 2 == 0: #se o valor for par
            print(f'{v} ', end='', flush = True) #print formatado com o valor
            sleep(0.3) #sleep antes de exibir o prox numero
            soma += v #soma recebe o valor
    print(f'\nSomando os pares temos: {soma}') #print mostrando a soma dos pares
            

#PROGRAMA PRINCIPAL
print('~' * 35)
numeros = list() #inicializa uma lista números
sorteio(numeros) #chama a função sorteio dando a lista de numeros como parâmetro
somaPar(numeros) #chama a função somaPar dando a lista de numeros como parâmetro
print('~' * 35)
