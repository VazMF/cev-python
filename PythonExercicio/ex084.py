#faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: a)qtd pessoas cadastradas; b)lista com + pesadas, c)lista + leves.
from time import sleep
cadastros = list() #inicializa uma lista vazia de cadastros
dados = list() #inicializa uma lista vazia de dados
maior = menor = 0 #inicializa as variaveis maior e menor como zero
print('-' * 45)
print(f'{"ANALISADOR DE PESOS":^45}') #titulo
while True: #looping infinito
    print('-' * 45) #print para resultado
    dados.append(str(input('Nome: '))) #input do nome na lista de dados
    dados.append(float(input('Peso: '))) #input do peso na lista dados
    if len(cadastros) == 0: #se o tamanho da lista de cadastros for 0
        maior = menor = dados[1] #maior e menor receberam o primeiro peso lido
    else: #senao
        if dados[1] > maior: #se o dados no indice 1 (peso) for maior que o valor da variavel maior
            maior = dados[1] #maior recebe o novo valor do peso
        if dados[1] < menor: #se dados no indice 1 (peso) for menor que o valor da varivael menor
            menor = dados[1] #menor recebe o novo valor do peso
    cadastros.append(dados[:]) #cadastros recebe uma copia de dados
    dados.clear() #limpa a lista dados
    print('\033[32mAdicionado com sucesso!\033[m') #print informando que o valor foi adicionado com sucesso
    res = str(input('Deseja cadastrar mais pessoas? [S/N] ')).strip().upper()[0] #input da variavel resposta 
    while res not in 'SN': #enquanto a resposta nao for S ou N
        print('\033[31m[ERROR] Digite SIM ou NÃO.\033[m') #print erro
        res = str(input('Deseja cadastrar mais pessoas? [S/N] ')).strip().upper()[0] #pede o input da resposta novamente
    if res == 'N': #se a resposta for nao
        print('FINALIZANDO...') #print finalizando o programa
        sleep(1)
        print('-' * 45)
        print(f'{"RESULTADO":^45}') #print de resultado
        print('-' * 45)
        print(f'Foram cadastradas \033[32m{len(cadastros)}\033[m pessoas.') #print formatado com o total de pessoas cadastradas
        print(f'O maior peso foi \033[32m{maior}kg\033[m. Peso de ', end='') #print com o maior peso lido sem quebrar linha
        for p in cadastros: #repeticao para cada pessoas na lista cadastros
            if p[1] == maior: #se o peso for igual ao valor da variavel maior
                print(f'[{p[0]}] ', end='') #print o nome da pesssoa, sem quebrar linha
        print() #print para quebrar linha
        print(f'O menor peso foi \033[32m{menor}kg\033[m. Peso de ', end='') #print formatado com o menor peso sem quebrar linha
        for p in cadastros: #repeticao para cada pessoa da lista de cadastros
            if p[1] == menor: #se o peso for igual ao valor da variavel menor
                print(f'[{p[0]}] ', end='') #print do nome da pessoa ou pessoas com menor peso
        print() #print para quebrar linha
        break #interrompe o while
print('-' * 45)
print('Obrigado por utilizar o nosso programa :)')
