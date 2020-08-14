#Crie um programa que tenha uma tupla totalmente preenchida com uma contagm por extenso, de zero até vinte. Seu programa vai ler um número pelo teclado e mostrar por extenso
print('=' * 30)
print(f'{"NÚMEROS POR EXTENSO":^30}') #titulo
print('=' * 30)
contagem = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'catorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte' ) #tupla com numeros de 0 1 20 por extenso
num = int(input('Digite um número de 0 a 20: ')) #input do numero
while num < 0 or num > 20: #enquanto numero for menor que 0 ou maior que 20
    num = int(input('ERRO. Digite um número de 0 a 20: ')) #mostra o erro e pede o input
print(f'Você digitou o número {(contagem[num].upper())}.') #print formatado com o numero na tupla de acordo com o indice
print('=' * 30)
