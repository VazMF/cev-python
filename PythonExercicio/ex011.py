#faça um progarama que leia a largura e a altura de uma paredee em metros, calcule sua area e a quantidade necessaria de tinta para pinta-la sabendo que cada litro de tinta pinta uma area de 2m²'
print('\033[1;31m---PINTANDO A PAREDE---\033[m') #titulo
l = float(input('Insira a largura da parede em metros: ')) #input da largura para variavel l
al = float(input('Insira a altura da parede em metros: ')) #input da altura para a variavel al
a = l*al #multiplicando a largura pela altura para ter a área total da parede e jogando na variavel a
q = a/2 #calculando a quantidade de tinta de acordo com a área da parede e a informação de que cada litro pinta 2m²
print(f'Para pintar \033[32m{a}m²\033[m você vai precisar de \033[32m{q:.2f}L\033[m de tinta') #mostrando o resultado