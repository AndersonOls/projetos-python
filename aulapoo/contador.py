import tkinter

class App:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Contador")
        self.window.geometry("360x640")
        self.window.resizable(False, False)

        self.pontos = tkinter.Label(self.window, text="0", font="Arial 80 bold",
                                    pady=50)
        self.pontos.pack()

        self.frame = tkinter.Frame(self.window, bg="green")
        self.frame.pack()

        self.botao_add = tkinter.Button(self.frame, text="Adicionar",
                                        bg="orange", width=20, command=self.adicionar)
        self.botao_add.pack(side="left")

        self.botao_diminuir = tkinter.Button(self.frame, text="Diminuir",
                                        bg="orange", width=20, command=self.diminuir)
        self.botao_diminuir.pack(side="left")

        self.valor = 0

        self.window.mainloop()

    def adicionar(self):
        self.valor += 1
        self.pontos.config(text="{}".format(self.valor))

    def diminuir(self):
        self.valor -= 1
        self.pontos.config(text="{}".format(self.valor))

App()