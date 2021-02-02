#ESCOPO DE VARIAVEL
def funcao():
    #global n1 quando quiser utilizar a global e nao criar outro n1
    n1 = 4 #variavel local, só funciona dentro da função
    print(f'N1 dentro vale {n1}')


n1 = 2 #variaveç global, funciona tanto na local quanto global
funcao()
print(f'N1 fora vale {n1}')
