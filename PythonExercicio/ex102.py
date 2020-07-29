#Crie um programa que tenha uma função fatorial(), que receba dois parâmetros: o número a calcular e o outro chamado show, que será um valor lógico (opcinal), indicando se será mostrado na tela ou não o prcesso de cálculo do fatorial.
#DEFININDO A FUNÇÃO
def fatorial(num, show=False): #define a função fatorial com os parâmetros num e show (padrao false)
    #DOCSTRING
    """
    -> Calcula o Fatorial de um numero.
    :param num: o número a ser calculado.
    :param show: (opcional) mostrar o calculo
    :return: retorna o resultado do fatorial de um numero n.
    """
    f = 1 #variavel fatorial recebe 1
    for c in range(num, 0, -1): #repetição de num ate 0 subtraindo 1
        if show: #se show for true
            print(c, end='') #printa o contador sem quebrar a linha
            if c > 1: #se c for maior que um
                print(' x ', end='') #print um x para indicar multiplicação
            else: #senao
                print(' = ', end='') #print = para o resultado final
        f = f * c #fatorial recebe fatorial multiplicado pelo c
    return f

#PROGRAMA PRINCPAL
print(fatorial(5, True)) #print da função fatorial passando o parâmetro num como 5 e o parâmetro show (opcional) como false
help(fatorial) #função help para exibir a docstring da função criada
