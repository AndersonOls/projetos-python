from tkinter import *

class Calc:
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculadora")
        self.window.config(bg="#1d2f38")
        self.window.resizable(False, False)

        self.tela_numeros = Entry(self.window, font="Arial 35 bold",
                                  bg="#1d2f38", fg="white", width=14, bd=0,
                                  justify="right")
        self.tela_numeros.pack()

        self.frame = Frame(self.window)
        self.frame.pack()

        self.button_1 = Button(self.frame, text="1", bg="orange", fg="white", bd=0,
                               font="Arial 20 bold", width=5, height=2, command=lambda: self.touch("1"))
        self.button_1.grid(row=2, column=0)

        self.button_2 = Button(self.frame, text="2", bg="orange", fg="white", bd=0,
                               font="Arial 20 bold", width=5, height=2, command=lambda: self.touch("2"))
        self.button_2.grid(row=2, column=1)

        self.button_3 = Button(self.frame, text="3", bg="orange", fg="white", bd=0,
                               font="Arial 20 bold", width=5, height=2, command=lambda: self.touch("3"))
        self.button_3.grid(row=2, column=2)

        self.button_4 = Button(self.frame, text="4", bg="orange", fg="white", bd=0,
                               font="Arial 20 bold", width=5, height=2, command=lambda: self.touch("4"))
        self.button_4.grid(row=1, column=0)

        self.button_5 = Button(self.frame, text="5", bg="orange", fg="white", bd=0,
                               font="Arial 20 bold", width=5, height=2, command=lambda: self.touch("5"))
        self.button_5.grid(row=1, column=1)

        self.button_6 = Button(self.frame, text="6", bg="orange", fg="white", bd=0,
                               font="Arial 20 bold", width=5, height=2, command=lambda: self.touch("6"))
        self.button_6.grid(row=1, column=2)

        self.button_7 = Button(self.frame, text="7", bg="orange", fg="white", bd=0,
                               font="Arial 20 bold", width=5, height=2, command=lambda: self.touch("7"))
        self.button_7.grid(row=0, column=0)

        self.button_8 = Button(self.frame, text="8", bg="orange", fg="white", bd=0,
                               font="Arial 20 bold", width=5, height=2, command=lambda: self.touch("8"))
        self.button_8.grid(row=0, column=1)

        self.button_9 = Button(self.frame, text="9", bg="orange", fg="white", bd=0,
                               font="Arial 20 bold", width=5, height=2, command=lambda: self.touch("9"))
        self.button_9.grid(row=0, column=2)

        self.button_0 = Button(self.frame, text="0", bg="orange", fg="white", bd=0,
                               font="Arial 20 bold", width=5, height=2, command=lambda: self.touch("0"))
        self.button_0.grid(row=3, column=1)

        self.button_igual = Button(self.frame, text="=", bg="orange", fg="white", bd=0,
                               font="Arial 20 bold", width=5, height=2, command=self.total)
        self.button_igual.grid(row=3, column=0)

        self.button_limp = Button(self.frame, text="C", bg="orange", fg="white", bd=0,
                                   font="Arial 20 bold", width=5, height=2, command= self.limpar)
        self.button_limp.grid(row=3, column=2)

        self.button_add= Button(self.frame, text="+", bg="orange", fg="white", bd=0,
                                  font="Arial 20 bold", width=5, height=2, command=lambda: self.touch("+"))
        self.button_add.grid(row=3, column=3)

        self.button_sub = Button(self.frame, text="-", bg="orange", fg="white", bd=0,
                                 font="Arial 20 bold", width=5, height=2, command=lambda: self.touch("-"))
        self.button_sub.grid(row=2, column=3)

        self.button_mult = Button(self.frame, text="*", bg="orange", fg="white", bd=0,
                                 font="Arial 20 bold", width=5, height=2, command=lambda: self.touch("*"))
        self.button_mult.grid(row=1, column=3)

        self.button_div = Button(self.frame, text="/", bg="orange", fg="white", bd=0,
                                 font="Arial 20 bold", width=5, height=2, command=lambda: self.touch("/"))
        self.button_div.grid(row=0, column=3)

        self.window.bind('<Return>', self.total_enter)

        self.window.mainloop()

    def touch(self, num):
        self.tela_numeros.insert(END, num)

    def limpar(self):
        self.tela_numeros.delete(0, END)

    def total(self):
        t = eval(self.tela_numeros.get())
        self.tela_numeros.delete(0, END)
        self.tela_numeros.insert(0, str(t))

    def total_enter(self, event):
        t = eval(self.tela_numeros.get())
        self.tela_numeros.delete(0, END)
        self.tela_numeros.insert(0, str(t))
Calc()