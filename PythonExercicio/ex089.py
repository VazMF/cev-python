#crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim
#contento a media de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
print('-' * 60)
print(f'{"> BOLETIM ESCOLAR <clea":^60}') #titulo
print('-' * 60)
ficha = list() #incializa uma lista vazia
while True: #looping infinito
    nome = str(input('Nome: ')) #input do nome
    nota1 = float(input('Nota 1: ')) #input da primeria nota
    nota2 = float(input('Nota 2: ')) #input da segunda nota
    media = (nota1 + nota2) / 2 #media recebe a soma as duas notas dividida por dois
    ficha.append([nome, [nota1, nota2], media]) #append dos dados lidos para a ficha (notas em 'sublista')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0] #input da resposta
    print('-' * 60) #print para resultado
    while resp not in 'SN': #enquanto a resposta nao for S ou N
        print('\033[31m!ERRO! DIGITE SIM OU NÃO.\033[m') #print erro
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0] #input da resposta novamente
        print('-' * 60) #print de resultado
    if resp == 'N': #se a resposta for nao
        break #interrompe o while
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}') #print do cabecalho do boletim
for i, a in enumerate(ficha): #para cada indice e aluno na lista enumerada ficha
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}') #print formatado do indice, nome do aluno e media
while True: #looping infinito
    print('-' * 60) #print para resultado
    opc = int(input('Quer mostrar as notas de qual aluno? [999 para parar]: ')) #input do numero do aluno
    print('-' * 60)
    if opc == 999: #se a opcao for 999
        break #interrompe o while
    elif opc <= len(ficha) -1: 
        print(f'As notas de {ficha[opc][0]} são: {ficha[opc][1]}')
