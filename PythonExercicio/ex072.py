#Crie um programa que tenha uma tupla totalmente preenchida com uma contagm por extenso, de zero até vinte. Seu programa vai ler um número pelo teclado e mostrar por extenso
print('=' * 30)
print('{:^30}'.format('NÚMEROS POR EXTENSO'))
print('=' * 30)
contagem = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'catorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte' )
num = int(input('Digite um número de 0 a 20: '))
while num < 0 or num > 20:
    num = int(input('Tente novamente. Digite um número de 0 a 20: '))
print(f'Você digitou o número {(contagem[num])}.')
