#melhore o ex061, perguntando ao usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
print('\033[35m-=-GERADOR-DE-PA-=-\033[m') #titulo
primeiro = int(input('Primeiro termo: ')) #input do primeiro termo
razao = int(input('Razão da PA: ')) #input da razão
termo = primeiro #variavel termo recebe o conteudo da variavel primeiro
cont = 1 #contador recebe 1
total = 0 #total recebe 0
mais = 10 #define o mais como 10 pq esse é a quantidade inicial de termos que será mostrada
while mais != 0: #enquanto mais for diferente de 0
    total += mais #o total será a soma do total com o mais
    while cont <= total: #enquanto o contador for menor ou igual ao total
        print(f'{termo} \033[35m->\033[m ', end='') #mostra o resultado com os 10 primeiros termos
        termo += razao #termo é o termo somado com a razão
        cont += 1 #contador sobe 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? [0 para parar] ')) #lê quantos termos mais o usuário deseja mostrar
print(f'Progressão finalizada com {total} termos mostrados.') #mostra o total de termos mostrado
