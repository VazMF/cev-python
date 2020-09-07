def leiaInt(msg):
    '''
    -> lê um valor inteiro
    :param msg: parametro para receber uma string msg
    :return: retorna um valor
    '''
    valor = 0
    while True:
        try:
            n = str(input(msg))  #le um input de uma string
            valor = int(n) #converte a string em um numero inteiro
        except (ValueError, TypeError):
            print('\033[31m[ERRO] Digite valor INTEIRO válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuário interrompeu a execução.')
            return 0
        else:
            return valor


def linha(tam=42):
    '''
    -> função para fazer a linha visual do ex
    :param tam: recebe o tamanho da linha (padrao 42)
    :return: retorna varios - formando uma linha
    '''
    return '-' * tam


def cabecalho(txt):
    '''
    -> função que faz um cabeçalho
    :param txt: parametro que recebe o texto do cabecalho
    :return: print duas linhas da função linha e o texto no meio
    '''
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    '''
    -> função que cria um menu para o usuario
    :param lista: parametro que recebe as opcoes do menu
    :return: retorna a opcao escolhida pelo usuario
    '''
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('O que deseja fazer? ')
    return opc
