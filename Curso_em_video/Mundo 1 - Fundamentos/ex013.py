'''Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre
seu novo salário, com 15% de aumento.'''

msg = f'{"Cálculo Aumento de Salário":^30}'

print('*'*len(msg))
print(msg)
print('*'*len(msg))

salario = float(input('Salário atual: R$'))

novo_salario = salario + (salario * (15/100))

print(f'\nNovo Salário com aumento de 15%: R${novo_salario:.2f}')