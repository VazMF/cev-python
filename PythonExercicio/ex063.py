#escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
print('\033[35m-=-=-=-SEQUÊNCIA DE FIBONACCI-=-=-=-\033[m') #titulo
n = int(input('Quantos termos você quer mostrar? ')) #input do número de termos desejado
t1 = 0 #define o primeiro termo como 1 (regra)
t2 = 1 #define o segundo termo como 0 (regra)
print(f'{t1} -> {t2}', end='') #mostra os dois primeiros termos
cont = 3 #contador começa a partir do terceiro termo pois os dois primeiros ja são pré definidos
while cont <= n: #enquanto o contador for menor ou igual o número do input fazer:
    t3 = t1 + t2 #definir t3 pelas somas do t1 e t2 (regra do fibonacci)
    print(f' -> {t3}', end='') #mostra o t3
    t1 = t2 #t1 vai ser alteradp para t2
    t2 = t3 #t2 vai ser alterado para t3 e assim em diante, sempre somando os dois termos para decobrir o próximo
    cont += 1 #contador sobe 1
print(' -> FIM')
