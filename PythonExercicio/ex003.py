#crie um programa que leia dois numeros e mostre a soma entre eles
#tipos primitivos e saidas de dados
from time import sleep #importando a função sleep para simular um carregamento
print('\033[1;31m---SOMAND0---\033[m') #titulo do programa em vermelho e negrito
n1 = int(input('Digite um valor: ')) #pedindo o input do primeiro número
n2 = int(input('Digite outro valor : ')) #pedindo o input do segundo número
s = n1 + n2 #comando da soma dos números do input
sleep(1) #ativação do sleep
print('\033[;32mPROCESSANDO...\033[m') #sleep funcionando em verde
print('A soma entre \033[32m{}\033[m e \033[32m{}\033[m é \033[1;32m{}\033[m.'.format(n1, n2, s)) #reposta do programa com a soma dos números inseridos pelo usuário
