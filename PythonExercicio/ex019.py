#um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome desles e escrevendo o nome do escolhido
#aula 08, utlizando módulos
from random import choice
from time import sleep
print('\033[1;31m---SORTEIO---\033[m') #titúlo
a1 = str(input('Primeiro(a) aluno(a): ')) #input do nome do primeiro aluno
a2 = str(input('Segundo(a) aluno(a): ')) #input do noome do segundo aluno
a3 = str(input('Terceiro(a) aluno(a): ')) #input do nome do terceiro aluno
a4 = str(input('Quarto(a) aluno(a): ')) #input do nome do quarto aluno
lista = [a1, a2, a3, a4] #lista com todos os inputs
escolhido = choice(lista) #comp escolhe um nome da lista
print('\033[31mPROCESSANDO...\033[m')
sleep(1)
print('O aluno(a) escolhido para apagar o quadro foi \033[1;31m{}\033[m.'.format(escolhido)) #mostra o aluno escolhido
print('\033[1;31m-\033[m' * 13)
