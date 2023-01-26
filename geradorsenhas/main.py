from tkinter import  *
import random

class Gerador():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("720x480")
        self.window.config(bg="#04447d")
        self.window.title("Gerador de Senhas")

        self.img_logo = PhotoImage(file="icons/logo.png")

        self.frame_logo = Frame(self.window, bg="#04447d",pady=20)
        self.frame_logo.pack(fill="x")
        self.lbl_img = Label(self.frame_logo, image=self.img_logo, bg="#04447d")
        self.lbl_img.pack()
        self.txt_titulo = Label(self.frame_logo, text="Gerador de senha",
                                bg="#04447d", font="Arial 30 bold", fg="white")
        self.txt_titulo.pack()

        self.frame_info = Frame(self.window,bg="#04447d")
        self.frame_info.pack(fill='x')

        self.lbl_tamanho = Label(self.frame_info, text="Escolha o tamanho da sua senha: ",
                                 bg="#04447d", fg="white", font="Arial 15")
        self.lbl_tamanho.grid(row=0, column=0)
        self.list_tamanho = Spinbox(self.frame_info, from_=10, to=25)
        self.list_tamanho.grid(row=0, column=1)

        self.lbl_senha_fraca = Label(self.frame_info, text="Senha simples: ",
                                     bg="#04447d", fg="white", font="Arial 15")
        self.lbl_senha_fraca.grid(row=1, column=0)
        self.senha_fraca = StringVar()
        self.txt_senha_fraca = Label(self.frame_info, textvariable=self.senha_fraca,
                                     bg="#04447d", fg="white", font="Arial 15")
        self.txt_senha_fraca.grid(row=1, column=1)

        self.lbl_senha_media = Label(self.frame_info, text="Senha intermediaria: ",
                                     bg="#04447d", fg="white", font="Arial 15")
        self.lbl_senha_media.grid(row=2, column=0)
        self.senha_media = StringVar()
        self.txt_senha_media = Label(self.frame_info, textvariable=self.senha_media,
                                     bg="#04447d", fg="white", font="Arial 15")
        self.txt_senha_media.grid(row=2, column=1)

        self.lbl_senha_forte = Label(self.frame_info, text="Senha forte: ",
                                     bg="#04447d", fg="white", font="Arial 15")
        self.lbl_senha_forte.grid(row=3, column=0)
        self.senha_forte = StringVar()
        self.txt_senha_forte = Label(self.frame_info, textvariable=self.senha_forte,
                                     bg="#04447d", fg="white", font="Arial 15")
        self.txt_senha_forte.grid(row=3, column=1)

        btn_gerar = Button(self.frame_info, text="Gerar", font="Arial 15",
                           command=self.gerar)
        btn_gerar.grid(row=4, column=1)

        self.window.mainloop()

    def gerar(self):
        self.tamanho = self.list_tamanho.get()
        self.password_simples = ''
        self.lowercase = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(int(self.tamanho)):
            self.randChar = random.choice(self.lowercase)
            self.password_simples = self.password_simples + self.randChar
        self.senha_fraca.set(self.password_simples)

        self.password_medio = ''
        self.uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(int(self.tamanho)):
            self.randChar = random.choice(self.lowercase + self.uppercase)
            self.password_medio = self.password_medio + self.randChar
        self.senha_media.set(self.password_medio)

        self.password_dificil = ''
        self.specials = '1234567890!@#$%&*-+'
        for i in range(int(self.tamanho)):
            self.randChar = random.choice(self.lowercase + self.uppercase + self.specials)
            self.password_dificil = self.password_dificil + self.randChar
        self.senha_forte.set(self.password_dificil)





Gerador()