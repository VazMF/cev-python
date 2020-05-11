#escreva um programa que leia um valor em metros e o exiba convertido em cm e em mm
#operadores aritimeticos, aula 07
from time import sleep #sleep
print('\033[31m---CONVERSOR---\033[m') #titúlo
m = int(input('\033[30mDigite um valor em metros\033[m: ')) #input do valor em m em uma variavel
print('\033[32mPROCESSANDO...\033[m')
sleep(1)
print('\033[30mQUILÔMETROS\033[m:  {}km'.format(m/1000)) #transformando m em km, dividindo o input pot 1000
print('\033[30mCENTÍMETROS\033[m: {}cm'.format(m*100)) #transformando m em cm, multiplicando o input  por 100
print('\033[30mDECÍMETROS\033[m: {}dc'.format(m*10)) #transformando m em dc, multiplicando o input por 10
print('\033[30mDECÂMETROS\033[m: {}dam'.format(m/10)) #transformando m em dam, dividindo o input por 10
print('\033[30mMILÍMETROS\033[m: {}mm'.format(m*1000)) #transformando m em mm, multiplicando o input por 1000
print('\033[30mHECTÔMETROS\033[m: {}hm'.format(m/100)) #transformando m em hm, dividindo o input por 100
