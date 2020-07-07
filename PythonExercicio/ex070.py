#crie um programa que leia o nome e o preço de vários produtos. o programa deve perguntar se o usuário vai continuar. no final mostre:
#qual é o total de gastos na compra; quantos produtos custam mais de R$1000; qual o produto mais barato.
print('{:-^40}'.format(' SHOP '))
total = totmil = menor = cont = 0
barato = ''
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 40)
    if resp == 'N':
            break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f}')
