#Crie um programa que leia vários valores e coloque-os em uma lista. Depois, crie duas listas extras que vão conter apenas valores pares e os valores impares. Ao final print tudo.
print('-' * 40)
print(f'{"LISTA PAR OU ÍMPAR":^40}') #titulo
print('-' * 40)
lista = list() #inicializacao da lista principal
listaPar = list() #inicializacao da lista de pares
listaImpar = list() #inicializacao da lista de impares
while True: #looping infinito
    num = int(input('Digite um número: ')) #input dos numeros na variavel num
    lista.append(num) #append do numero na lista principal
    print('\033[33mValor adicionado com sucesso\033[m') #print informando que o valor foi adicionado com sucesso
    res = str(input('Deseja adicionar mais números a lista? [S/N] ')).strip().upper()[0] #input da variavel resposta
    while res not in 'SN': #enquanto a resposta nao for S ou N
        print('\033[31mInválido. Tente novamente.\033[m') #print avisando que a resposta é inválida
        res = str(input('Deseja adicionar mais números a lista? [S/N] ')).strip().upper()[0] #input da resposta novamente
    if res == 'N': #se a resposta for N
        if num % 2 == 0: #se o numero for par
            listaPar.append(num) #append do numero na lista par
        elif num % 2 == 1: #senao se o numero for impar
            listaImpar.append(num) #append do numero na lista de impares
        break #interrompe o while
    elif num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
print(f'LISTA: {lista}') #print da lista principal
print(f'LISTA DE PARES: {listaPar}') #print da lista de pares
print(f'LISTA DE ÍMPARES: {listaImpar}') #print da lista de impares
