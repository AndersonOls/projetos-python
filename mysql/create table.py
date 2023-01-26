import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", database="aula",
                                  user="root", password="", port="3307")
    criar_tabela = """CREATE TABLE alunos(
                       idAluno INT(11) NOT NULL AUTO_INCREMENT,
                       matricula INT(6),
                       nome VARCHAR(20),
                       curso VARCHAR(10),
                       turma VARCHAR(2),
                       CONSTRAINT pk_alunos PRIMARY KEY (idAluno)
                       );"""
    cur = con.cursor()
    cur.execute(criar_tabela)
    print("Tabela criada com sucesso!")

except mysql.connector.Error as erro:
    print("Falha ao criar tabela: {}".format(erro))
finally:
    if con.is_connected():
        cur.close()
        con.close()
        print("Conexão ao banco de dados foi encerrada")