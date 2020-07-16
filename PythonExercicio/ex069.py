#crie um programa que leia a idade e o sexo de várias pessoas. a cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. no final mostre:
#quantas pessoas tem mais de 18; quantos homens foram cadastrados; quantas mulheres tem menos de 20 anos.
print('\033[35m-=-CADASTRO-=-\033[m') #titulo
tot18 = totH = totM20 = 0 #inicializa as variaveis com 0
while True: #loop infinito
    idade = int(input('Informe a idade: ')) #input da idade 
    sexo = ' ' #sexo recebe vazio
    while sexo not in 'MF': #enquqnato sexo nao for M ou F
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0] #pede po input do sexo
    print('\033[35m-\033[m' * 15) #print de resultado
    if idade >= 18: #se a idade for maior ou igual a 18
        tot18 += 1 #tootal de pessoas com 18 recebe + 1
    if sexo == 'M': #se sexo for igual a M
        totH += 1 #total de homens recebe mais um
    if sexo == 'F' and idade < 20: #se sexo for igual a F e idade for menor que 20
        totM20 += 1 #tottal de mulheres menores de 20 recebe mais um
    resp = ' ' #resposta recebe vazio
    while resp not in 'SN': #enquanto resposta nao for S ou N
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0] #input da resposta
    print('\033[35m-\033[m' * 15) #print do resultado
    if resp == 'N': #se a resposta for N
        break #interrompe o loop
print(f'Total de pessoas com mais de 18 anos: {tot18}') #prints formatados
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')
