#PARTE PRÁTICA
def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print(f'O número {num} É PAR!')
else:
    print(f'O número {num} NÃO É PAR!')
    