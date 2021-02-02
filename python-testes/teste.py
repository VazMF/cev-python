#VALORES ÚNICOS EM UMA LISTA
lista = []
while True:
    answer = ' '
    while True:
        num = int(input('Digite um valor: '))
        if num not in lista:
            lista.append(num)
            print('Valor adicionado com sucesso...')
            break
        else:
            print('Valor duplicado! Não vou adicionar...')
    while answer not in 'SN':
        answer = input('Deseja continuar? [s/n] ').strip().upper()[0]
    if answer == 'N':
        break
print('-=' * 40)
lista.sort()
print(f'Você digitou os valores {lista}')