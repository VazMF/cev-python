#crie um programa que leia vários números inteiros pelo teclado. o programa só vai parar quando o usuário didgitar 999, que é a condição de parada. no final, mostre quantos números
#foram digitados e qual foi a soma entre eles (desconsiderando o flag)
cont = soma = 0 #inicializacao das variaveis contador e soma como 0
while True: #loop infinito
    n = int(input('Digite um número [999 para parar]: ')) #input do numero
    if n == 999: #se o valor de n for 999
        break #interrompe e sai do while
    #senao
    cont += 1 #contador soma mais um
    soma += n #soma recebe soma mais n
print(f'A soma dos {cont} valores foi {soma}!') #resultado
