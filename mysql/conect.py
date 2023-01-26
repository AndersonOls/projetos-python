import mysql.connector
from mysql.connector import errorcode

try:
    con = mysql.connector.connect(host="localhost", database="aula",
                                  user="root", password="", port="3307")
    db_info = con.get_server_info()
    print("Conectado ao servidor: ", db_info)
    cur = con.cursor()
    cur.execute("select database();")
    linha = cur.fetchone()
    print("Conectado ao banco de dados: ", linha)
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de dados não existe!")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Nome de usuário ou senha incorreto")
    else:
        print(error)
