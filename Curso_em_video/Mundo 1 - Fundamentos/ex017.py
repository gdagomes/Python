'''Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

import math

msg = f'{"Calculando a Hipotenusa de um triângulo":^50}'

print('*'*len(msg))
print(msg)
print('*'*len(msg))

cateto_oposto = float(input('Cateto Oposto: '))
cateto_adjacente = float(input('Cateto Adjacente: '))

hipotenusa = math.sqrt(pow(cateto_oposto,2) + pow(cateto_adjacente,2))

print(f'A hipotenusa do triângulo é: {hipotenusa:.2f}')