#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final, mostre: a média de idade; nome do homem mais velho; quantas mullheres tem menos de 21 anos.
somaidade = mediaidade = maioridadehomem = totmulher20 = 0 #inicializacao das variaveis
for p in range(1, 5): #repeticao de 1 ate 4
    print(f'=== {p}º PESSOA ===') #print do cabecalho 
    nome = str(input('Nome: ')).strip() #varivael nome recebe o input do nome da pessoa (desconsiderando espacos com o strip)
    idade = int(input('Idade: ')) #variavel idade recbe um valor inteiro da idade do usuario
    sexo = str(input('Sexo [M/F]: ')).strip() #variavel sexo recebe o input do sexo do usuario 
    somaidade += idade #variavel somaidade recebe o valor dela mais a idade
    if p == 1 and sexo in 'Mm': #se for a primeira repeticao e sexo for masculino
        maioridadehomem = idade #maioridadehomem recebe a idade informada
        nomevelho = nome #nomevelho recebe o nome informado
    if sexo in 'Mn' and idade > maioridadehomem: #se sexo for masculino e a idade for maior que a maioridadehomem
        maioridadehomem = idade #maioridadehomem recebe a nova idade informada
        nomevelho = nome #nomevelho recebe o novo nome informado
    if sexo in 'Ff' and idade < 20: #se sexo for feminino e a idade for menor que 20
        totmulher20 += 1 #total de mulher com menor de 20 anos recebe mais um
mediaidade = somaidade / 4 #calculo da media da idade na variavel mediaidade
print(f'A média de idade do grupo é \033[33m{mediaidade}\033[m anos') #print formatado com a media de idade do grupo
print(f'O homem mais velho tem \033[33m{maioridadehomem}\033[m anos e se chama \033[33m{nomevelho}\033[m') #print formatado com a idade e nome do homem mais velho
print(f'Ao todo são \033[33m{totmulher20}\033[m mulheres com menos de \033[33m20\033[m anos.') #print formatado com o total de mulheres menores de 20 anos
