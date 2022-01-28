'''Exercício Python 018: Faça um programa que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

import math

msg = f'{"Cálculo Seno, Cosseno e Tangente ":^30}'

print('*'*len(msg))
print(msg)
print('*'*len(msg))

angulo = float(input('\nDigite o ângulo que você deseja: '))

print('\nResultado')
print(f'Seno: {math.sin(math.radians(angulo)):.2f}')
print(f'Cosseno: {math.cos(math.radians(angulo)):.2f}')
print(f'Tangente: {math.tan(math.radians(angulo)):.2f}')
