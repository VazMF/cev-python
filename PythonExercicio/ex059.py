#crie um programa que leia dois valores e mostre na tela um menu: 1 = somar, 2 = multiplicar, 3 = maior, 4 = novos números, 5 = sair do programa
# eu programa deverá realizar a operação solicitada em cada caso.
from time import sleep #import do sleep
print('\033[35m=-=\033[m' * 10)
n1 = int(input('Primeiro valor: ')) #lê o primeiro valor
n2 = int(input('Segundo valor: ')) #lê o segundo valor
opcao = 0 #determina a opção como 0
while opcao != 5: #determina que enquanto a opção for diferente de 5 o while vai acontecer
    print('''\033[35m[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MOSTRAR O MAIOR
[ 4 ] DIGITAR NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA\033[m''') #menu de opções para os números
    opcao = int(input('Qual é a sua opção? ')) #pergunta qual opção quer executar
    if opcao == 1: #se a oapção escolhida for 1
        soma = n1 + n2 #vai somar n1 com n2
        print(f'A soma entre {n1} + {n2} é {soma}.') #mostra o resultado
    elif opcao == 2: #se a opção for 2
        multi = n1 * n2 #multiplica n1 com n2
        print(f'O resultado da multiplicação de {n1} x {n2} é {multi}.') #mostra o resultado da multiplicação
    elif opcao == 3: #se a opção for 3
        if n1 > n2: #se n1 for maior que n2
            maior = n1 #o maior será n1
            print(f'Entre {n1} e {n2} o maior valor é {maior}.')  #mostra o resultado
        elif n2 > n1: #se o maior for n2
            maior = n2 #a variavél maior será alterado para n2
            print(f'Entre {n1} e {n2} o maior valor é {maior}.')  # mostra o resultado
        else: #senao
            print('Os dois números são iguais.')
    elif opcao == 4: #se a opção escolhida for 4
        print('Infome os números novamente: ') #pede para digitar os valores novamente
        n1 = int(input('Primeiro valor: ')) #primeiro valor
        n2 = int(input('Segundo valor: ')) #segundo valor
    elif opcao == 5: #se a opção escolhida for 5
        print('Finalizando...') #finaliza o programa fechando o while
    else: #se o número digitado na opção não for nenhum dos definidos
        print('Opção inválida. Tente novamente.') #erro
    print('\033[35m=-=\033[m' * 10)
    sleep(1) #sleep para o programa dormir antes do while acontecer novamente
print('Fim do programa, volte sempre!') #mensagem de fim
