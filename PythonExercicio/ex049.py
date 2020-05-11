#refaça o desafio 009, motrando a tabuada de um número que o usuário escolher só que agora utilizando um laço for.
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} \033[34mx\033[m {:2} \033[34m=\033[m {}'.format(num, c, num*c))
