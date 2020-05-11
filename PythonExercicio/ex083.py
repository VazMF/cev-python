#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. O app deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem.
expr = str(input('Digite a expressão: ')).strip()
lista = list()
for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('\033[33mSua expressão é VÁLIDA.\033[m')
else:
    print('\033[31mSua expressão é INVÁLIDA.\033[m')
