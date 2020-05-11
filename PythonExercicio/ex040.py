#crie um programa que leia duas notas de um aluno e calcule sua média. mostrando uma mensagem no final de acordo com a média atingida: <50 reprovado, 50 ou 69 recuperação
# >= 70 aprovado
print('\033[31m---MÉDIA---\033[m') #titúlo
nota1 = float(input('Primeira nota: ')) #input da primeira nota
nota2 = float(input('Segunda nota: ')) #input da primeira nota
média = (nota1 + nota2) / 2 #calcúlo da nota
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 5: #se a média for menor que 7 ou menor e igual a 5
    print('O aluno está em \033[33mRECUPERAÇÃO.\033[m') #print recuperação
elif média < 5: #se a média for menor que 5
    print('O aluno está \033[31mREPROVADO.\033[m') #print reprovado
elif média >= 7: #se a média for igual ou maior que 7
    print('O aluno está \033[32mAPROVADO.\033[m') #print aprovado
print('\033[31m-\033[m' * 11) #fim