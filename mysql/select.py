import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host="localhost", database="aula",
                                  user="root", password="", port="3307")
    consulta = "SELECT * FROM alunos"
    cur = con.cursor()
    cur.execute(consulta)
    linhas = cur.fetchall()
    print("Número de registros retornados", cur.rowcount)

    for linha in linhas:
        print("ID: ", linha[0])
        print("Matricula: ", linha[1])
        print("Nome: ", linha[2])
        print("Curso: ", linha[3])
        print("Turma: ", linha[4], "\n")

except Error as erro:
    print("Falha ao inserir dados na tabela: {}".format(erro))