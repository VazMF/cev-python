#faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.
#operadores aritiméticos aula 07
from time import sleep #importando o sleep
print('\033[31m---ANTECESSOR E SUCESSOR---\033[m') #titulo em vermelho
n = int(input('Insira um número: ')) #variavel do input do numero a ser analisado
print('\033[33mPROCESSANDO...\033[m') #print da para simulacao do processamento
sleep(1) #sleep
print(f'O antecessor de \033[31m{n}\033[m é \033[31m{n-1}\033[m e o sucessor é \033[31m{n+1}\033[m.') #print com a resposta
