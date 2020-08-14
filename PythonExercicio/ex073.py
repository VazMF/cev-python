#crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. depois mostre:
#apenas os 5 primeiros; os últimos 4 colocados; uma lista com os timer em ordem alfabética; em que posição na tabela está o time da chapecoense.
print('' * 30)
print(f'{" BRASILEIRÃO 2019":^30 }') #titulo
print('=' * 30)
times = ('Flamengo', 'Santos', 'Pelmeiras', 'Grêmio',
         'Athletico-PR', 'São Paulo', 'Internacional',
         'Corinthians', 'Fortaleza', 'Goiás', 'Bahia',
         'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo0',
         'Ceará-SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí') #tupla com todos os times
print(f'Lista de times do Brasileirão 2019: {times}') #print com a lista de times
print('=' * 30)
print(f'TOP 5: {times[0:5]}') #print com os cinco primeiros colocados 
print('=' * 30)
print(f'4 ÚLTIMOS COLOCADOS: {times[-4:]}') #print com os 4 ultimos colocados
print('=' * 30)
print(f'EM ORDEM ALFABÉTICA: {sorted(times)}') #print em ordem alfabetica
print('=' * 30)
print(f'POSIÇÃO DO CHAPECONESE: {times.index("Chapecoense")+1}ª ') #print mostrando a colocacao do chapecoense
print('=' * 30)
