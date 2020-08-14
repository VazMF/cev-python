#Crie um programa que val ler vários números e colocar em uma lista. Depois mostre: a)quanros numeros foram digitados; b)a lista ordenada decrescente; c)se o valor 5 foi digitado.
print('-' * 45)
print(f'{"- ADD NÚMEROS -":^45}') #titulo
print('-' * 45)
lista = list() #inicia lista vazia
while True: #looping infinito
    num = int(input('Digite um número: ')) #input do numero da variavel num
    lista.append(num) #append do numero lido na lista
    print(f'\033[33mO número {num} foi adicionado a lista.\033[m') #confirmacao de add
    res = str(input('Deseja adicionar mais números a lista? [S/N] ')).strip().upper()[0] #input da variavel resposta
    while res not in 'SN': #enquanto a resposta nao for s ou n
        print('\033[31mInválido, tente novamente.\033[m') #print do erro
        res = str(input('Deseja adicionar mais números a lista? [S/N] ')).strip().upper()[0] #pede o input da resposta novamente
    if res == 'N': #se a resposta for nao
        print('-' * 45) #print de resultado
        break #interrompe o while
print(f'A lista contém {len(lista)} valores') #print de quantos numeros tem a lista por meio do lenght
lista.sort(reverse=True) #ordenando a lista em ordem descrescente
print(f'Lista em ordem descrescente: {lista}') #print da lista em ordem decrescente
if 5 in lista: #se a lista tiver o numero 5
    print(f'A lista \033[33mCONTÉM\033[m o número 5.') #print que a lista contém o numero 5
else: #senao
    print(f'A lista \033[31mNÃO CONTÉM\033[m o número 5') #print que a lista nao contem o numero 5
print('-' * 45)
