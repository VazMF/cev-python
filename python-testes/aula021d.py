#PARTE PRÁTICA
def farotial(num = 1):
    f = 1
    for cont in range(num, 0, -1):
        f *= cont
    return f


#n = int(input('Digite um número: '))
#print(f'O fatorial de {n} é igual a {farotial(n)}.')
f1 = farotial(5)
f2 = farotial(4)
f3 = farotial()
print(f'Os resultados são {f1}, {f2} e {f3}.')
