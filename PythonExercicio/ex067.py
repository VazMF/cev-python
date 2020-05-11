#faça um programa que motre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. o programa será interrompido quando o número solicitado for nagtivo
print('\033[34m-=-TABUADA 3.0-=-\033[m')
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('\033[34m-\033[m' * 30)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {num} = {num * c}')
    print('\033[34m-\033[m' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
