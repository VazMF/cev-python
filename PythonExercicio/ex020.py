#o mesmo professor quer sortear a ordem de apresentação dos trabalhos dos alunos. faça um programa que leia o nome e mostre a ordem sorteada
from random import shuffle #importando a função shuffle para escolher a lista
from time import sleep #importando a função sleep
print('\033[33m-----ORDEM DE APRESENTAÇÃO-----\033[m') #titúlo
a1 = str(input('Primeiro(a) aluno(a): ')) #input do primeiro aluno na variavel a1
a2 = str(input('Segundo(a) aluno(a): ')) #input segundo aluno na variavel a2
a3 = str(input('Terceiro(a) aluno(a): ')) #input terceiro aluno na variavel a3
a4 = str(input('Quarto(a) aluno(a): ')) #input quarto aluno na variavek a4
lista = [a1, a2, a3, a4] #lista de todos os alunos
shuffle(lista) #embaralhando lista
print('\033[33mPROCESSANDO...\033[m') #print do processamento
sleep(1) #sleep
print(f'A ordem de apresentação dos trabalhos será \033[33m{lista}\033[m.') #resultado da ordem de apreentação
