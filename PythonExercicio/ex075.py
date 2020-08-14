#desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final mostre:
#quantas vezes apareceu o valor 9; em que posição foi digitado o primeiro valor 3; quais foram os números pares.
print('-' * 40)
print(f'{"-ANALISADOR DE TUPLAS-":^40}') #titulo
print('-' * 40)
num = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')), int(input('Digite o último número: '))) #tupla com 4 inputs de numero
print(f'Você digitou os valores {num}') #print da tupla
print(f'O número nove apareceu {num.count(9)} vezes') #print mostrando quantas vezes o 9 apareceu por meio do count
if 3 in num: #se tem o numero 3 na tupla
    print(f'O número 3 apareceu na {num.index(3) + 1}º posição') #print o a posição do em que o numero 3 aparece (index)
else: #senao
    print('O número 3 não apareceu em nenhuma posição.') #print informando que o 3 nao aparece
print(f'Os valores pares digitados foram ', end='') #print dos valores pares digitados sem quebrar linha
for n in num: #repeticao para analisar cada numero da tupla
    if n % 2 == 0: #se o numero for par
        print(n, end=' ') #print do numero
