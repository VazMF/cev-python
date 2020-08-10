#faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = cont = 0 #declaracao das variaveis
for c in range(1, 501, 2): #para c no intervalo de 1 ate 500 
    if c % 3 == 0: #se o resto da divisao de c por 3 é igual a 0
        cont += 1 #contador recebe contador mais um
        soma += c #soma recebe soma mais c
print(f'A soma de todos os \033[32m{cont}\033[m valores solicitados é \033[32m{soma}\033[m.') #print formatado com o resultado
