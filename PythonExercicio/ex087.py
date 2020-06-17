#aprimore o exercicio anterior mostrnado: a soma dos valores pares; a soma dos valores da terceira coluna; o maior valor da segunda linha.
print('-' * 45)
print('{:^45}'.format('MATRIZ 2.0'))
print('-' * 45)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
p = 0
t = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            p += matriz[l][c]
print('-' * 45)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-' * 45)
print(f'A soma dos pares é: {p}')
print(f'Soma dos valores da terceira coluna: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
for i in matriz[1]:
    if i > maior:
        maior = i
print(f'O maior valor da segunda linha: {maior}')
print('-' * 45)
