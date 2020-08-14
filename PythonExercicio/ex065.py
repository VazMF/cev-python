#crie um programa que leia vários números inteiros pelo teclado. no final mostre a média entre todos e qual foi o maior e o menor. o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
print('\033[35m-=-=-MEDIA, MAIOR E MENOR-=-=-\033[m') #titulo
resp = 'S' #define a resposta como sim
media = soma = quant = maior = menor = 0 #determina a media, soma, quantidade, maior e menor como 0
while resp in 'Ss': #enquanto a resposta estiver em sim faça:
    n = int(input('Digite um número: ')) #input do número
    soma += n #soma a variavel soma com o valor de n
    quant += 1 #soma um a quantidade
    if quant == 1: #se quantidade é igual a um
        maior = menor = n #maior e menor recebem n
    else: #senao
        if n > maior: #testa se n é maior
            maior = n #se sim, maior vira n
        if n < menor: #testa se n é menor
            menor = n #se sim, menor vira n
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0] #pergunta se o usuario quer continuar a digitar
media = soma / quant #calculo da media pela soma dos valores dividido pela quantidade de valores
print(f'Você digitou {quant} números e a média foi {media}') #resposta
print(f'O maior valor foi {maior} e o menor foi {menor}') #resposta
