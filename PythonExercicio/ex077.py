#crie um programa que tenha uma tupla com várias palavras (não usar acentos). depois disso, você dever mostrar para cada palavra, quais são as sua vogais.
print('-' * 40)
print(f'{"CONTADOR DE VOGAIS":^40}')
print('-' * 40)
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'progamador', 'futuro')
for p in palavras:
    print(f'\nNa palavra \033[34m{p.upper()}\033[m temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
