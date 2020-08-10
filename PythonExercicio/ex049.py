#refaça o desafio 009, motrando a tabuada de um número que o usuário escolher só que agora utilizando um laço for.
print('\033[34m-\033[m' * 40)
num = int(input('Digite um número para ver sua tabuada: ')) #input do numero na variavel num
for c in range(1, 11): #repita de 1 ate 10
    print(f'{num} \033[34mx\033[m {c:2} \033[34m=\033[m {num*c}') #print formatado
print('\033[34m-\033[m' * 40)
