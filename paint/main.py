from tkinter import *

class Paint:
    def __init__(self):
        self.window = Tk()
        self.window.title("Paint")
        self.window.geometry("1280x720")
        self.window.resizable(False, False)

        self.oval = False
        self.line = True
        self.erase = False

        self.cores = ["black", "gray", "white", "red","red2", "red3","red4",
                      "green yellow","green2","green3","green","dark green",
                      "blue1","blue2", "blue3", "purple1","purple2","purple3"]

        self.pega_cor = "black"

        self.img_line = PhotoImage(file="icons/line.png")
        self.img_oval = PhotoImage(file="icons/oval.png")
        self.img_eraser = PhotoImage(file="icons/eraser.png")
        self.img_save = PhotoImage(file="icons/save.png")
        self.img_new = PhotoImage(file="icons/new.png")

        self.barra_menu = Frame(self.window, bg="#3b3b3b", height=50)
        self.barra_menu.pack(fill="x")

        self.txt_cor = Label(self.barra_menu, text="Cores: ", fg="white", bg="#3b3b3b")
        self.txt_cor.pack(side="left")

        for i in self.cores:
            self.btn_cor = Button(self.barra_menu, bg=i, width=4, height=2,
                                  command=lambda cor=i: self.seleciona_cor(cor))
            self.btn_cor.pack(side="left")

        self.txt_ferramentas = Label(self.barra_menu, text="Ferramentas: ", bg="#3b3b3b",
                                     fg="white").pack(side="left")
        self.btn_line = Button(self.barra_menu, image=self.img_line, bd=0, bg="#3b3b3b",
                               command=self.p_line).pack(side="left")
        self.btn_oval = Button(self.barra_menu, image=self.img_oval, bd=0, bg="#3b3b3b",
                               command=self.p_oval).pack(side="left")
        self.btn_eraser = Button(self.barra_menu, image=self.img_eraser, bd=0, bg="#3b3b3b",
                               command=self.p_erase).pack(side="left")

        self.txt_tamanho = Label(self.barra_menu, text="Tamanho: ", bg="#3b3b3b", fg="white")
        self.txt_tamanho.pack(side="left")
        self.caixa_tamanho = Spinbox(self.barra_menu, from_=1, to=50, width=8)
        self.caixa_tamanho.pack(side="left")

        self.btn_save = Button(self.barra_menu, image=self.img_save, bd=0, bg="#3b3b3b",
                                ).pack(side="right")
        self.btn_new = Button(self.barra_menu, image=self.img_new, bd=0, bg="#3b3b3b",
                               ).pack(side="right")


        self.area_desenho = Canvas(self.window, height=720,
                                   bg="gainsboro")
        self.area_desenho.pack(fill="both")
        self.area_desenho.bind("<B1-Motion>", self.desenho)

        self.window.mainloop()

    def desenho(self, event):
        x1,y1 =(event.x), (event.y)
        x2,y2 = (event.x), (event.y)

        if self.oval:
            self.area_desenho.create_oval(x1,y1,x2,y2, fill=self.pega_cor,
                                      outline=self.pega_cor, width=self.caixa_tamanho.get())
        elif self.line:
            self.area_desenho.create_line(x1 -10, y1 -10, x2, y2, fill=self.pega_cor,
                                          width=self.caixa_tamanho.get())
        else:
            self.area_desenho.create_oval(x1, y1, x2, y2, fill="gainsboro",
                                          outline="gainsboro", width=self.caixa_tamanho.get())


    def seleciona_cor(self, cor):
        self.pega_cor = cor

    def p_oval(self):
        self.oval = True
        self.line = False
        self.erase = False

    def p_line(self):
        self.oval = False
        self.line = True
        self.erase = False

    def p_erase(self):
        self.oval = False
        self.line = False
        self.erase = True




Paint()