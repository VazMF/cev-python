#Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
#dicionário se por acaso a CTPS for diferente de zero, o dicionário tembém receberá o ano de contratação e 
#o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa irá se aposentar. 35 anos de contribuicao
from datetime import date
ano = date.today().year
print('-' * 45)
print(f'{"CADASTRO DE TRABALHADOR":^45}') #titulo
print(f'-' * 45)
dados = dict() #inicializacao de um dicionario dados
dados['nome'] = str(input('Nome: ')) #input do nome
nasc = int(input('Ano de nascimento: ')) #input do ano de nascimento
dados['idade'] = date.today().year - nasc #calculo da idade
dados['ctps'] = int(input('Carteira de trabalho [0 se não tem]: ')) #input da ctps
if dados['ctps'] != 0: #se a ctps for diferente de 0
    dados['contratação'] = int(input('Ano de contratação: ')) #input do ano de contratacao
    dados['salário'] = float(input('Salário: R$')) #input do salario
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - date.today().year) #calculo da idade da aposentadoria
print('-' * 45) #print de resultado
for k, v in dados.items(): #repeticao para cada chave e valor nos itens de dados
    print(f'-> {k.upper()}: {v}') #print das informacoes
print('-' * 45)
