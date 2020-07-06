#faça um programa que leia o sexo de uma pessoa, mas só aceita os valores M ou F. Caso esteja errado, peça a digitaçãp novamente até ter um valor correto
print('\033[31m===VALIDAÇÃO DE DADOS===\033[m')
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('\033[31mDados inválidos.\033[m Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo \033[33m{}\033[m registrado com sucesso!'.format(sexo))
print('\033[31m=\033[m' * 25)
