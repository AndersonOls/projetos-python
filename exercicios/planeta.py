from tkinter import *
from tkinter import ttk

class Planeta:
    def __init__(self):
        self.window = Tk()
        self.window.title("Peso no Planeta")
        self.window.geometry("400x200")
        self.window.config(bg="#69cf95")

        self.txt_peso = Label(self.window, text="Insira o seu peso em Kg:",
                               font="Arial 10 bold", bg="#69cf95", fg="white", pady=10)
        self.txt_peso.grid(row=0, column=0)

        self.input_peso = Entry(self.window, font="Arial 10 bold")
        self.input_peso.insert(0, "0.00")
        self.input_peso.grid(row=0, column=1)

        self.txt_planeta = Label(self.window, text="Selecione o planeta: ",
                                 font="Arial 10 bold", bg="#69cf95", fg="white", pady=10)
        self.txt_planeta.grid(row=1, column=0)

        self.lista_planeta = ["Mercúrio", "Vênus", "Marte", "Júpiter", "Saturno", "Urano",
                              "Netuno", "Plutão"]
        self.combo_planeta = ttk.Combobox(self.window, values=self.lista_planeta)
        self.combo_planeta.set("Mercúrio")
        self.combo_planeta.grid(row=1, column=1)

        self.btn_calcular = Button(self.window, text="Calcular", command=self.calcular)
        self.btn_calcular.grid(row=3, column=0)

        self.resultado = StringVar()
        self.txt_resultado = Label(self.window, textvariable=self.resultado, bg="#69cf95",
                                   font="Arial 10 bold", fg="black", width=10, height=1)
        self.txt_resultado.grid(row=3, column=1)


        self.window.mainloop()

    def calcular(self):
        p = self.combo_planeta.get()
        peso = float(self.input_peso.get())
        if p == "Mercúrio":
            r = peso * 0.37
            self.resultado.set(str(r))
        elif p == "Vênus":
            r = peso * 0.88
            self.resultado.set(str(r))
        elif p == "Marte":
            r = peso * 0.38
            self.resultado.set(str(r))
        elif p == "Júpiter":
            r = peso * 2.64
            self.resultado.set(str(r))
        elif p == "Saturno":
            r = peso * 1.15
            rf = "{:.2f}".format(r)
            self.resultado.set(str(rf))
        elif p == "Urano":
            r = peso * 1.17
            self.resultado.set(str(r))
        elif p == "Netuno":
            r = peso * 1.18
            self.resultado.set(str(r))
        elif p == "Plutão":
            r = peso * 0.11
            self.resultado.set(str(r))

Planeta()