#Condições aninhadas, aula012.
nome = str(input('Qual é seu nome? '))
if nome == 'Maria Fernanda' or nome == 'Maria' or nome == 'Fernanda' or nome == 'Nanda':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'João' or nome == 'Paulo' or nome == 'Enzo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Julia Camila Batriz Nathalia':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))