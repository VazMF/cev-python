#melhore o ex061, perguntando ao usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
print('\033[35m-=-GERADOR-DE-PA-=-\033[m') #titulo
primeiro = int(input('Primeiro termo: ')) #lê o primeiro termo
razao = int(input('Razão da PA: ')) #lê a razão
termo = primeiro #define termo como primeiro
cont = 1 #define contador como 1
total = 0 #define o total como 0
mais = 10 #define o mais como 10 pq esse é a quantidade inicial de termos que será mostrada
while mais != 0: #enquanto mais for diferente de 0
    total += mais #o total será a soma do total com o mais
    while cont <= total: #enquanto o contador for menor ou igual ao total
        print('{} \033[35m->\033[m '.format(termo), end='') #mostra o resultado com os 10 primeiros termos
        termo += razao #termo é o termo somado com a razão
        cont += 1 #contador sobe 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? ')) #lê quantos termos mais o usuário deseja mostrar
print('Progressão finalizada com {} termos mostrados.'.format(total)) #mostra o total de termos mostrado
