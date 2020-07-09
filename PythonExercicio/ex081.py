#Crie um programa que val ler vários números e colocar em uma lista. Depois mostre: a)quanros numeros foram digitados; b)a lista ordenada decrescente; c)se o valor 5 foi digitado.
print('-' * 45)
print(f'{"ADD NÚMEROS":^45}')
print('-' * 45)
lista = list() #inicia lista vazia
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    print(f'\033[33mO número {num} foi adicionado a lista.\033[m')
    res = str(input('Deseja adicionar mais números a lista? [S/N] ')).strip().upper()[0]
    while res not in 'SN':
        print('\033[31mInválido, tente novamente.\033[m')
        res = str(input('Deseja adicionar mais números a lista? [S/N] ')).strip().upper()[0]
    if res == 'N':
        print('-' * 45)
        break
print(f'A lista contém {len(lista)} valores')
lista.sort(reverse=True)
print(f'Lista em ordem descrescente: {lista}')
if 5 in lista:
    print(f'A lista \033[33mCONTÉM\033[m o número 5.')
else:
    print(f'A lista \033[31mNÃO CONTÉM\033[m o número 5')
print('-' * 45)
