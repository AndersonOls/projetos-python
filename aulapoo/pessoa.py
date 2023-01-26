class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def dizer_ola(self):
        print("Olá meu nome é {}. Tenho {} anos e minha altura"
              " é {} metros".format(self.nome, self.idade, self.altura))

    def cozinhar(self, receita: str):
        print("Estou cozinhando: {}".format(receita))

    def andar(self, distancia: float):
        print("Saí para caminhar, volto quando completar {} metros".format(distancia))

pessoa = Pessoa("José", 25, 1.75)
pessoa.dizer_ola()
pessoa.cozinhar("Arroz")
pessoa.andar(300.0)