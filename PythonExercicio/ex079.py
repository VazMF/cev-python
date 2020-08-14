#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os e uma lista. Caso o número já exista, não será adicionado. Exibir os valores em ordem crescente.
print('-' * 40)
print(f'{"- ORDENADOR CRESCENTE -":^40}') #titulo
print('-' * 40)
lista = list() #inicializacao de uma lista vazia
while True: #loop infinito
    resp = ' ' #variavel recebe vazio
    while True: #loop infinito
        num = (int(input('Digite um valor: '))) #input do numero na variavel num
        if num not in lista: #se o numero nao estiver na lista
            lista.append(num) #lista append o numero
            print('\033[33mValor adicionado.\033[m') #print informando que o valor for adicionado
            print('-' * 40) #print para o resultado
            break #interrompe o while
        else: #senao, se o numero estiver na lista
            print('\033[31mErro. Não posso duplicar valores.\033[m') #print informando o que nao é possível duplicar valores
            print('-' * 40) #print para resultado
    while resp not in 'sn': #enquanto a resposta nao for s ou n
        resp = str(input('Deseja continuar digitando? [s/n] ')).strip().lower()[0] #pede o input da resposta
        print('-' * 40) #print para resultado
    if resp == 'n': #se a respota for n
        break #interrompe o while
print(f'Os valores informados foram {sorted(lista)}') #print formatado com todos os valores da lista em ordem crescente
print('-' * 40)
