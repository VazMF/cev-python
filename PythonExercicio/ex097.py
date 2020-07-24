#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma msg com tamanho adaptavel
#DEFININDO A FUNÇÃO
def escreva(txt): #função com parametro para texto
    tam = len(txt) + 4 #variavel tamanho recebe o tamanho do txt + 4
    print('~' * tam) #print um ~ para cada caractere do texto
    print(f'  {txt}') #print formatado do texto com espaços para centralizar
    print('~' * tam) #print um ~ para cada caractere do texto


#programa principal
escreva('Fuck this love calling my name, get out of my veins') #usando a função escreva 
escreva('No reasons to stay, is a good reason to go')
escreva('No crying in the club')
escreva('Cry for me')
