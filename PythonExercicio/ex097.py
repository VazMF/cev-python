#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma msg com tamanho adaptavel
def escreva(txt):
    print('~' * len(txt))


msg = '  Python melhor linguagem  '
escreva(msg)
print(msg)
escreva(msg)
