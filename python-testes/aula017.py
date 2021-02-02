num =[2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse = True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não posso remover algo que não existe.')
print(num)
print(f'essa lisa tem {len(num)} valores')
