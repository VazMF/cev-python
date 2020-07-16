#crie um programa que tenha uma tupla com várias palavras (não usar acentos). depois disso, você dever mostrar para cada palavra, quais são as sua vogais.
print('-' * 40)
print(f'{"CONTADOR DE VOGAIS":^40}') #titulo
print('-' * 40)
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'progamador', 'futuro') #tupla com as palavras
for p in palavras: #repeticao para cada palavra em palavras
    print(f'\nNa palavra \033[34m{p.upper()}\033[m temos ', end='') #print a palavra em maiusculas
    for letra in p: #para cada letra em palavra
        if letra.lower() in 'aeiou': #se a letra em minusculas estiver em aeiou
            print(letra, end=' ') #print a letra
