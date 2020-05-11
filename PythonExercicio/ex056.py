#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final, mostre: a média de idade; nome do homem mais velho; quantas mullheres tem menos de 21 anos.
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('=== {}º PESSOA ==='.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é \033[33m{}\033[m anos'.format(mediaidade))
print('O homem mais velho tem \033[33m{}\033[m anos e se chama \033[33m{}\033[m'.format(maioridadehomem, nomevelho))
print('Ao todo são \033[33m{}\033[m mulheres com menos de \033[33m20\033[m anos.'.format(totmulher20))
