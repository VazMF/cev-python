#Crie um programa quue gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
#quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
#guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
print('-' * 45)
print(f'{"CADASTRO JOGADOR DE FUTEBOL":^45}')
print('-' * 45)
dic = dict()
gols = 0
dic['nome'] = str(input('Nome do jogador: '))
dic['partidas'] = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
for c in range(0, dic['part']):
    dic['qtd_gols'] = int(input(f'Quantos gols {dic["nome"]} fez na {c+1}° partida? '))
    gols += dic['qtd_gols']
print('-' * 45)
print(dic)
print('-' * 45)
for k, v in dic.items():
    print(f'O campo {k.upper()} tem o valor {v}')
