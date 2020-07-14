#Elabore um programa que calcule o valor a ser pago por um produto. considerando seu preço normal e condição de pagamento.
#à vista/dinheiro/cheque = 10% de desconto; à vista no cartão 5% de desconto; em até 2x no cartão preço normal; 3x ou mais no cartão = 20% de juros.
print('\033[35m===================CALCULANDO PREÇO===================\033[m') #titulo
preço = float(input('Preço das compras: R$')) #input do preço do produto
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''') #print do menu de opcoes
pagamento = int(input('Qual será a forma de pagamento? ')) #input da froma de pagamento escolhida
if pagamento == 1: #se a opcao for 1
    total = preço - (preço * 10 / 100) #o total recebe 10% de desconto
elif pagamento == 2: #se a opcao for 2
    total = preço - (preço * 5 / 100) #total recebe 5% de desconto
elif pagamento == 3: #se a opcao for 3
    total = preço #total recebe o valor normal do produto
    parcela = total / 2 #calculo da parcela
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} \033[33mSEM JUROS\033[m') #print das parcelas
elif pagamento == 4: #se a opcao for 4
    total = preço + (preço * 20 / 100) #total recebe 20% de juro
    totparc = int(input('Quantas parcelas? ')) #input do total de parcelas desejadas
    parcela = total / totparc #variavel parcela recebe o valor de cada parcela
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} \033[33mCOM JUROS\033[m') #print informando o total de parcelas e valor
else: #senao
    total = preço #total recebe preço
    print('\033[31mOPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE.\033[m')
print(f'Sua compra de \033[35mR${preço:.2f}\033[m vai custar \033[35mR${total:.2f}\033[m no final.') #print do total a pagar com desconto ou juros
