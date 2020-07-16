#crie um programa que simule o funcionamento de um caixa eletrônico. no início pergunte ao usuário qual será o valor a ser sacado (numero inteiro) e o programa vai informar
#quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('=' * 40)
print(f'{"BANCO DO BRASIL":^40}') #titulo
print('=' * 40)
valor = int(input('Informe o valor do saque: R$')) #input do valor a ser sacado
total = valor #total recebe o valor
ced = 50 #cedula recebe 50
totced = 0 #total de cedulas recebe 0
while True: #loop infinito
    if total >= ced: #se o total for maior ou igual a cedulas
        total -= ced #total recebe total menor cedulas
        totced += 1 #total de cedulas recebe mais um
    else: #senao se o total for menor que o a cedula
        if totced > 0: #se total de cedulas for maior que 0
            print(f'Total de cédulas: {totced} de R${ced}') #print o total de cedulas e o valor da cedula
        if ced == 50: #se cedulas for igual a 50
            ced = 20 #cedula recebe 20 e volta pro loop
        elif ced == 20: #senao se cedula for igual a 20
            ced = 10 #cedula recebe 10 e volta pro loop
        elif ced == 10: #se cedula for 10
            ced = 1 #cedula recebe 1 e volta pro loop
        totced = 0 #total de cedula recebe 0
        if total == 0: #se o total for 0
            break #interrompe o while
print('=' * 40) #print de resultado
print('Volte sempre e tenha um BOM DIA!') #mensagem
