'''Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e
mostre na tela a sua porção Inteira.

Ex: Digite um número: 6.127
O número 6.127 tem a parte Inteira 6.'''

import math

msg = f'{"Porção Inteira de um número Real":^30}'

print('*'*len(msg))
print(msg)
print('*'*len(msg))

numero_real = float(input('Digite um número Real: '))

print(f'O número digitado foi {numero_real} e sua porção inteira é {math.trunc(numero_real)}.')



