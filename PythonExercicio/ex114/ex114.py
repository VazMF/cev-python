#Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site NÃO está acessível no momento.\033[m')
else:
    print('\33[32mConsegui acessar o site Pudim com SUCESSO\033[m')
