def dobrar(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2 #funciona como o +=
        pos += 1


valores = [1, 7, 5, 0, 4]
print(valores)
dobrar(valores)
print(valores)
