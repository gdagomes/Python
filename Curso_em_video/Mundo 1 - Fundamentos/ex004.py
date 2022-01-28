dado = input('Digite  algo: ').strip()
print(f'O tipo primitivo desse valor é: {type(dado)}'
      f'\nSó possui espaços? {dado.isspace()}'
      f'\nÉ um número? {dado.isnumeric()}'
      f'\nÉ alfabético? {dado.isalpha()}'
      f'\nÉ alfanumérico? {dado.isalnum()}'
      f'\nEstá em minúsculo? {dado.islower()}'
      f'\nEstá em maiúsculo? {dado.isupper()}'
      f'\nEstá capitalizado? {dado.istitle()}'
      )

