'''Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
 com 5% de desconto.'''

msg = f'{"Cálculo Desconto":^30}'

print('*'*len(msg))
print(msg)
print('*'*len(msg))

preco_atual = float(input('Insira o preço atual do produto: R$'))

preco_desconto = preco_atual - (preco_atual * (5/100))

print(f'\nPreço com 5% de desconto: R${preco_desconto:.2f}')