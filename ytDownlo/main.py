from tkinter import *
from pytube import YouTube
from tkinter import filedialog


class App():

    def __init__(self):
        self.window = Tk()
        self.window.title("Youtube Downloader")
        self.window.resizable(False, False)
        self.window.geometry("1280x720")

        self.audio = False
        self.video = False

        self.img_logo = PhotoImage(file="imagens/logo.png")
        self.img_button = PhotoImage(file="imagens/button.png")

        self.frame_logo = Frame(self.window, bg="#adadac")
        self.frame_logo.pack(fill="x")

        self.lbl_logo = Label(self.frame_logo, image=self.img_logo, bg="#adadac")
        self.lbl_logo.pack()

        self.frame_link = Frame(self.window, pady=20)
        self.frame_link.pack()

        self.txt_link = Label(self.frame_link, text="Insira o link: ", font="Arial 15")
        self.txt_link.pack(side="left")

        self.input_link = Entry(self.frame_link, font="Arial 20", width=50)
        self.input_link.pack(side="left")

        self.btn_download = Button(self.frame_link, image=self.img_button, bd=0,
                                   command= lambda: self.download(self.input_link.get()))
        self.btn_download.pack(side="left")

        self.frame_btn = Frame(self.window)
        self.frame_btn.pack()

        self.radio1 = Radiobutton(self.frame_btn, font="Arial 12", text="Audio .mp3",
                                  value=0, command=self.valida_audio)
        self.radio1.pack(side="left")
        self.radio2 = Radiobutton(self.frame_btn, font="Arial 12", text="Vídeo .mp4",
                                  value=1, command=self.valida_video)
        self.radio2.pack(side="left")

        self.window.mainloop()

    def valida_audio(self):
        self.audio = True
        self.video = False

    def valida_video(self):
        self.audio = False
        self.video = True

    def download(self, link):
        try:
            if self.audio:
                pasta = filedialog.askdirectory()
                YouTube(link).streams.filter(only_audio=True).first().download(pasta)
                self.completo()
            else:
                pasta = filedialog.askdirectory()
                YouTube(link).streams.first().download(pasta)
                self.completo()
        except:
            self.erro()

    def erro(self):
        janela = Toplevel()
        janela.title("Erro")
        janela.geometry("300x50")
        janela.resizable(False, False)

        mensagem = Label(janela, text="Link invalido!")
        mensagem.pack()

        btn_ok = Button(janela, text="Ok", command=janela.destroy)
        btn_ok.pack()

    def completo(self):
        janela = Toplevel()
        janela.title("Completo")
        janela.geometry("300x50")
        janela.resizable(False, False)

        mensagem = Label(janela, text="Download concluido!")
        mensagem.pack()

        btn_ok = Button(janela, text="Ok", command=janela.destroy)
        btn_ok.pack()


App()