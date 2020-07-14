#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: o primeiro valor é maior; o segundo valor é maior; são iguais.
print('---COMPARANDO VALORES---') #titúlo
n1 = int(input('Primeiro número inteiro: ')) #input do primeiro valor na variavel n1
n2 = int(input('Segundo número inteiro: ')) #input do segundo valor na variavel n2
if n1 > n2: #se n1 for maior que n2 execute o comando abaixo e termine
    print('o primeiro valor é \033[33mMAIOR\033[m')
elif n2 > n1: #se n2 for maior que n1 execute o comando abaixo e termine
    print('O segundo valor é \033[33mMAIOR\033[m.')
else: #se nenhuma das afirmações anteriores forem verdadeiras
    print('Os dois valores são \033[33mIGUAIS\033[m') #os números sao iguais
print('-' * 24) #fim
