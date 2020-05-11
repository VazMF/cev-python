#faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: se ele ainda vai se alistar no serviço militar; se é hpra de se alistar; passou o tempo
#seu programa também deverá mostrar o tempo que ou que passou do prazo
from datetime import date #importa a data atual do computador
print('\033[31m---ALISTAMENTO MILITAR---\033[m') #titúlo
nasc = int(input('Ano de nascimento: ')) #input do ano de nascimento
atual = date.today().year #import da data
idade = atual - nasc #cálculo da idade
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade < 18: #se a idade for menor que 18
    saldo = 18 - idade
    print('Ainda faltam {} anos para seu alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade == 18: #se a idade for 18
    print('Você tem que se alistar \033[31mIMEDIATAMENTE\033[m')
elif idade > 18: #caso nenhuma das afirmações acima seja veradeira
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
print('\033[31m-\033[m' * 25) #fim
