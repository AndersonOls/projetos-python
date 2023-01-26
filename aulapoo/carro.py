class Carro:
    def __init__(self, marca: str,  modelo:str, ano:int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print("Carro ligado")

    def acelerar(self):
        print("Acelerando")

    def frear(self):
        print("Freou")

carro = Carro("VW", "Gol", 2007)
carro.ligar()
carro.acelerar()
carro.frear()