'''Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

msg = f'{"Aluguel de Veículos":^30}'

print('*'*len(msg))
print(msg)
print('*'*len(msg))

dias_alugado = int(input('\nInsira a quantidade de dias que o veículo foi alugado: '))
km_percorridos = float(input('Quantos quilômetros foram percorridos? '))

valor_a_pagar = (dias_alugado * 60) + (km_percorridos * 0.15)

print(f'\n O valor a ser pago será de R${valor_a_pagar:.2f}.')