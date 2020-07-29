#Faça um mini sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM' o programa será encerrado. OBS: Use cores.
from time import sleep
#DEFININDO A FUNÇÃO
def ajuda(cmd):
    titulo(f'Acessando o manual do comando {cmd}')
    help(cmd)
    sleep(2)


def titulo(txt, cor=0):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)
    sleep(1)


#PROGRAMA PRINCIPAL
comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!')
