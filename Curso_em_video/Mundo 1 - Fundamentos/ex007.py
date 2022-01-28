'''Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno,
 calcule e mostre a sua média.'''

msg = f'{"Média de um aluno":^30}'

print('*'*len(msg))
print(msg)
print('*'*len(msg))

nota_um = float(input("\nDigite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))

media = (nota_um + nota_dois)/2

print(f'\nA média do aluno é {media}')