#faça um progarama que leia a largura e a altura de uma paredee em metros, calcule sua area e a quantidade necessaria de tinta para pinta-la sabendo
#que cada litro de tinta pinta uma area de 2m²
#operadores aritimeticos, aula 07'
from time import sleep
print('\033[1;31m---PINTANDO A PAREDE---\033[m')
l = float(input('Insira a largura da parede em metros: ')) #input da largura
al = float(input('Insira a altura da parede em metros: ')) #input da altura
a = l*al #multiplicando a largura pela altura para ter a área total da parede
q = a/2 #calculando a quantidade de tinta de acordo com a área da parede e a informação de que cada litro pinta 2m²
print('\033[32mPROCESSANDO...\033[m')
sleep(1)
print('Para pintar \033[32m{}m²\033[m você vai precisar de \033[32m{:.2f}L\033[m de tinta'.format(a, q)) #mostrando o resultado