#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
from time import sleep
print('\033[33m---PAR OU IMPÁR?---\033[m')
n = int(input('Digite um número: ')) #input do número digitado pelo usuário na variavel n
print('\033[33mPROCESSANDO...\033[m')
sleep(1)
if n % 2 == 0: #se o resto da divisao por dois for zero o numero é par
    print(f'O número {n} é \033[4;33mPAR\033[m.') #mensagem que aparece caso o número for par
else: #senão
    print(f'O número {n} é \033[4;33mIMPÁR\033[m.') #mensagem caso o número seja ímpar
print('\033[33m-\033[m' * 19)
