'''Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,
 calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de
 tinta pinta uma área de 2 metros quadrados.'''

msg = f'{"Calculando a quantidade de tinta":^30}'

print('*'*len(msg))
print(msg)
print('*'*len(msg))

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = larg * alt
litros_tinta = area / 2

print(f'\nSua parede tem a dimensão de {larg} x {alt} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {litros_tinta:.2f} litros de tinta.')