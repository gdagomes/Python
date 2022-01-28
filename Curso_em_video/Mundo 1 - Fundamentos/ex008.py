'''Exercício Python 008: Escreva um programa que leia um valor
 em metros e o exiba convertido em centímetros e milímetros.'''

msg = f'{"Conversor de distâncias":^30}'

print('*'*len(msg))
print(msg)
print('*'*len(msg))

metros = float(input("Insira a distância em metros: "))

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print(f'\nConversor:')
print(f'{km} km')
print(f'{hm} hm')
print(f'{dam} dam')
print(f'{dm} dm')
print(f'{cm} cm')
print(f'{mm} mm')

