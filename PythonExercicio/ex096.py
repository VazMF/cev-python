#Faça um programa que tenha uma função chamada area(), que receba as diimensões de um terreno retangular e mostre a area do terreno

#defindo a função
def area(l, c): #função area com dois parâmetros
    a = l * c #a recebe largura vezes comprimento
    print(f'A área de um terreno \033[33m{l} x {c}\033[m é de \033[33m{a}m²\033[m') #print mostrando as dimensões do terreno


#programa principal
#titulo
print('~' * 45)
print(f'{"CONTROLE DE TERRENOS":^45}')
print('~' * 45)
#variaveis
largura = float(input('Informe a lagura do terreno [m]: ')) #var para ler a largura do tereno em metros
altura = float(input('Informe a comprimento do terreno [m]: ')) #var para ler a altura do terreno em metros
area(largura, altura) #chamada da função area
