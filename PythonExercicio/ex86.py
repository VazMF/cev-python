#crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = []
print('-' * 30)
print('{:^30}'.format('MATRIZ'))
print('-' * 30)
for c in range(0, 9):
    matriz.append(int(input('Digite um número: ')))
print('-' * 30)
print([matriz[0]], [matriz[1]], [matriz[2]])
print([matriz[3]], [matriz[4]], [matriz[5]])
print([matriz[6]], [matriz[7]], [matriz[8]])
