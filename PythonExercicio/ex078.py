#Faça um programa que leia 5 valores e guarde-os em uma lista. No final mostre qual foi o maior e o menor valor digitado e suas posições
print('-' * 40)
print(f'{"MAIOR E MENOR NA LISTA":^40}')
print('-' * 40)
lista = list()
maior = []
menor = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Você digitou os valores {lista}')
for indice, valores in enumerate(lista):
    if valores == max(lista):
        maior.append(indice)
    if valores == min(lista):
        menor.append(indice)
print('-' * 40)
print(f'O maior valor digitado foi {max(lista)}, na posição {maior}')
print(f'O menor valor digitado foi {min(lista)}, na posição {menor}')
