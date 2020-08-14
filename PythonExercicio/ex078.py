#Faça um programa que leia 5 valores e guarde-os em uma lista. No final mostre qual foi o maior e o menor valor digitado e suas posições
print('-' * 45)
print(f'{"MAIOR E MENOR NA LISTA":^45}') #titulo
print('-' * 45)
lista = list() #inicializacao de lista vazia
maior = [] #inicializacao de lista vazia
menor = [] #inicializacao de lista vazia
for c in range(0, 5): #repeticao de 1 a 5
    lista.append(int(input(f'Digite um valor para a {c}° posição: '))) #input do valorna lista
print(f'Você digitou os valores {lista}') #print mostrando os valores da lista
for indice, valores in enumerate(lista): #repeticao para cada indice e valores na lista enumerada
    if valores == max(lista): #se o valor for o max da lista
        maior.append(indice) #append na lista de maiores
    if valores == min(lista): #se o valor for o minimo da lista
        menor.append(indice) #append na lista dos menores
print('-' * 45) #print para o resultado
print(f'O maior valor digitado foi {max(lista)}, na posição {maior}') #print formatado com o maior valor digitado e a posicao
print(f'O menor valor digitado foi {min(lista)}, na posição {menor}') #print formatado com o menor valor e a posicao
