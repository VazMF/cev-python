#faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.
#operadores aritiméticos aula 07
from time import sleep #importando o sleep
print('\033[1;31m---ANTECESSOR E SUCESSOR---\033[m') #titulo em vermelho e negrito
n = int(input('Insira um número: ')) #pedindo o input do número
print('\033[33mPROCESSANDO...\033[m') #carregamento
sleep(1) #sleep
print('O antecessor de \033[31m{}\033[m é \033[31m{}\033[m e o sucessor é \033[31m{}\033[m.'.format(n, (n-1), (n+1))) #resposta
