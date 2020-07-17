#crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
print('-' * 40)
print(f'{"MATRIZ":^40}') #titulo
print('-' * 40)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #inicializa uma lista matriz com 3 listas iternas com 3 numeros cada
for l in range(0, 3): #repeticao para cada linha 
    for c in range(0, 3): #repeticao para cada coluna
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: ')) #input do valor mostrando na a posicao de insercao
print('-' * 40) #print para resultado
for l in range(0, 3): #repeticao para cada linha
    for c in range(0, 3): #repeticao para cada coluna
        print(f'[{matriz[l][c]:^5}]', end='') #print a coluna e linha da matriz sem quebrar linha
    print() #quebra linha no final
