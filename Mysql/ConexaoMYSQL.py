import mysql.connector


def conexao():

    conexao = mysql.connector.connect(host='localhost',
                                      database='enem',
                                      user='root',
                                      password='')

    if conexao.is_connected():
        print()
        db_info = conexao.get_server_info()
        print(f'Conectado no servidor: {db_info}')

        cursor = conexao.cursor()
        cursor.execute('select database();')

        db_con = cursor.fetchone()
        print(f'Conectado no Bando de Dados: {db_con}')

    return conexao


def fechar_conexao(cursor):
    cursor.close()


def select(conexao):
    cursor = conexao.cursor()
    cursor.execute("select * from itens_prova_2019;")
    consult = cursor.fetchall()
    return consult