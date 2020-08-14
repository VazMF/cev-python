#crie um programa que leia o nome e o preço de vários produtos. o programa deve perguntar se o usuário vai continuar. no final mostre:
#qual é o total de gastos na compra; quantos produtos custam mais de R$1000; qual o produto mais barato.
print(f'{" SHOP ":-^40}') #titulo
total = totmil = menor = cont = 0 #inicializa as variaveis com 0
barato = '' #barato recebe vazio
while True: #loop infinito
    nome = str(input('Nome do produto: ')).strip() #input do nome do produto
    preco = float(input('Preço do produto: R$')) #input do preço do produto
    cont += 1 #contador recebe mais um
    total += preco #total receebe total mais preço
    if preco > 1000: #se o preço for maior que 1000
        totmil += 1 #total mil recebe total mil mais um
    if cont == 1 or preco < menor: #se for a primeria repeticao ou o preço for menor que o valor da variavel menor
        menor = preco #menor recebe o preço
        barato = nome #barato recebe o nome
    resp = ' ' #resposta recebe vazio
    while resp not in 'SN': #enquanto a resposta nao for S ou N
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0] #input da resposta
        print('-' * 40) #print de resultado
    if resp == 'N': #se a resposta for N
            break #interrompe o while
print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'O total da compra foi R${total:.2f}') #print do total da compra
print(f'Temos {totmil} produtos custando mais de R$1000') #print da quantidade de produtos que custaram mais de 1000
print(f'Produto mais barato foi {barato} que custou R${menor:.2f}') #print do produto mais barato e o preço
