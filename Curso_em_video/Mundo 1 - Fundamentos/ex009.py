'''Exercício Python 009: Faça um programa que leia um número Inteiro
qualquer e mostre na tela a sua tabuada.'''

msg = f'{"Tabuada":^30}'

print('*'*len(msg))
print(msg)
print('*'*len(msg))

num_tab = int(input("\nVocê deseja visualizar a tabuada de qual número? "))

print(f'\nTabuada do {num_tab}\n')

print(f'{num_tab} x {"1":2} = {num_tab*1}')
print(f'{num_tab} x {"2":2} = {num_tab*2}')
print(f'{num_tab} x {"3":2} = {num_tab*3}')
print(f'{num_tab} x {"4":2} = {num_tab*4}')
print(f'{num_tab} x {"5":2} = {num_tab*5}')
print(f'{num_tab} x {"6":2} = {num_tab*6}')
print(f'{num_tab} x {"7":2} = {num_tab*7}')
print(f'{num_tab} x {"8":2} = {num_tab*8}')
print(f'{num_tab} x {"9":2} = {num_tab*9}')
print(f'{num_tab} x {"10":2} = {num_tab*10}')
