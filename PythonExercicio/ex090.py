#Faça um programa que leia o nome e média de um aluno, guardando também a siatuação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela. > 7 aprovado
print('-' * 35)
print(f'{"APROVADO OU REPROVADO":^35}')
print('-' * 35)
aluno = dict()
aluno['nome'] = str(input('Nome do aluno(a): '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = '\033[32mAPROVADO(A)\033[m'
elif 5<= aluno['media'] < 7:
    aluno['situacao'] = '\033[33mRECUPERAÇÃO\033[m'
else:
    aluno['situacao'] = '\033[31mREPOVADO(A)\033[m'
print('-' * 35)
for k, v in aluno.items():
    print(f'{k}: {v}')
print('-' * 35)
