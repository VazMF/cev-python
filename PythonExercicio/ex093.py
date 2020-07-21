#Crie um programa quue gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
#quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
#guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
print('-' * 50)
print(f'{"CADASTRO JOGADOR DE FUTEBOL":^50}') #titulo
print('-' * 50)
jogador = dict() #inicializa um dicionario
partidas = list() #inicializa um lista
jogador['nome'] = str(input('Nome do Jogador: ')) #input do nome do jogador
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? ')) #input do total de partidas jogadas
for c in range(0, tot): #repeticao de 0 ate o valor da variavel total
    partidas.append(int(input(f'Quantos gols {jogador["nome"]} fez na {c+1}° partida? '))) #append do gols de cada partida
jogador['gols'] = partidas[:] #jogador no indice gols recebe uma copia de partidas
jogador['total'] = sum(partidas) #jogador no indice total recebe a soma das partidas
print('-' * 50)
print(jogador) #print o dicionario jogador
print('-' * 50)
for k, v in jogador.items(): #repeticao para cada chave e valor nos itens de jogador
    print(f'{k.upper()}: {v}') #print da chave e valor
print('-' * 50)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.') #print formatado com as informacoes do jogador
for i, v in enumerate(jogador['gols']): #repeticao para cada indice e valor na lista do dicionario gols
    print(f'-> Na {i+1}° partida fez {v} gols.') #print dos gols em cada partida
print(f'Foi um total de {jogador["total"]}.') #print do total de gols do jogador
