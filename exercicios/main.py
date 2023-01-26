from tkinter import *

class Triangulo:
    def __init__(self):
        self.window = Tk()
        self.window.title("Triângulo")
        self.window.geometry("400x200")
        self.window.config(bg="#4f67ff")

        self.txt_lado1 = Label(self.window, text="Insira a medida do primeiro lado:",
                               font="Arial 10 bold", bg="#4f67ff", fg="white", pady=10)
        self.txt_lado1.grid(row=0, column=0)

        self.input_lado1 = Entry(self.window, font="Arial 10 bold")
        self.input_lado1.grid(row=0, column=1)

        self.txt_lado2 = Label(self.window, text="Insira a medida do segundo lado:",
                               font="Arial 10 bold", bg="#4f67ff", fg="white", pady=10)
        self.txt_lado2.grid(row=1, column=0)

        self.input_lado2 = Entry(self.window, font="Arial 10 bold")
        self.input_lado2.grid(row=1, column=1)

        self.txt_lado3 = Label(self.window, text="Insira a medida do terceiro lado:",
                               font="Arial 10 bold", bg="#4f67ff", fg="white", pady=10)
        self.txt_lado3.grid(row=2, column=0)

        self.input_lado3 = Entry(self.window, font="Arial 10 bold")
        self.input_lado3.grid(row=2, column=1)

        self.btn_calcular = Button(self.window, text="Calcular", command=self.calcular)
        self.btn_calcular.grid(row=3, column=0)

        self.resultado = StringVar()
        self.txt_resultado = Label(self.window, textvariable=self.resultado, bg="#4f67ff",
                                   font="Arial 10 bold", fg="white")
        self.txt_resultado.grid(row=3, column=1)

        self.window.mainloop()

    def calcular(self):
        a = self.input_lado1.get()
        b = self.input_lado2.get()
        c = self.input_lado3.get()

        if (a == b) and (a == c):
            self.resultado.set("Triângulo Equilatero")
        elif (a == b) or (a == c) or (b == c):
            self.resultado.set("Triângulo Isósceles")
        else:
            self.resultado.set("Triângulo Escaleno")


Triangulo()