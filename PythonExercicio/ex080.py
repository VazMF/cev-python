#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista. já na posição correta de inserção (sem usar sort()). Mostrar lista ordenada.
print('-' * 30)
numList = [] #inicia uma lista vazia
for c in range(0, 5): #repeat 5 vezes para ler os números
    num = int(input("Digite um número: ")) #input dos números
    if c == 0 or num > numList[-1]: #se o num for o primeiro valor lido ou num for maior que o último valor da lista
        numList.append(num) #adiciona o valor a lista
        print('\033[33mAdicionado ao final da lista.\033[m')
    else: #senão
        pos = 0 #posição recebe 0
        while pos < len(numList): #enquanto posição for menor que a lista
            if num <= numList[pos]: #se o valor lido é menor ou igual
                numList.insert(pos, num) #insere o num lido na posição pos.
                print(f'\033[33mAdicionado na posição {pos} da lista.\033[m')
                break #quebra de enquanto
            pos += 1 #variavel para mudar a posição
print('-' * 30)
print(f'LISTA ORDENADA: {numList}')
