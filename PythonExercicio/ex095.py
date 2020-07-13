#Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
#de detalhes do aproveitamento de cada jogador.
print('-' * 50)
print(f'{"CADASTRO JOGADOR DE FUTEBOL 2.0":^50}')
print('-' * 50)
jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols {jogador["nome"]} fez na {c+1}° partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 50)
        if resp in 'SN':
            break
        print('\033[31mERRO! Digite apenas S ou N.\033[m')
    if resp == 'N':
        break
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<16}', end='')
    print()
print('-' * 50)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'\033[31mERRO! Não existe jogador com o código {busca}.\033[m')
    else:
        print('-' * 50)
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f' - No {i+1}° jogo fez {g} gols.')
    print('-' * 50)
print('<< VOLTE SEMPRE! >>')
