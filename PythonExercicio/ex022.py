#Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas, minúsculas, quantidade de letras sem considerar espaços, letras 1 nome.
#aula09, manipulando texto/string
from time import sleep
print('\033[31m---ANALISANDO NOMES----\033[m') #titúlo
nome = str(input('Digite seu nome completo: ')).strip() #input do nome
print('\033[32mANALISANDO SEU NOME...\033[m')
sleep(1)
print('Seu nome em maiúsculas é \033[32m{}\033[m'.format(nome.upper())) #o nome do input em caps por meio do upper
print('Seu nome em minúsculas é \033[32m{}\033[m'.format(nome.lower())) #nome do input em minusculas por meio do lower
print('Seu nome tem ao todo \033[32m{}\033[m letras'.format(len(nome)-nome.count(' '))) #contando as letras do nome com o len
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split() #svariavel que separa os nomes pelo split
print(separa) #mostrando a variavel
print('Seu primeiro nome é \033[32m{}\033[m e ele tem \033[32m{}\033[m letras'.format(separa[0], len(separa[0]))) #resultado
print('\033[31m-\033[m' * 22)