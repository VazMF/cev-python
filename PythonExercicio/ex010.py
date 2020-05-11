#crie um programa que leia quantos reais uma pessoa tem na carteira e converta pra dolares
#operadores aritimeticos, aula 07
from time import sleep
print('\033[1;31m---CONVERSOR DE MOEDAS---\033[m')
r = float(input('Insira um valor em reais: R$'))
print('\033[32mDÓLAR\033[m: R${:.2f} valem U$${:.2f} '.format(r, (r/4.20)))
print('\033[32mDÓLAR CANADENSE\033[m: R${:.2f} valem C${:.2f}'.format(r, r/3.22))
print('\033[32mEURO\033[m: R${:.2f} valem €{:.2f}'.format(r,r/4.67))

