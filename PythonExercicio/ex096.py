#Faça um programa que tenha uma função chamada area(), que receba as diimensões de um terreno retangular e mostre a area do terreno
def area(l, h):
    a = l * h
    print(f'A área de um terreno \033[33m{l} x {h}\033[m é de \033[33m{a}m²\033[m')


print('\033[33m-' * 45)
print(f'{"CONTROLE DE TERRENOS":^45}')
print('-\033[m' * 45)
largura = float(input('Informe a lagura do terreno [m]: '))
altura = float(input('Informe a altura do terreno [m]: '))
area(largura, altura)
