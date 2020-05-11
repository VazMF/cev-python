#refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.
#equilátero = todos os lados iguais; isósceles = dois lador=s iguais; escaleno = todos diferentes.
print('\033[31m=-=ANALISANDO TRIÂNGULOS=-=\033[m')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[33mPODEM\033[m formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('\033[33mEQUILÁTERO.\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[33mESCALENO.\033[m')
    else:
        print('\033[33mISÓSCELES.\033[m')
else:
    print('Os segmentos acima \033[31mNÃO PODEM\033[m formar um triângulo.')
print('\033[31m=-=\033[m' * 9)
