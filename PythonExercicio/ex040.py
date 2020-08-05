#crie um programa que leia duas notas de um aluno e calcule sua média. mostrando uma mensagem no final de acordo com a média atingida: <50 reprovado, 50 ou 69 recuperação e >= 70 aprovado
print('\033[31m---------MÉDIA---------\033[m') #titulo
nota1 = float(input('Primeira nota: ')) #input da primeira nota na variavel n1
nota2 = float(input('Segunda nota: ')) #input da primeira nota na variavel n2
media = (nota1 + nota2) / 2 #variavel emdia recebe o calculo da media
print(f'A média do aluno é {media:.1f}') #print das duas notas e media do aluno
if 7 > media >= 5: #se a média for menor que 7 ou menor e igual a 5
    print('O aluno está em \033[33mRECUPERAÇÃO.\033[m') #print recuperação
elif media < 5: #se a média for menor que 5
    print('O aluno está \033[31mREPROVADO.\033[m') #print reprovado
elif media >= 7: #se a média for igual ou maior que 7
    print('O aluno está \033[32mAPROVADO.\033[m') #print aprovado
print('\033[31m-\033[m' * 23) #fim
