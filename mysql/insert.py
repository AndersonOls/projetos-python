import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host="localhost", database="aula",
                                  user="root", password="", port="3307")
    inserir_alunos = """ INSERT INTO alunos(matricula, nome, curso, turma)
                        VALUES
                        (271720, "William", "TI", "94"),
                        (875405, "João Pedro", "TI", "94"),
                        (886654, "Elysander", "TI", "93"),
                        (890697, "Maiko", "TI", "93")"""
    cur = con.cursor()
    cur.execute(inserir_alunos)
    con.commit()
    print(cur.rowcount, "registros inseridos na tabela")
except Error as erro:
    print("Falha ao inserir dados na tabela: {}".format(erro))
finally:
    if con.is_connected():
        cur.close()
        con.close()
        print("Conexão ao banco de dados foi encerrada")
