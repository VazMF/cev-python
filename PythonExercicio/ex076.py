#crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#no final, mostre uma listagem de preços organizado os dados em forma tabular.
print('=' * 40)
print(f'{"~ LISTAGEM DE PREÇOS ~":^40}') #titulo
print('=' * 40)
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Tranferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90) #tupla com os itens e preço
for pos in range(0, len(listagem)): #reprticao para cada posicao de 0 ate o tamanho da tupla
    if pos % 2 == 0: #se a posicao tiver indice par (é preço)
        print(f'{listagem[pos]:.<30}', end='') #print formatado com a posicao alinhada com 30 pontos a esquerda
    elif pos % 2 == 1: #se a posicao tiver indice impar (é nome do item)
        print(f'R${listagem[pos]:>7.2f}') #print formaado alinhando o nome do item a direita
print('=' * 40)
