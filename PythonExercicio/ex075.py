#desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final mostre:
#quantas vezes apareceu o valor 9; em que posição foi digitado o primeiro valor 3; quais foram os números pares.
print('-' * 30)
print('{:^30}'.format('ANALISADOR DE TUPLAS'))
print('-' * 30)
num = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O número nove apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3) + 1}º posição')
else:
    print('O número 3 não apareceu em nenhuma posição.')
print(f'Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
