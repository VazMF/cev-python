#faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o segundo nome separadamente
from time import sleep
print('\033[31m---PRIMEIRO E ÚLTIMO NOME---\033[m') #titúlo
n = str(input('Digite seu nome completo: ')).strip() #input do nome completo
nome =n.split() #variavel que armazena os nomes separados pelo split
print('\033[32mANALISANDO NOME...\033[m')
sleep(1)
print('\033[30mMuito prazer em te conhecer!\033[m') #msg de boas vindas
print('Seu primeiro nome é \033[4;32m{}\033[m.'.format(nome[0])) #mostra o primeiro nome
print('Seu último nome é \033[4;32m{}\033[m.'.format(nome[len(nome)-1])) #mostra o último nome
print('\033[31m-\033[m' * 28) #fim