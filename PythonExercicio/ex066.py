#crie um programa que leia vários números inteiros pelo teclado. o programa só vai parar quand o usuário didgitar 999, que é a condição de parada. no final, mostre quantos números
#foram digitados e qual foi a soma entre eles (desconsiderando o flag)
cont = soma = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} valores foi {soma}!')
