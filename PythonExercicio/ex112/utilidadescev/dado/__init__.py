def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == "":
            print(f'\033[31mERRO: \"{entrada}\" é um preço inválido.\033[m')
        else:
            valido = True
            return float(entrada)


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