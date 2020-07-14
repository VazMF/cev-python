#crie um programa que leia quantos reais uma pessoa tem na carteira e converta pra dolares
print('\033[32m--------CONVERSOR DE MOEDAS--------\033[m') #titulo
r = float(input('Insira um valor em reais: R$')) #variavel r recebe o inpur de uma quantidade em reais
print(f'DÓLAR: \033[32mR${r:.2f}\033[m valem \033[32mU$${r/5.40:.2f}\033[m') #print convertendo reais para dolar americano
print(f'DÓLAR CANADENSE: \033[32mR${r:.2f}\033[m valem \033[32mC${r/3.97:.2f}\033[m') #print convertendo reais para dolar canadense
print(f'EURO: \033[32mR${r:.2f}\033[m valem \033[32m€{r/6.13:.2f}\033[m') #print convertendo reais para euro

