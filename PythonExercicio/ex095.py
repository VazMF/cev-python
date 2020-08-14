#Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
#de detalhes do aproveitamento de cada jogador.
print('-' * 50)
print(f'{">>> CADASTRO JOGADOR DE FUTEBOL 2.0 <<<":^50}') #titulo
print('-' * 50)
jogador = dict() #cria um dicionario
partidas = list() #cria uma lista
time = list() #cria outra lista
while True: #looping infinito
    jogador.clear() #limpa o conteudo do dicionario 
    jogador['nome'] = str(input('Nome do Jogador: ')) #input do nome no dicionario
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? ')) #input do total de partidas na variavel tot
    partidas.clear() #limpa o conteudo da lista partidas
    for c in range(0, tot): #repeticao de 0 ate o total de partidas
        partidas.append(int(input(f'Quantos gols {jogador["nome"]} fez na {c+1}° partida? '))) #input dos gols em cada partida na lista partida
    jogador['gols'] = partidas[:] #dicionario no indice gols vai receber uma copia da lista de partidas
    jogador['total'] = sum(partidas) #dicionario no indice total recebe a soma de todos os gols
    time.append(jogador.copy()) #lista time recebe um append da copia do dicionario jogador
    while True: #looping infinito
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0] #input para ver se o user quer cadastrar mais jogadores
        print('-' * 50)
        if resp in 'SN': #se a resposta for S ou N
            break #interrompe o if
        print('\033[31mERRO! Digite apenas S ou N.\033[m') #senao, print do erro e o while se repete
    if resp == 'N': #se a resposta for nao
        break #interrompe o while
print('cod ', end='') #print para o cabecahlo de levantamento do jogador
for i in jogador.keys(): #repeticao para cada indice nas chaves do dicionario jogador
    print(f'{i:<15} ', end='') #print formatado do nome da chave 
print() #print de quebra de linha
print('-' * 50)
for k, v in enumerate(time): #repeticao para cada chave a valores na lista de times enumerada
    print(f'{k:>3} ', end='') #print formatado das chaves
    for d in v.values(): #repeticao para cada dado em valores
        print(f'{str(d):<16}', end='') #print formatado com o valor
    print() #print para quebrar a linha
print('-' * 50)
while True: #looping infinito
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] ')) #input do cod do jogador para mostrar dados
    if busca == 999: #se o valor de busca for 999
        break #interrompe o while e finaliza o programa
    if busca >= len(time): #se busca for maior ou igual ao tamanho da lista de times
        print(f'\033[31mERRO! Não existe jogador com o código {busca}.\033[m') #print erro pq o codigo é invalido
    else: #senao
        print('-' * 50)
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:') #print com o levantamento do jogador com o cod inserido
        for i, g in enumerate(time[busca]['gols']): #repeticao para cada partida do jogador
            print(f' - No {i+1}° jogo fez {g} gols.') #print formatado com cada gol por partida
    print('-' * 50)
print('<< VOLTE SEMPRE! >>')
