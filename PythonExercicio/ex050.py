#Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
print('\033[31m-=SOMA-DOS-PARES=-\033[m')
soma = cont = 0 #declaracao das variaveis
for c in range(1, 7): #repita de 1 ate 7
    num = int(input(f'Digite o {c}° valor: ')) #input do numero na variavel num
    if num % 2 == 0: #se o numero for par
        soma += num #soma recebe soma mais num
        cont += 1 #cont recebe cont mais um
print(f'Você informou {cont} números PARES e a soma foi {soma}.')
print('\033[31m-=-\033[m' * 6)
