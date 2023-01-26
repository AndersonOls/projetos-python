import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        global con
        con = mysql.connector.connect(host="localhost", database="aula",
                              user="root", password="", port="3307")
        print("Conectado ao banco de dados com sucesso!")
    except Error as erro:
        print("Erro de conexão: {}".format(erro))

def consulta(idAluno):
    try:
        conectar()
        consulta_sql = "SELECT * FROM alunos WHERE idAluno = " + idAluno
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print("Id:", linha[0])
            print("Matricula:", linha[1])
            print("Aluno: ", linha[2])
            print("Curso: ", linha[3])
            print("Turma: ", linha[4])
    except Error as erro:
        print("Falha ao consultar aluno: {}".format(erro))
    finally:
        if(con.is_connected()):
            cursor.close()
            con.close()

def atualiza(declaracao):
    try:
        conectar()
        altera_aluno = declaracao
        cursor = con.cursor()
        cursor.execute(altera_aluno)
        con.commit()
        print("Aluno alterado com sucesso!")
    except Error as erro:
        print("Falha ao alterar o aluno: {}".format(erro))
    finally:
        if(con.is_connected()):
            cursor.close()
            con.close()

print("Alteração de aluno")
idAluno = input("Digite o código do aluno: ")
consulta(idAluno)

turma = input("Entre com a nova turma do aluno: ")
declaracao = """ UPDATE alunos
SET turma = """ + turma + """ WHERE idAluno = """ + idAluno
atualiza(declaracao)

print("Conferencia: ")
idAluno = input("Digite o código do aluno: ")
consulta(idAluno)