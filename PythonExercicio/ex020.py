#o mesmo professor quer sortear a ordem de apresentação dos trabalhos dos alunos. faça um programa que leia o nome e mostre a ordem sorteada
#aula 08, utilizando módulos
from random import shuffle #importando a função shuffle para escolher a lista
from time import sleep #importando a função sleep
print('\033[1;31m---ORDEM DE APRESENTAÇÃO---\033[m') # titúlo
a1 = str(input('Primeiro(a) aluno(a): ')) #input do primeiro aluno
a2 = str(input('Segundo(a) aluno(a): ')) #input segundo aluno
a3 = str(input('Terceiro(a) aluno(a): ')) #input terceiro aluno
a4 = str(input('Quarto(a) aluno(a): ')) #input quarto aluno
lista = [a1, a2, a3, a4] #lista de todos os alunos
shuffle(lista) #embaralhando lista
print('\033[32mPROCESSANDO...\033[m')
sleep(1)
print('A ordem de apresentação dos trabalhos será \033[32m{}\033[m.'.format(lista)) #resultado da ordem de apreentação
print('\033[1;31m-\033[m' * 27)
