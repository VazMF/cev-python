#Crie um programa que leia vários valores e coloque-os em uma lista. Depois, crie duas listas extras que vão conter apenas valores pares e os valores impares. Ao final print tudo.
print('-' * 40)
print('{:^40}'.format('LISTA PAR OU ÍMPAR'))
print('-' * 40)
lista = list()
listaPar = list()
listaImpar = list()
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    print('\033[33mValor adicionado com sucesso\033[m')
    res = str(input('Deseja adicionar mais números a lista? [S/N] ')).strip().upper()[0]
    while res not in 'SN':
        print('\033[31mInválido. Tente novamente.\033[m')
        res = str(input('Deseja adicionar mais números a lista? [S/N] ')).strip().upper()[0]
    if res == 'N':
        if num % 2 == 0:
            listaPar.append(num)
        elif num % 2 == 1:
            listaImpar.append(num)
        break
    elif num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
print(f'LISTA: {lista}')
print(f'LISTA DE PARES: {listaPar}')
print(f'LISTA DE ÍMPARES: {listaImpar}')
