#refaça o ex51. lendo primeiro o termo e a razão de uma PA. mostrando os 10 primeiros termos usando o while.
print('\033[35m-=-GERADOR-DE-PA-=-\033[m') #titulo
primeiro = int(input('Primeiro termo: ')) #input do primeiro termo
razao = int(input('Razão da PA: ')) #input da razão (de quantos em quantos números a pa vai pular)
termo = primeiro #define termo como o número do input
cont = 1 #define contador como 1
while cont <= 10: #enquanto o contador for menor ou igual a 10
    print(f'{termo} \033[35m->\033[m ', end='') #print formatado da com o termo da PA e a uma ->
    termo += razao #termo muda para a soma do termo com a razão
    cont += 1 #contador ganha mais um
print('FIM')
