#Crie um programa que tenha uma função fatorial(), que receba dois parâmetros: o número a calcular e o outro chamado show, que será um valor lógico (opcinal), indicando se será mostrado na tela ou não o prcesso de cálculo do fatorial.
#DEFININDO A FUNÇÃO
def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um numero.
    :param num: o número a ser calculado.
    :param show: (opcional) mostrar o calculo
    :return: retorna o resultado do fatorial de um numero n.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#PROGRAMA PRINCPAL
print(fatorial(5, False))
help(fatorial)
