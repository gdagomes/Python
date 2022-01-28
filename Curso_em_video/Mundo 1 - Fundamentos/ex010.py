'''Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem
na carteira e mostre quantos dólares ela pode comprar.'''

msg = f'{"Conversor moeda":^30}'

print('*'*len(msg))
print(msg)
print('*'*len(msg))

# valor do dolar ficticio e considerado um valor constante
dolar = 5.7372

real = float(input('\nQual valor você deseja converter para dólar? R$'))

conversao = real/dolar

print(f'\nCom {real:.2f} reais você comprará {conversao:.2f} dolares.')