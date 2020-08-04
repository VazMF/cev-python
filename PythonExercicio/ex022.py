#Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas, minúsculas, quantidade de letras sem considerar espaços, letras 1 nome.
from time import sleep #import sleep
print('\033[32m------------------ANALISANDO NOMES-------------------\033[m') #titúlo
nome = str(input('Digite seu nome completo: ')).strip() #input do nome na variavel nome
print('\033[32mANALISANDO...\033[m') #print para simular a analise
sleep(1) #sleep
print(f'Seu nome em maiúsculas é \033[32m{nome.upper()}\033[m') #o nome do input em caps por meio do upper
print(f'Seu nome em minúsculas é \033[32m{nome.lower()}\033[m') #nome do input em minusculas por meio do lower
print(f'Seu nome tem ao todo \033[32m{len(nome) - nome.count(" ")}\033[m letras') #contando as letras do nome com o len
separa = nome.split() #variavel que separa os nomes pelo split
print(separa) #mostrando a variavel
print(f'Seu primeiro nome é \033[32m{separa[0]}\033[m e ele tem \033[32m{len(separa[0])}\033[m letras') #resultado
