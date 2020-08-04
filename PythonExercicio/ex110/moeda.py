def aumentar(preco=0, taxa=0, forma=False):
    """
    -> Aumenta um preco de acordo com uma taxa
    :param preco: o valor a ser aumentado
    :param taxa: o valor da porcentagem do aumento
    :param forma: parametro opcional de formatacao
    :return: retorna o preco apos o aumento (formatado ou nao)
    """
    res = preco + (preco * taxa/100)
    return res if forma is False else moeda(res)


def diminuir(preco=0, taxa=0, forma=False):
    """
    -> Diminui o preco de acordo com uma taxa
    :param preco: o valor a ser aumentado
    :param taxa: o valor da porcentagem do aumento
    :param forma: parametro opcional de formatacao
    :return: retorna o preco apos o desconto (formatado ou nao)
    """
    res = preco - (preco * taxa/100)
    return res if forma is False else moeda(res)


def dobro(preco=0, forma=False):
    """
    -> Dobra o valor de um preco
    :param preco: preco a ser dobrado
    :param forma: parametro opcional de formatacao
    :return: retorna o preco dobrado (formatado ou nao)
    """
    res = preco * 2
    return res if forma is False else moeda(res)


def metade(preco=0, forma=False):
    """
    -> Divide um preco pela metade
    :param preco: o valor a ser divido
    :param forma: parametro opcional de formatcao
    :return: retorna a metade do preco (formatado ou nao)
    """
    res = preco / 2
    return res if forma is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    """
    -> Formata um preco com o padrao real brasileiro
    :param preco: o valor a ser formatado
    :param moeda: a sigla da moeda
    :return: retorna uma string formatada de acordo com o padrao monetario do Brasil
    """
    return f'{moeda}{preco:.2f}'.replace('.', ',')

