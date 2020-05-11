nome = str(input('Nome do cliente: '))
mes = int(input('Mês do aniversário: '))
preco = float(input('Valor da compra: R$'))
parcela = 0

if preco < 699:
    print(f'{nome}, valor a pagar R${preco}.')
else:
    if mes > 12:
        print('Mês inválido.')
        if mes in (1, 2, 3, 4, 5, 6):
            if mes % 2 == 0:
                parcela = preco / 2
                print(f'{nome} pode parcelar a compra de R${preco:.2f} em 2x de {parcela:.2f}')
        else:
            parcela = preco / 3
            print(f'{nome} pode parcelar a compra de R${preco:.2f} em 3x de R${parcela:.2f}')
    if mes in (7, 8, 9, 10, 11, 12):
            if mes % 2 == 0:
                parcela = preco / 3
                print(f'{nome} pode parcelar a compra de R${preco:.2f} em 3x de R${parcela:.2f}')
    else:
        parcela = preco / 2
        print(f'{nome} pode parcelar a compra de R${preco:.2f} em 2x de {parcela:2f}.')
