#faça um programa que motre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. o programa será interrompido quando o número solicitado for negativo
print('\033[34m------------TABUADA 3.0------------\033[m') #titulo
while True: #loop infinito
    num = int(input('Quer ver a tabuada de qual valor? ')) #input do numero
    print('-' * 35) #print para o resultado
    if num < 0: #se o numero for menor que 0
        break #interrompe o loop
    for c in range(1, 11): #repeticao de 1 ate 11 para mostrar a tabuada
        print(f'{c} x {num} = {num * c}') #print formatado como tabuada
    print('-' * 35) #print para o resultado
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!') #mensagem de encerramento
