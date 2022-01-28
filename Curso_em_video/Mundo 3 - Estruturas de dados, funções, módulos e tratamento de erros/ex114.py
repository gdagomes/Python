'''Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''

from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

url = Request('http://pudim.com.br/')

try:
    response = urlopen(url)
except (HTTPError, URLError):
    print('\033[0;31mO site não está disponível.\033[m')
else:
    print('\033[0;31mConsegui acessar o site Pudim com sucesso!\033[m')