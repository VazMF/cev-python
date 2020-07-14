#faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: se ele ainda vai se alistar no serviço militar; se é hpra de se alistar; passou o tempo. seu programa também deverá mostrar o tempo que ou que passou do prazo
from datetime import date #importa a data atual do computador
print('\033[33m---ALISTAMENTO MILITAR---\033[m') #titúlo
nasc = int(input('Ano de nascimento: ')) #input do ano de nascimento na varivel nasc
atual = date.today().year #variavel atual recebe o ano atual do computador
idade = atual - nasc #cálculo da idade
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}') #print mostrando a idade 
if idade < 18: #se a idade for menor que 18
    saldo = 18 - idade #saldo recebe idade
    print(f'Ainda faltam {saldo} anos para seu alistamento.') #print mostrando os anos que faltam para a pessoa se alistar
    ano = atual + saldo #ano recebe o ano atual mais o saldo para o calculo do ano de alistamento
    print(f'Seu alistamento será em {ano}') #print do ano de alistamento
elif idade == 18: #se a idade for 18
    print('Você tem que se alistar \033[31mIMEDIATAMENTE\033[m') #print mostrando que a pessoa deve se aistar o mais rapido possivel
elif idade > 18: #se a idade for maior que 18
    saldo = idade - 18 #saldo recebe a idade menor 18
    print(f'Você já deveria ter se alistado há {saldo} anos.') #print mostrando quando a pessoa deveria ter se alistado
    ano = atual - saldo #ano recebe o ano atual menos saldo
    print(f'Seu alistamento foi em {ano}') #print mostrando o ano de alistamento da pessoa
