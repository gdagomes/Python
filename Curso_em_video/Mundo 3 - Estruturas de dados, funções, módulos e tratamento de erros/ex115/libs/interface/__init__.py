def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return inteiro


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    for pos, item in enumerate(lista):
        print(f'\033[33m{pos+1}\033[m - \033[32m{item}\033[m')
    opc = leiaInt('Sua Opção: ')
    return opc
