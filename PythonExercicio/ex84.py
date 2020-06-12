#faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: a)qtd pessoas cadastradas; b)lista com + pesadas, c)lista + leves.
from time import  sleep
cadastros = list()
dados = list()
pessoas = 0
pesados = list()
leves = list()
while True:
    print('-----------------------------------------')
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    cadastros.append(dados[:])
    dados.clear()
    pessoas += 1
    print('\033[32mAdicionado com sucesso!\033[m')
    res = str(input('Deseja cadastrar mais pessoas? [S/N] ')).strip().upper()[0]
    while res not in 'SN':
        print('\033[31m[ERROR] Digite SIM ou NÃO.\033[m')
        res = str(input('Deseja cadastrar mais pessoas? [S/N] ')).strip().upper()[0]
    if res == 'N':
        print('FINALIZANDO...')
        sleep(3)
        print('----------------RESULTADO----------------')
        for i in cadastros:
            if i[1] >= 100:
                pesados.append(i[0])
            elif i[1] <= 60:
                leves.append(i[0])
        print(f'Foram cadastradas {pessoas} pessoas.')
        print(f'As pessoas mais pesadas são: {pesados}')
        print(f'As pessoas mais leves são: {leves}')
        break
print('-----------------------------------------')
print('Obrigado por utilizar o nosso programa :)')
