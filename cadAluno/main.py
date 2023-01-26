import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Cadastro():
    def __init__(self):
        self.window = Tk()
        self.window.title("Cadastro de aluno")
        self.window.resizable(False, False)
        self.window.geometry("480x240")

        self.img_novo = PhotoImage(file="icons/novo.png")
        self.img_edit = PhotoImage(file="icons/editar.png")

        self.frame_titulo = Frame(self.window, bg="#00c4eb")
        self.frame_titulo.pack(fill="x")

        self.lbl_titulo = Label(self.frame_titulo,
                                text="Cadastro de alunos",
                                font= "Arial 15 bold", fg="white",
                                bg="#00c4eb")
        self.lbl_titulo.pack()

        self.frame_botoes = Frame(self.window)
        self.frame_botoes.pack(fill='x')

        self.txt_novo = Label(self.frame_botoes, text="Novo Aluno",
                              font="Arial 15 bold").pack()
        self.btn_novo = Button(self.frame_botoes, image=self.img_novo, command=self.cadastro)
        self.btn_novo.pack(fill=BOTH)

        self.txt_edit = Label(self.frame_botoes, text="Editar Aluno",
                              font="Arial 15 bold").pack()
        self.btn_edit = Button(self.frame_botoes, image=self.img_edit, command=self.editar)
        self.btn_edit.pack(fill=BOTH)

        self.window.mainloop()

    def conectar(self):
        try:
            global con
            con = mysql.connector.connect(host="localhost", database="senac",
                                          user="root", password="", port="3307")
        except Error as erro:
            print("Erro de conexão: {}".format(erro))

    def comando(self, sql, msg_ok, msg_erro):
        try:
            self.conectar()
            cur = con.cursor()
            cur.execute(sql)
            con.commit()
            messagebox.showinfo(title="Completo", message= msg_ok)
        except Error:
            messagebox.showerror(title="Erro", message= msg_erro)
        finally:
            if con.is_connected():
                cur.close()
                con.close()

    def cadastro(self):
        def inserir():
            matricula = caixa_matricula.get()
            nome = caixa_nome.get()
            curso = caixa_curso.get()
            turma = caixa_turma.get()

            dados = '(' + matricula + ',\'' + nome + '\'' + ',\'' \
                    + curso + '\'' + ',\'' + turma + '\'' + ')'
            declaracao = """ INSERT INTO alunos 
                                (matricula, nome, curso, turma)
                                VALUES """
            sql = declaracao + dados

            caixa_matricula.delete(0, END)
            caixa_nome.delete(0, END)
            caixa_curso.delete(0, END)
            caixa_turma.delete(0, END)

            ok = "Aluno cadastrado com sucesso"
            erro = "Falha ao cadastrar o aluno"

            self.comando(sql, ok, erro)
            janela_novo.destroy()

        janela_novo = Toplevel()
        janela_novo.title("Novo aluno")
        janela_novo.resizable(False, False)
        janela_novo.geometry("480x150")

        lbl_matricula = Label(janela_novo, text="Matricula: ", font="Arial 15")
        lbl_matricula.grid(column=0, row=0)
        caixa_matricula = Entry(janela_novo, font="Arial 15", width=20)
        caixa_matricula.grid(column=1, row=0)

        lbl_nome = Label(janela_novo, text="Nome: ", font="Arial 15")
        lbl_nome.grid(column=0, row=1)
        caixa_nome = Entry(janela_novo, font='Arial 15', width=20)
        caixa_nome.grid(column=1, row=1)


        lbl_curso = Label(janela_novo, text="Curso: ", font="Arial 15")
        lbl_curso.grid(column=0, row=2)
        caixa_curso = Entry(janela_novo, font='Arial 15', width=20)
        caixa_curso.grid(column=1, row=2)

        lbl_turma = Label(janela_novo, text="Turma: ", font="Arial 15")
        lbl_turma.grid(column=0, row=3)
        caixa_turma = Entry(janela_novo, font="Arial 15", width=20)
        caixa_turma.grid(column=1, row=3)

        btn_cadastro = Button(janela_novo, text="Cadastrar", command=inserir)
        btn_cadastro.grid(column=1, row=4)


        janela_novo.mainloop()

    def editar(self):
        def consulta():
            try:
                self.conectar()
                sql = "SELECT * FROM alunos"
                cur = con.cursor()
                cur.execute(sql)
                res = cur.fetchall()
                for i in res:
                    lista_alunos.insert("", "end", values=i)
            except Error:
                messagebox.showerror(title="Erro", message="Erro ao buscar alunos")
            finally:
                if con.is_connected():
                    cur.close()
                    con.close()

        def exclui():
            select = lista_alunos.selection()
            if select:
                valor = lista_alunos.item(select, "values")
                id_del = valor[0]

                sql = "DELETE FROM alunos WHERE id = " + id_del
                ok = "Aluno excluido com sucesso!"
                erro = "Falha ao exclui o aluno!"

                self.comando(sql, ok, erro)
                janela_edit.destroy()
            else:
                messagebox.showwarning(title='Atenção', message="Nenhum aluno foi selecionado")
        def btn():
            def atualiza():
                up_id = caixa_id.get()
                up_matricula = caixa_matricula.get()
                up_nome = caixa_nome.get()
                up_curso = caixa_curso.get()
                up_turma = caixa_turma.get()

                sql = """UPDATE alunos
                SET matricula =""" + up_matricula + """, nome=""" + "\"" + up_nome + "\"" \
                + """, curso = """ + "\"" + up_curso + "\"" + """, turma= """ + "\"" + up_turma + \
                      "\"" + """ WHERE id= """ + up_id

                ok= "Aluno atuailzado com sucesso!"
                erro = "Impossível atualizar o aluno!"

                self.comando(sql, ok, erro)
                janela_atualiza.destroy()




            selecao = lista_alunos.selection()
            if selecao:
                janela_atualiza = Toplevel()
                janela_atualiza.title("Atualizar aluno")
                janela_atualiza.resizable(False, False)
                janela_atualiza.geometry("480x180")

                lbl_id = Label(janela_atualiza, text="ID: ", font="Arial 15")
                lbl_id.grid(column=0, row=0)
                caixa_id = Entry(janela_atualiza, font="Arial 15", width=20)
                caixa_id.grid(column=1, row=0)

                lbl_matricula = Label(janela_atualiza, text="Matricula: ", font="Arial 15")
                lbl_matricula.grid(column=0, row=1)
                caixa_matricula = Entry(janela_atualiza, font="Arial 15", width=20)
                caixa_matricula.grid(column=1, row=1)

                lbl_nome = Label(janela_atualiza, text="Nome: ", font="Arial 15")
                lbl_nome.grid(column=0, row=2)
                caixa_nome = Entry(janela_atualiza, font="Arial 15", width=20)
                caixa_nome.grid(column=1, row=2)

                lbl_curso = Label(janela_atualiza, text="Curso: ", font="Arial 15")
                lbl_curso.grid(column=0, row=3)
                caixa_curso = Entry(janela_atualiza, font="Arial 15", width=20)
                caixa_curso.grid(column=1, row=3)

                lbl_turma = Label(janela_atualiza, text="Turma: ", font="Arial 15")
                lbl_turma.grid(column=0, row=4)
                caixa_turma = Entry(janela_atualiza, font="Arial 15", width=20)
                caixa_turma.grid(column=1, row=4)

                btn_atualiza = Button(janela_atualiza, text="Atualizar", command=atualiza)
                btn_atualiza.grid(column=1, row=5)


                for i in lista_alunos.selection():
                    id, matricula, nome, curso, turma = lista_alunos.item(i, 'values')
                    caixa_id.insert(END, id)
                    caixa_id.config(state="readonly")
                    caixa_matricula.insert(END, matricula)
                    caixa_nome.insert(END, nome)
                    caixa_curso.insert(END, curso)
                    caixa_turma.insert(END, turma)
                janela_edit.destroy()
            else:
                messagebox.showwarning(title="Atenção", message="Nenhum aluno foi selecionado")



        janela_edit = Tk()
        janela_edit.title("Edição de aluno")
        janela_edit.resizable(False, False)
        janela_edit.geometry("600x300")

        lbl_edit = Label(janela_edit, text="Selecione um aluno para editar:",
                         font= "Arial 12 bold")
        lbl_edit.pack()

        colunas = ("ID", "Matricula", "Nome", "Curso", "Turma")
        lista_alunos = ttk.Treeview(janela_edit, columns=colunas)

        lista_alunos.heading("#0", text='')
        lista_alunos.heading("#1", text='ID')
        lista_alunos.heading("#2", text='Matricula')
        lista_alunos.heading("#3", text='Nome')
        lista_alunos.heading("#4", text='Curso')
        lista_alunos.heading("#5", text='Turma')

        lista_alunos.column("#0", width=1)
        lista_alunos.column("#1", width=60)
        lista_alunos.column("#2", width=100)
        lista_alunos.column("#3")
        lista_alunos.column("#4", width=100)
        lista_alunos.column("#5", width=100)

        consulta()

        lista_alunos.pack()

        btn_editar = Button(janela_edit, text="Editar", command=btn)
        btn_editar.pack(side="left", padx=15)

        btn_excluir = Button(janela_edit, text="Excluir", command=exclui)
        btn_excluir.pack(side="left")

        btn_cancelar = Button(janela_edit, text="Cancelar", command=janela_edit.destroy)
        btn_cancelar.pack(side="left", padx=15)


        janela_edit.mainloop()




Cadastro()