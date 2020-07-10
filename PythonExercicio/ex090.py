#Faça um programa que leia o nome e média de um aluno, guardando também a siatuação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela. > 7 aprovado
print('-' * 35)
print(f'{"APROVADO OU REPROVADO":^35}')
print('-' * 35)
nome = str(input('Nome do aluno(a): '))
media = float(input(f'Média de {nome}: '))
s = {'situacao': '\033[32mAPROVADO(A)\033[m'}
if media < 7:
    s['situacao'] = '\033[31mREPROVADO(A)\033[m'
print('-' * 35)
print(f'Nome: {nome}')
print(f'Média: {media}')
print(f'Situação: {s["situacao"]}')
print('-' * 35)
