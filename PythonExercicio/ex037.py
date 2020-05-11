#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário; 2 para octal e 3 para hexadecimal
print('\033[31m=-=CONVERTENDO=-=\033[m')
num= int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para \033[32mBINÁRIO\033[m
[ 2 } converter para \033[32mOCTAL\033[m
[ 3 ] converter para \033[32mHEXADECIMAL\033[m''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[31mOPÇÃO INVÁLIDA. TENTE NOVAMENTE.\033[m')
print('\033[31m=-=\033[m' * 6)

