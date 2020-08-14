#Faça um programa que leia o nome e média de um aluno, guardando também a siatuação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela. > 7 aprovado
print('-' * 35)
print(f'{"< APROVADO OU REPROVADO >":^35}') #titulo
print('-' * 35)
aluno = dict() #inicializa um dicionario de alunos
aluno['nome'] = str(input('Nome do aluno(a): ')) #input do nome do aluno 
aluno['media'] = float(input(f'Média de {aluno["nome"]}: ')) #input da media do aluno
if aluno['media'] >= 7: #se a media do aluno for maior ou igual a 7
    aluno['situacao'] = '\033[32mAPROVADO(A)\033[m' #a situacao recebe aprovado
elif 5 <= aluno['media'] < 7: #senao se a media do aluno for menor ou igual a 5 e menor que 7
    aluno['situacao'] = '\033[33mRECUPERAÇÃO\033[m' #a situacao é recuperacao
else: #senao 
    aluno['situacao'] = '\033[31mREPOVADO(A)\033[m' #a situacao é reprovado
print('-' * 35)
for k, v in aluno.items(): #repeticao para cada chave a valor nos itens de aluno
    print(f'{k}: {v}') #print formatado da chave a valor
print('-' * 35)
