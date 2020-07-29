#INTERACTIVE HELP E DOCSTRING
def contador(i, f, p):
    """ #DOCSTRING
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = 1
    while c <= f:
        print(f'{c} -> ', end='')
        c += p
    print('FIM!')


contador(0, 100, 10)
help(contador)
help(print) #INTERACTIVE HELP

