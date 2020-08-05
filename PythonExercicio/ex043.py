#Dsenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
#abaixo de 18,5 = abaixo do peso; entre 18,5 e 25 = peso ideal; 25 até 30 = sobrepeso; acima de 40 = obesidade mórbida.
print('\033[31m------------IMC------------\033[m') #titúlo
peso = float(input('Quantos é seu peso? (kg) ')) #input do peso
altura = float(input('Qual é sua altura? (m) ')) #input da altura
imc = peso / (altura**2) #cálcula o imc
print('Seu IMC: \033[33m{:.1f}\033[m'.format(imc)) #mostra o resultado do cálculo
if imc < 18.5: #se o imc for menor que 18.5
    print('Você está \033[1mABAIXO\033[m do peso.') #print abaixo do peso
elif 18.5 <= imc < 25: #se o imc for menor ou igual a 25
    print('Você está com o peso \033[1mIDEAL\033[m.') #print peso ideal
elif 25 <= imc < 30: #se o imc for maior ou igual a 30
    print('Você está \033[1mSOBREPESO\033[m.') #print sobrepeso
elif 30 <= imc < 48:
    print('Você está em \033[1mOBESIDADE\033[m')
elif imc >= 40: #se o imc não se encaixar em nenhuma das outras alternativas
    print('Você está em \033[1mOBESIDADE MÓRBIDA\033[m.') #print obesidade mórbida
print('\033[31m-\033[m' * 27) #fim
