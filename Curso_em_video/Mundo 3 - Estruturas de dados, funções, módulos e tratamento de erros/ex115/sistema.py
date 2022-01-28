'''Exercício Python 115a/115b/115c:
Vamos criar um menu em Python, usando modularização.'''

from ex115.libs.interface import *
from time import sleep
from ex115.libs.arquivo import *

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criarArq(arq)

while True:
    resp = menu(['Listar pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do Sistema'])
    if resp == 1:
        lerArq(arq)
    elif resp == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: ')).strip()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo do sistema... Até Logo!')
        sleep(1)
        break
    else:
        print('\033[31mErro: Opção inválida!\033[m')