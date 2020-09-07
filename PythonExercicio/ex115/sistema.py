from PythonExercicio.ex115.lib.interface import *
from PythonExercicio.ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas', 'Sair do sistema'])
    if resposta == 1:
        #opcao para listas o conteudo de um arquivo txt
        lerArquivo(arq)
    elif resposta == 2:
        #opcao para cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Programa encerrado. Volte sempre ;)')
        break
    else:
        print('\033[31m[ERRO] Por favor digite uma opção válida.\033[m')
    sleep(1.5)
