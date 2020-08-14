#Crie um programa que leia, nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
#e todos os dicionários em uma lista. No final, mostre: a) quantas pessoas foram cadastradas; b)a media de idade do
#grupo; c)uma lista com todas as mulheres; d)uma lista com todas as pessoas com idade acima da média.
galera = list() #inicializa uma lista vazia
pessoa = dict() #inicializa um dicionario vazio
soma = 0 #variavel soma recebe 0
print('-' * 40)
print(f'{">> CADASTRO DE PESSOAS <<":^40}') #titulo
print('-' * 40)
while True: #looping infinito
    pessoa['nome'] = str(input('Nome: ')) #input do nome no dicionario no indice nome
    while True: #looping infinito
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0] #input do sexo no indice sexo do dicionario
        if pessoa['sexo'] in 'MF': #se o sexo for masculino ou feminino
            break #interrompe o while
        print('\033[31mERRO! Por favor digite M ou F.\033[m') #print de erro
    pessoa['idade'] = int(input(f'Qual a idade de {pessoa["nome"]}? ')) #input da idade no indice idade no dicionario
    soma += pessoa['idade'] #soma recebe soma mais idade
    galera.append(pessoa.copy()) #append de uma copia de pessoa para galera
    while True: #looping infinito
        resp = str(input('Deseja cadastrar mais pessoas? [S/N] ')).upper()[0] #input da resposta
        print('-' * 40)
        if resp in 'SN': #se a resposta for S ou N
            break #interrompe o while
        print('\033[31mERRO! Responda apenas S ou N.\033[m') #print do erro
    if resp == 'N': #se a resposta for nao
        break #interrompe o while
print(f'Ao todo foram cadastradas \033[34m{len(galera)}\033[m pessoas.') #print do total de pessoas cadastradas
print(f'A média de idade do grupo é \033[34m{soma/len(galera):5.1f}\033[m anos.') #print da media de idade do grupo
print(f'As mulheres cadastradas foram ', end='') #print das mulheres cadastradas
for p in galera: #repeticao para cada pessoa em galera
    if p['sexo'] == 'F': #se o sexo da pessoa for feminino
        print(f'\033[34m[{p["nome"]}]\033[m ', end='') #print o nome 
print() #print para quebra de linha
print('Pessoas que estão acima da média de idade: ') #print para pessoas acima da media de idade
for p in galera: #repeticao para cada pessoa em galera
    if p['idade'] > soma/len(galera): #se a idade for maior que a media
        for k, v in p.items(): #repeticao para cada chave e valor em itens
            print(f'{k} = \033[34m{v};\033[m ', end='') #print para cada chave a valor sem quebrar linha
        print() #print para quebrar linha
print('<< ENCERRADO >>')
