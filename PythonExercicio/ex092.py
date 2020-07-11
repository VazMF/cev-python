#Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
#dicionário se por acaso a CTPS for diferente de zero, o dicionário tembém receberá o ano de contratação e 
#o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa irá se aposentar. 35 anos de contribuicao
from datetime import date
ano = date.today().year
print('-' * 40)
print(f'{"CADASTRO DE TRABALHADOR":^40}')
print(f'-' * 40)
dic = dict()
dic['nome'] = str(input('Nome: '))
dic['nasc'] = int(input('Ano de nascimento: '))
dic['ctps'] = int(input('Carteira de Trabalho (0 se não tem): '))
dic['idade'] = ano - dic['nasc']
if dic['ctps'] != 0:
    dic['ano_contr'] = int(input('Ano de contratação: '))
    dic['salario'] = float(input('Salário: R$'))
    dic['apos'] = (dic['ano_contr'] + 35) - dic['nasc']
print('-' * 40)
for k, v in dic.items():
    print(f'{k.upper()}: {v}')
print('-' * 40)
