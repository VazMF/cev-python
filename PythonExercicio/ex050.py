#Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
print('\033[31m-=SOMA-DOS-PARES=-\033[m')
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}.'.format(cont, soma))
print('\033[31m-=-\033[m' * 6)
