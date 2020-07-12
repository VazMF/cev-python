#Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
#dicionário se por acaso a CTPS for diferente de zero, o dicionário tembém receberá o ano de contratação e 
#o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa irá se aposentar. 35 anos de contribuicao
from datetime import date
ano = date.today().year
print('-' * 45)
print(f'{"CADASTRO DE TRABALHADOR":^45}')
print(f'-' * 45)
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - nasc
dados['ctps'] = int(input('Carteira de trabalho [0 se não tem]: '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - date.today().year)
print('-' * 45)
for k, v in dados.items():
    print(f'-> {k.upper()}: {v}')
print('-' * 45)
