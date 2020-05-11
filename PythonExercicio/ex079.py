#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os e uma lista. Caso o número já exista, não será adicionado. Exibir os valores em ordem crescente.
print('-' * 40)
print('{:^40}'.format('ORDENADOR CRESCENTE'))
print('-' * 40)
lista = list()
while True:
    resp = ' '
    while True:
        num = (int(input('Digite um valor: ')))
        if num not in lista:
            lista.append(num)
            print('\033[33mValor adicionado.\033[m')
            print('-' * 40)
            break
        else:
            print('\033[31mErro. Não posso duplicar valores.\033[m')
            print('-' * 40)
    while resp not in 'sn':
        resp = str(input('Deseja continuar digitando? [s/n] ')).strip().lower()[0]
        print('-' * 40)
    if resp == 'n':
        break
print(f'Os valores informados foram {sorted(lista)}')
print('-' * 40)
