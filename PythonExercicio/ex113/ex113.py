def leiaInt(msg):
    '''
    -> lê um valor inteiro
    :param msg: parametro para receber uma string msg
    :return: retorna um valor
    '''
    valor = 0
    while True:
        try:
            n = str(input(msg))  # le um input de uma string
            valor = int(n)#converte a string em um numero inteiro
        except (ValueError, TypeError):
            print('\033[31m[ERRO] Digite valor INTEIRO válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuário interrompeu a execução.')
            return 0
        else:
            return valor


def leiaFloat(txt):
    '''
    -> lê um valor real
    :param txt: parametro para receber uma string
    :return: retorna um valor
    '''
    valor = 0
    while True:
        try:
            n = str(input(txt))
            valor = float(n)
        except (ValueError, TypeError):
            print(f'\033[31m[ERRO] Digite um valor REAL válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuário interrompeu a execução.')
            return 0
        else:
            return valor
