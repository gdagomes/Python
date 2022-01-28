def aumentar(valor=0, taxa=0, formatar=False):
    valor = valor + (valor * (taxa/100))
    return valor if not formatar else moeda(valor)


def diminuir(valor=0, taxa=0, formatar=False):
    valor = valor - (valor * (taxa / 100))
    return valor if not formatar else moeda(valor)


def dobro(valor=0, formatar=False):
    valor = valor * 2
    return valor if not formatar else moeda(valor)


def metade(valor=0, formatar=False):
    valor = valor / 2
    return valor if not formatar else moeda(valor)


def moeda(valor=0, moeda='R$'):
    return (f'{moeda}{valor:<8.2f}').replace('.', ',')


def resumo(moeda=0, aumento=10, desconto=10):
    print('-'*30)
    print(f'Resumo de R${moeda}'.center(30))
    print('-' * 30)
    print(f'Aumento de {aumento}%:\t\t{aumentar(moeda,aumento,True)}')
    print(f'Desconto de {desconto}%:\t{diminuir(moeda, desconto, True)}')
    print(f'Dobro do valor:\t\t{dobro(moeda, True)}')
    print(f'Metade do valor:\t{metade(moeda, True)}')
    print('-' * 30)
