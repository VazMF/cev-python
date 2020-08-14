#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador mesmo que algum dado não tenha sido informado corretamente.
#DEFININDO A FUNÇÃO
def ficha(nome = '<desconhecido>', gols = 0): #define a função ficha com parâmetro nome recebendeo desconhecido e gols recebendo zero
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato') #print informando o nome do jogador e a quantidade de gols


#PRINCIPAL
print('-' * 45)
n = str(input('Nome do Jogador: ')) #input do nome do jogador na variavel n
g = str(input('Quantidade de gols: ')) #input da quantidade de gols como string na variavel g para poder deixa vazio caso necessário
if g.isnumeric(): #se a variavel g for um numero
    g = int(g) #g é convertido para inteiro
else: #senao
    g = 0 #g recebe zero
if n.strip() == '': #se removendo o espaço de n ele é vázio
    ficha(gols=g) #chama a função ficha somente com o parâmetro gols
else: #senão
    ficha(n, g) #chama a função completa
print('-' * 45)
