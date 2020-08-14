#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. O app deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem.
expr = str(input('Digite uma expressão matemática: ')).strip() #input da expressao a ser analisada
lista = list() #inicializacao de uma lista vazia
for simb in expr: #repeat para cada simbolo em expressao
    if simb == '(': #se o simbolo for um parenteses abrindo
        lista.append('(') #append o parenteses na lista
    elif simb == ')': #senao, se o simbolo for um parenteses fechado
        if len(lista) > 0: #se a lista for maior que zero
            lista.pop() #apaga o ultimo item da lista
        else: #senao
            lista.append(')') #append de um parenteses fechando na lista
            break #interrompe o while
if len(lista) == 0: #se a lista estiver vazia
    print('\033[33mSua expressão é VÁLIDA.\033[m') #print informando que a expressao é valida
else: #senao
    print('\033[31mSua expressão é INVÁLIDA.\033[m') #print informando que a expressao é invalida
