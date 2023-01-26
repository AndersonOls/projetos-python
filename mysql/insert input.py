import mysql.connector
from mysql.connector import Error

print("Cadastro de aluno")
matricula = input("Insira a matrícula do aluno: ")
nome = input("Insira o nome do aluno: ")
curso = input("Insira o curso: ")
turma = input("Insira a turma: ")

dados = '(' + matricula + ',\'' + nome + '\'' + ',\'' + curso + '\'' + ',\'' + turma + '\'' + ')'
declaracao = """ INSERT INTO alunos (matricula, nome, curso, turma) VALUES """

sql = declaracao + dados

try:
    con = mysql.connector.connect(host="localhost", database="aula",
                                  user="root", password="", port="3307")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    print(cur.rowcount, "registros inseridos na tabela")

except Error as erro:
    print("Falha ao inserir dados na tabela: {}".format(erro))
finally:
    if con.is_connected():
        cur.close()
        con.close()
        print("Conexão ao banco de dados foi encerrada")