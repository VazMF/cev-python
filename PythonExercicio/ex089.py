#crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim
#contento a media de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
print('-' * 60)
print('{:^60}'.format('BOLETIM ESCOLAR'))
print('-' * 60)
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-' * 60)
    
    while resp not in 'SN':
        print('\033[31m!ERRO! DIGITE SIM OU NÃO.\033[m')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 60)
    if resp == 'N':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
    print('-' * 60)
    opc = int(input('Quer mostrar as notas de qual aluno? [999 para parar]: '))
    print('-' * 60)
    if opc == 999:
        break
    elif opc <= len(ficha) -1:
        print(f'As notas de {ficha[opc][0]} são: {ficha[opc][1]}')
