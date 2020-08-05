#refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.
#equilátero = todos os lados iguais; isósceles = dois lados iguais; escaleno = todos diferentes.
print('\033[31m=-=ANALISANDO TRIÂNGULOS=-=\033[m') #titulo
r1 = float(input('Primeiro segmento: ')) #input do segmento na variavel r1
r2 = float(input('Segundo segmento: ')) #input do segmento na variavel r2
r3 = float(input('Terceiro segmento: ')) #input do segmento na variavel r3
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: #se r1 for menor que r2 mais r3 e r2 for menor que r1 mais r3 e r3 for menor que r1 mais r2
    print('Os segmentos acima \033[33mPODEM\033[m formar um triângulo ', end='') #print informando que é possivel formar o triangulo
    if r1 == r2 == r3: #se r1 for igual a r2 for igual a r3
        print('\033[33mEQUILÁTERO.\033[m') #print equilatero
    elif r1 != r2 != r3 != r1: #se r1 for diferente de r2 e r3 for diferente de r1
        print('\033[33mESCALENO.\033[m') #print escaleno
    else: #senao
        print('\033[33mISÓSCELES.\033[m') #print isosceles
else: #senao
    print('Os segmentos acima \033[31mNÃO PODEM\033[m formar um triângulo.') #nao é possivel formar triangulo
