#faça um programa que leia o sexo de uma pessoa, mas só aceita os valores M ou F. Caso esteja errado, peça a digitaçãp novamente até ter um valor correto
print('\033[31m===VALIDAÇÃO DE DADOS===\033[m') #titulo
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0] #input do sexo desconsidernado espacos jogando para masiculas e pegando somente a primeira letra
while sexo not in 'MF': #loop caso o sexo nao seja masculino ou feminino
    sexo = str(input('\033[31mDados inválidos.\033[m Por favor informe seu sexo: ')).strip().upper()[0] #pede o sexo novamente
print(f'Sexo \033[33m{sexo}\033[m registrado com sucesso!') #pirnt formatado com o sexo inserido
