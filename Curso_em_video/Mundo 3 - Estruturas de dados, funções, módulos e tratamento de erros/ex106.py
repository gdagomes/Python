'''
Cores:
0 - sem cor
1 - vermelho
2 - verde
3 - amarelo
4 - azul
5 - roxo
6 - branco
'''


cor = ('\033[m', '\033[0;30;41m', '\033[0;30;42m', '\033[0;30;43m', '\033[0;30;44m', '\033[0;30;45m', '\033[7;30m')


def ajuda(com, c=0):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(cor[c], end="")
    help(com)
    print(cor[c], end="")


def titulo(tit,c=0):
    print(cor[c], end="")
    print("*" * len(tit))
    print(tit)
    print("*" * len(tit))
    print(cor[0], end="")

while True:
    titulo(f"{'Sistema PyHelp':^30}", 2)
    funcao = str(input("Funcao ou Biblioteca >>> "))
    if funcao.upper() == 'FIM':
        break
    else:
        ajuda(funcao, 3)

titulo(f"{'Volte Logo!':^15}", 2)

