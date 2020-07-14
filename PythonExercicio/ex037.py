#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário; 2 para octal e 3 para hexadecimal
print('\033[31m=-=CONVERTENDO=-=\033[m') #titulo
num = int(input('Digite um número inteiro: ')) #input do numero da variavel num
print('''Escolha uma das bases para conversão:
[ 1 ] converter para \033[32mBINÁRIO\033[m
[ 2 ] converter para \033[32mOCTAL\033[m
[ 3 ] converter para \033[32mHEXADECIMAL\033[m''') #print do menu para a escolha da conversao
opção = int(input('Sua opção: ')) #variavel que vai armazenar a opcao escolhida
if opção == 1: #se a opcao for 1
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}') #print do numero convertido por meio do bin
elif opção == 2: #se a opcao for 2
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}') #print do numero convertido para octal por meio do oct
elif opção == 3: #se a opcao for 3
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}') #print do numero convertido para hexadecimal por meio do hex
else: #senao
    print('\033[31mOPÇÃO INVÁLIDA. TENTE NOVAMENTE.\033[m') #print da opcao invalida
print('\033[31m=-=\033[m' * 6)
