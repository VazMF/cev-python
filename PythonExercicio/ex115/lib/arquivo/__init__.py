from PythonExercicio.ex115.lib.interface import *

def arqExiste(nome):
    '''
    -> funcao para verificar se um arquivo existe
    :param nome: nome do arquivo
    :return: retorna verdadeiro ou falso
    '''
    try:
        a = open(nome, 'rt') #tenta abrir um arquivo para leitua e texto, por isso rt
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    '''
    -> funcao que cria um arquivo
    :param nome: nome do arquivo a ser criado
    :return: retorna se o arquivo foi criado ou nao
    '''
    try:
        a = open(nome, 'wt') #tenta abrir o arquivo para escrita e texto, por isso wt
        a.close()
    except:
        print('Ocorreu um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    '''
    -> funcao para ler um arquivo
    :param nome: nome do arquivo
    :return: retorna as pessoas cadastradas no arquivo
    '''
    try:
        a = open(nome, 'rt') #tenta abrir um arquivo para leitura
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30}{dados[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='<descinhecido>', idade=0):
    try:
        a = open(arq, 'at+')
    except:
        print('Ocorreu um erro na hora de abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
            a.close()
