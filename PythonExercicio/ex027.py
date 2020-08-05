#faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o segundo nome separadamente
from time import sleep #impor do sleep
print('\033[32m---------PRIMEIRO E ÚLTIMO NOME---------\033[m') #titúlo
n = str(input('Nome completo: ')).strip() #input do nome completo na variavel n
nome = n.split() #variavel que armazena os nomes separados pelo split
print('\033[32mANALISANDO NOME...\033[m')
sleep(1)
print('Muito prazer em te conhecer!') #msg de boas vindas
print(f'Seu primeiro nome é \033[4;32m{nome[0]}\033[m.') #mostra o primeiro nome
print(f'Seu último nome é \033[4;32m{nome[len(nome)-1]}\033[m.') #mostra o último nome
