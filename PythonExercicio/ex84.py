#faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: a)qtd pessoas cadastradas; b)lista com + pesadas, c)lista + leves.
from time import  sleep #import do sleep
cadastros = list() #cria lista cadastros vazias
dados = list() #cria lista dados vazia
pessoas = 0 #cria a varivel pessoas comecando com zero
pesados = list() #cria lista pesados vazia
leves = list() #cria lsta leves vazia
while True: #enquanto infinito
    print('-----------------------------------------') #frescura
    dados.append(str(input('Nome: '))) #a string que for lida é apendada a lista dados
    dados.append(int(input('Peso: '))) #o inteiro que for lido é apendado a lista dados
    cadastros.append(dados[:]) #cadastros recebe uma copia de dados
    dados.clear() #limpa a lista dados
    pessoas += 1 #contador de pessoas recebe mais um
    print('\033[32mAdicionado com sucesso!\033[m') #print de confirmação de add
    res = str(input('Deseja cadastrar mais pessoas? [S/N] ')).strip().upper()[0] #pergunta se quer continuar
    while res not in 'SN': #caso a resposta não seja sim ou não
        print('\033[31m[ERROR] Digite SIM ou NÃO.\033[m') #print erro
        res = str(input('Deseja cadastrar mais pessoas? [S/N] ')).strip().upper()[0] #pergunta novamente
    if res == 'N': #se a resposta for não
        print('FINALIZANDO...') #programa finaliza
        sleep(3)
        print('----------------RESULTADO----------------')
        for i in cadastros: #para cada indice da lista cadastros
            if i[1] >= 100: #se o conteudo do indice do peso for maior ou igual a 100
                pesados.append(i[0]) #append na lista de pesados
            elif i[1] <= 60: #senao, se o peso for menor ou igual a 60
                leves.append(i[0]) #append na lista de leves
        print(f'Foram cadastradas {pessoas} pessoas.') #print quantidade de pessoas
        print(f'As pessoas mais pesadas são: {pesados}') #print nome das pessoas mais pesadas
        print(f'As pessoas mais leves são: {leves}') #print nome das pessoas mais leves
        break #break para sair do while
print('-----------------------------------------') #frescura
print('Obrigado por utilizar o nosso programa :)') #agradcimento
