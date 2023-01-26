class Computador:
    def __init__(self, marca, memoria, video):
        self.power = 0

        self.marca = marca
        self.memoria = memoria
        self.video = video

    def ligar(self):
        if self.power == 0:
            self.power = 1
            print("Ligando o PC...")
            print("PC Ligado")
        elif self.power == 1:
            print("O PC já está ligado!")

    def desligar(self):
        if self.power == 1:
            self.power = 0
            print("Desligando o PC...")
            print("PC Desligado")
        elif self.power == 0:
            print("O PC já está desligado!")

    def info(self):
        if self.power == 1:
            print(self.marca, self.memoria, self.video)
        elif self.power == 0:
            print("Informações indisponíveis, ligar o PC primeiro")

pc = Computador("Dell", "8gb", "Nvidia")
pc2 = Computador("Hp", "4gb", "Intel")
pc3 = Computador("Acer", "16gb", "Radeon")

pc.ligar()
pc.info()
pc2.ligar()
pc2.info()
pc3.ligar()
pc3.info()