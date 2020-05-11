#desenvolva um programa que leia duas notas de um aluno, calcule e mostre a média
from time import sleep #sleep
print('\033[31m---MÉDIA DAS NOTAS---\033[m') #título
nota1 = float(input('Insira a nota do primeiro semestre: ')) #input da primeira nota
nota2 = float(input('Insira a nota do segundo semestre: ')) #input da segunda nota
print('\033[33mPROCESSANDO...\033[m')
print('A média semestral desse aluno é \033[31m{:.1f}\033[m'.format((nota1 + nota2) / 2)) #resultado da média obtido somando os dois inputs e dividindo por dois
