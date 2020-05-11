#Elabore um programa que calcule o valor a ser pago por um produto. considerando seu preço normal e condição de pagamento.
#à vista/dinheiro/cheque = 10% de desconto; à vista no cartão 5% de desconto; em até 2x no cartão preço normal; 3x ou mais no cartão = 20% de juros.
print('\033[31m===CALCULANDO PREÇO===\033[m') #titúlo
preço = float(input('Preço das compras: R$')) #pede o preço do produto
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
pagamento = int(input('Qual será a forma de pagamento? ')) #pede a forma de pagamento de acordo com as instruções
if pagamento == 1: #se o número digitado for 1
    total = preço - (preço * 10 / 100)
elif pagamento == 2: #se o número digitado for 2
    total = preço - (preço * 5 / 100)
elif pagamento == 3: #se o número digitado for 3
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} \033[33mSEM JUROS\033[m'.format(parcela))
elif pagamento == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} \033[33mCOM JUROS\033[m'.format(totparc, parcela))
else:
    total = preço
    print('\033[31mOPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE.\033[m')
print('Sua compra de \033[35mR${:.2f}\033[m vai custar \033[35mR${:.2f}\033[m no final.'.format(preço, total))
print('\033[31m=\033[m' * 22) #fim
