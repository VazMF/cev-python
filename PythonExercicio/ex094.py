#Crie um programa que leia, nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
#e todos os dicionários em uma lista. No final, mostre: a) quantas pessoas foram cadastradas; b)a media de idade do
#grupo; c)uma lista com todas as mulheres; d)uma lista com todas as pessoas com idade acima da média.
galera = list()
pessoa = dict()
soma = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('\033[31mERRO! Por favor digite M ou F.\033[m')
    pessoa['idade'] = int(input(f'Qual a idade de {pessoa["nome"]}? '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Deseja cadastrar mais pessoas? [S/N] ')).upper()[0]
        print('-' * 40)
        if resp in 'SN':
            break
        print('\033[31mERRO! Responda apenas S ou N.\033[m')
    if resp == 'N':
        break
print(f'Ao todo foram cadastradas {len(galera)} pessoas.')
print(f'A média de idade do grupo é {soma/len(galera):5.1f} anos.')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'[{p["nome"]}] ', end='')
print()
print('Pessoas que estão acima da média de idade: ')
for p in galera:
    if p['idade'] > soma/len(galera):
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
