#crie um programa onde o usuário possa digitar 7 valores númericos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. Mostre os valores em ordem cresc
numeros = [], []
print('-' * 40)
print('{:^40}'.format('PAR E IMPAR'))
print('-' * 40)
for c in range(1, 8):
    n = int(input(f'Digite o {c}o número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print('-' * 40)
print(f'Os números pares foram {sorted(numeros[0])}')
print(f'Os números ímpares foram {sorted(numeros[1])}')
print('-' * 40)
