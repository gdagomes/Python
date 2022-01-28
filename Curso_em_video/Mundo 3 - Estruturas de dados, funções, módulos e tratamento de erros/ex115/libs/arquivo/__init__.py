from ex115.libs.interface import cabecalho


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArq(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('Pessoas Cadastradas')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>.3} anos')
    finally:
        arquivo.close()


def cadastrar(nome_arq, nome='desconhecido', idade=0):
    try:
        arquivo = open(nome_arq, 'at')
    except:
        print('Erro ao tentar abrir o arquivo')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao cadastrar uma nova pessoa')
        else:
            print('Cadastro realizado com sucesso.')
    finally:
        arquivo.close()