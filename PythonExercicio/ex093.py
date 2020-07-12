#Crie um programa quue gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
#quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
#guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
print('-' * 50)
print(f'{"CADASTRO JOGADOR DE FUTEBOL":^50}')
print('-' * 50)
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols {jogador["nome"]} fez na {c+1}° partida? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-' * 50)
print(jogador)
print('-' * 50)
for k, v in jogador.items():
    print(f'{k.upper()}: {v}')
print('-' * 50)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'-> Na {i+1}° partida fez {v} gols.')
print(f'Foi um total de {jogador["total"]}.')
