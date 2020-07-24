#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
#DEFININDO A FUNÇÃO
def maior(* num): #define a função com valores indeterminados
    cont = maior = 0 #incializa a variavel contador e maior com zero
    print('~' * 40) #separador
    print('Analisando os valores informados...') #print informando que os numeros estao sendo analisados
    sleep(1) #sleep de um segundo para o user ler
    for v in num: #para cada valor de numeros
        print(f'\033[33m{v}\033[m ', end='', flush = True) #print o valor sem quebrar linha e esperando um tempo antes de do prox
        sleep(0.3) #sleep de 0.3s
        if cont == 0: #se o contador for zero
            maior = v #maior recebe o valor
        elif v > maior: #senao se o valor for maior que o conteudo da variavel maior
            maior = v #maior recebe valor
        cont += 1 #contador recebe mais um
    print(f'Foram informados \033[33m{cont}\033[m valores.') #print informando o total de valore analisados pelo contador
    print(f'O maior valor informado foi \033[33m{maior}\033[m.') #print informando o maior valor


#PROGRAMA PRINCIPAL
#chamadas da função maior passando os parâmetros
maior(2, 9, 4, 5, 7, 1) 
maior(4, 7, 0, 8)
maior(1, 2, 5)
maior(6, 1)
maior(9)
maior()
