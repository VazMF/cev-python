#desenvolva um programa que leia duas notas de um aluno, calcule e mostre a média
print('\033[31m----MÉDIA DAS NOTAS----\033[m') #título
nota1 = float(input('Insira a nota do primeiro semestre: ')) #input da primeira nota para a varivel nota1
nota2 = float(input('Insira a nota do segundo semestre: ')) #input da segunda nota para a variavel nota2
print(f'A média semestral desse aluno é \033[31m{(nota1 + nota2) / 2:.1f}\033[m') #resultado da média obtido somando os dois inputs e dividindo por dois
