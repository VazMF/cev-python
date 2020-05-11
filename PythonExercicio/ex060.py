#faça um programa que leia um número qualquer e mostre seu fatorial
print('\033[31m-=-=FATORIAL=-=-\033[m') #titulo
num = int(input('Digite um número para calcular seu fatorial: ')) #input do número desejado
c = num #define o contador como o num inserido no input
f = 1 #fatorial é definido como 1
print('Calculando {}! = '.format(num), end='') #formato do fatorial
while c > 0: #enquanto o contador for maior que 0
    print('{}'.format(c), end='') #mostre o contador
    print(' x ' if c > 1 else ' = ', end='') #se o c for maior que 1 coloque x, senão coloque =
    f = f * c #fatorial é definido como f * c
    c -= 1 #contador é contadore - 1
print('\033[33m{}\033[m'.format(f)) #resultado do fatorial
print('\033[31m=\033[m' * 16)
