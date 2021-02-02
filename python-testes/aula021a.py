#ARGUMENTOS OPCIONAIS
def somar(a = 0, b = 0, c = 0): #INICIALIZA COM ZERO PARA SER OPCIONAL
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(3, 2)
somar()
somar(3, 4, 5)
 