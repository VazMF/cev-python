#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Pyhton, só que fazendo a validação para aceitar apenas um valor númerico.
#DEFININDO A FUNÇÃO
def leiaInt(msg): #define a função leiaInt com o parâmetro msg
    ok = False #variavel ok recebe falso
    valor = 0 #valor recebe zero
    while True: #looping infinito
        n = str(input(msg)) #n recebe o input da string msg
        if n.isnumeric(): #se o n for um valor númerico
            valor = int(n) #valor recebe a conversão inteira de n
            ok = True #ok recebe true
        else: #senao
            print('\033[31m[ERRO]. Digite um número inteiro válido.\033[m') #informe o erro enquanto n não for um numero
        if ok: #se om for true
            break #sai do loop
    return valor #retorna o valor

#PROGRAMA PRINCIPAL
n = leiaInt('Informe um número: ') #n recebe a função leiaInt
print(f'Você acabou de digitar o número {n}.') #print formatado informando o número digitado
