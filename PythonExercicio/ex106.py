#Faça um mini sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM' o programa será encerrado.
from time import sleep
#DEFININDO A FUNÇÃO
def ajuda(cmd): #define a função ajuda com o parâmetro cmd
    titulo(f'Acessando o manual do comando {cmd}') #chama a função titulo
    help(cmd) #chama a função help com o parâmetro cmd
    sleep(2)


def titulo(txt): #define a função tuitulo com o parâmetro txt
    tam = len(txt) + 4 #tamanho recebe o len de txt mais 4
    print('-' * tam) #print ~ vezes o tamanho
    print(f'  {txt}') #print formatado com o texto
    print('-' * tam) #print ~ vezes o tamanho
    sleep(1)


#PROGRAMA PRINCIPAL
comando = '' #variavel comando recebe vazio
while True: #looping infinito
    titulo('Sistema de Ajuda PyHelp') #chama a função titulo
    comando = str(input('Função ou Biblioteca > ')) #comando recebe o input da função/biblioteca desejada
    if comando.upper() == 'FIM': #se o comando for igual a fim
        break #interrompe o while
    else: #senão
        ajuda(comando) #chama a função ajuda do comando
titulo('ATÉ LOGO!') #despedida
