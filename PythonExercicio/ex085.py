#crie um programa onde o usuário possa digitar 7 valores númericos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. Mostre os valores em ordem cresc
numeros = [[], []] #declaracao da lista com dois indices
print('-' * 40)
print('{:^40}'.format('PAR E IMPAR')) #titulo
print('-' * 40)
for c in range(1, 8): #repeticao para ler os sete numeros
    n = int(input(f'Digite o {c}o número: ')) #input do numero
    if n % 2 == 0: #se o numero for par
        numeros[0].append(n) #append no primeiro indice da lsta numeros
    else: #senao
        numeros[1].append(n) #append no segundo indice da lista numeros
print('-' * 40)
print(f'Os números pares foram {sorted(numeros[0])}') #print dos numeros pares em orderm crescente
print(f'Os números ímpares foram {sorted(numeros[1])}') #print dos numeros impares em ordem crescente
print('-' * 40)