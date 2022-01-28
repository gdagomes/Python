'''Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random

msg = f'{"Sorteando Aluno":^30}'

print('*'*len(msg))
print(msg)
print('*'*len(msg))

lista_alunos = []

lista_alunos.append(input('Insira o nome do Aluno: '))
lista_alunos.append(input('Insira o nome do Aluno: '))
lista_alunos.append(input('Insira o nome do Aluno: '))
lista_alunos.append(input('Insira o nome do Aluno: '))

aluno_sorteado = random.randint(0, len(lista_alunos)-1)

print(f'\nO Aluno que deverá apagar o quandro é: {lista_alunos[aluno_sorteado]}.')