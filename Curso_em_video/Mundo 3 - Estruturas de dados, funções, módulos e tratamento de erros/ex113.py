''' Exercício Python 113: Reescreva a função leiaInt() que fizemos no
desafio 104, incluindo agora a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade. '''

def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return inteiro


def leiaFloat(msg):
    while True:
        try:
            real = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return real


num_int = leiaInt('Digite um número inteiro: ')
num_real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {num_int} e o valor real foi {num_real}.')