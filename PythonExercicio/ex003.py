#crie um programa que leia dois numeros e mostre a soma entre eles, tipos primitivos e saidas de dados
from time import sleep #importando a o sleep para simular um carregamento
print('\033[31m-------SOMAND0-------\033[m') #titulo do programa em vermelho e negrito
n1 = int(input('Digite um valor: ')) #varivel que recebe o valor do primeiro numero por input
n2 = int(input('Digite outro valor : ')) #input do segundo numero
s = n1 + n2 #variavel que recebe a soma dos dois numeros de input
print('\033[;31mPROCESSANDO...\033[m') #print para simular o processamento
sleep(1) #comando sleep 
print(f'A soma entre \033[31m{n1}\033[m e \033[31m{n2}\033[m é \033[31m{s}\033[m.') #reposta do programa com a soma dos números inseridos pelo usuário
