class Brinquedos:
    def __init__(self, nome, cor, tamanho, preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        print(f"Estou brincando com o(a) {self.nome}.")

class BuzzLightyear(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, asas_abertas=False):
        super().__init__(nome, cor, tamanho, preco)
        self.asas_abertas = asas_abertas

    def brincar(self):
        print(f"Ao infinito e além! O {self.nome} está voando!")

    def voar(self):
        self.asas_abertas = True
        print("Asas ativadas!")

class Woody(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, cinto_amarrado=False):
        super().__init__(nome, cor, tamanho, preco)
        self.cinto_amarrado = cinto_amarrado
    
    def brincar(self):
        print(f"Tem uma cobra na minha bota! O {self.nome} está laçando.")

    def lancar_laco(self):
        print("Laço lançado!")

class Rex(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, medroso=True):
        super().__init__(nome, cor, tamanho, preco)
        self.medroso = medroso
    
    def brincar(self):
        print(f"O {self.nome} está tentando rugir assustadoramente... Ahh!")

    def rugir(self):
        if self.medroso:
            print("Roaaar... Ops, quase!")
        else:
            print("ROAAAAR! Que medo!")

# Exemplo de uso
buzz = BuzzLightyear("Buzz Lightyear", "Branco e Verde", "Médio", 50.0)
woody = Woody("Woody", "Marrom", "Médio", 45.0)
rex = Rex("Rex", "Verde", "Grande", 35.0)

buzz.brincar()
buzz.voar()

woody.brincar()
woody.lancar_laco()

rex.brincar()
rex.rugir()