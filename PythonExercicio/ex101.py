#Faça um programa que tenha uma função voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se a pessoa tem voto negado, opcional ou obrigatório nas eleições.
#DEFININDO A FUNÇÃO
def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return f'NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'VOTO OPCIONAL.'
    else:
        return f'VOTO OBRIGATÓRIO.'

#PROGRAMA PRINCIPAL
print('_' * 30)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
