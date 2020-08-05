#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: até 9 anos = mirim; até 14 anos = infantil; até 19 anos = junior; até 20 anos = sênior; acima = master.
from datetime import date
print('\033[36m---CONFEDERAÇÃO NACIONAL DE NATAÇÃO---\033[m') #titulo
ano = int(input('Digite o ano em que você nasceu: ')) #input do ano de nascimento
atual = date.today().year #import do ano atual do computador na variavel atual
idade = atual - ano #cálculo da idade
print(f'O atleta tem {idade} anos.') #print da idade do atleta
if idade <= 9: #se a idade for menor ou igual a 9
    print('CLASSIFICAÇÃO: \033[36mMIRIM\033[m.') #print mirim
elif idade <= 14: #se a idade for menor ou igual a 14
    print('CLASSIFICAÇÃO: \033[36mINFANTIL\033[m') #print infantil
elif idade <= 19: #se a idade for menor ou igual a 19
    print('CLASSIFICAÇÃO: \033[36mJUNIOR\033[m') #print junior
elif idade <= 25: #se a idade for menor ou igual a 25
    print('CLASSIFICAÇÃO: \033[36mSÊNIOR\033[m') #print sênior
else: #caso nenhuma das alternativas acima forem viaveis
    print('CLASSIFICAÇÃO: \033[36mMASTER\033[m') #print categoria master
