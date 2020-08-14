#crie um programa que leia vários números inteiros pelo teclado. o programa vai parar quando o usuário digitar 999, que é a condição de parada.
#no final, mostre quantos números foram digitados e qual foi a soma entre eles.
cont = soma = 0 #determina soma, contador e numero como 0
print('-' * 50)
n = int(input('Digite um número [999 para parar]: ')) #input do numero
while n != 999: #enquanto o numero for diferente de 999 faça:
    cont += 1 #some mais um ao contador
    soma += n #some o numero a variavel soma
    n = int(input('Digite um número [999 para parar]: ')) #pede outro número
print(f'Foram digitados {cont} números e a soma entre eles é {soma}.') #resultado
print('-' * 50)
