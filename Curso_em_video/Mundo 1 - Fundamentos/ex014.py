'''Exercício Python 014: Escreva um programa que converta uma temperatura digitando
em graus Celsius e converta para graus Fahrenheit.'''

msg = f'{"Conversor de Temperatura":^30}'

print('*'*len(msg))
print(msg)
print('*'*len(msg))

temp_Celsius = float(input('\nInforme a temperatura em ºC: '))

temp_Fahrenheit = (temp_Celsius * 1.8) + 32

print(f'\nTemperatura em Fahrenheit: {temp_Fahrenheit:.1f}ºF')