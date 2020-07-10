#faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: a)qtd pessoas cadastradas; b)lista com + pesadas, c)lista + leves.
from time import sleep
cadastros = list()
dados = list()
maior = menor = 0
print('-' * 45)
print(f'{"ANALISADOR DE PESOS":^45}')
while True:
    print('-' * 45)
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(cadastros) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    cadastros.append(dados[:])
    dados.clear()
    print('\033[32mAdicionado com sucesso!\033[m')
    res = str(input('Deseja cadastrar mais pessoas? [S/N] ')).strip().upper()[0]
    while res not in 'SN':
        print('\033[31m[ERROR] Digite SIM ou NÃO.\033[m')
        res = str(input('Deseja cadastrar mais pessoas? [S/N] ')).strip().upper()[0]
    if res == 'N':
        print('FINALIZANDO...')
        sleep(1)
        print('-' * 45)
        print(f'{"RESULTADO":^45}')
        print('-' * 45)
        print(f'Foram cadastradas \033[32m{len(cadastros)}\033[m pessoas.')
        print(f'O maior peso foi \033[32m{maior}kg\033[m. Peso de ', end='')
        for p in cadastros:
            if p[1] == maior:
                print(f'[{p[0]}] ', end='')
        print()
        print(f'O menor peso foi \033[32m{menor}kg\033[m. Peso de ', end='')
        for p in cadastros:
            if p[1] == menor:
                print(f'[{p[0]}] ', end='')
        print()
        break
print('-' * 45)
print('Obrigado por utilizar o nosso programa :)')
