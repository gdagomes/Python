from mysql.connector import Error
from ConexaoMYSQL import *
from Usepandas import *

try:

    con = conexao()
    base = select(con)
    mostrar_dados(base)

except Error as e:

    print('Não foi possível se conectar ao Banco de Dados')

finally:
    print('Conexao Encerrada!')