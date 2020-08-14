#Faça um programa que tenha uma função voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se a pessoa tem voto negado, opcional ou obrigatório nas eleições.
#DEFININDO A FUNÇÃO
def voto(nasc): #define a função voto com o parâmetro nascimento
    from datetime import date #import local do date para pegar o ano atual
    idade = date.today().year - nasc #variavel idade recebe o ano atual menos o ano informado pelor user
    print(f'Com {idade} anos: ', end='') #print informando a idade da pessoa, sem quebra de linha
    if idade < 16: #se a idade for menor que 16 anos
        return f'NÃO VOTA.' #retorna a string informando que o indivíduo não pode votar
    elif 16 <= idade < 18 or idade > 65: #senão se a idade for maior que 16 e menor que 18, ou maior de 65
        return f'VOTO OPCIONAL.' #retorna a string informando que o voto é opcional
    else: #senão
        return f'VOTO OBRIGATÓRIO.' #retorna a string informando que o voto é obrigatório

#PROGRAMA PRINCIPAL
print('-' * 30) #print de resultado
ano = int(input('Em que ano você nasceu? ')) #input do ano de nascimento do usuário na variavel ano
print(voto(ano)) #print da função voto com o parâmetro ano
print('-' * 30) #print de resultado
