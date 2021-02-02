#RETURN
def somar(a = 0, b = 0, c = 0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    """
    s = a + b + c
    return s #retorna o valor de s para fazer um print mais personalizado


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')
