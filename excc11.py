class Filme:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao
    
    def play(self):
        print(f"Play no filme '{self.nome}'.")

class Acao(Filme):
    def __init__(self, nome, duracao, genero="Ação"):
        super().__init__(nome, duracao)
        self.genero = genero
        
    def explodir(self):
        print(f"Cena de explosão no filme de {self.genero}!")

class Drama(Filme):
    def __init__(self, nome, duracao, genero="Drama"):
        super().__init__(nome, duracao)
        self.genero = genero
    
    def emocionar(self):
        print(f"Cena emocionante no filme de {self.genero}!")

class Suspense(Filme):
    def __init__(self, nome, duracao, genero="Suspense"):
        super().__init__(nome, duracao)
        self.genero = genero
    
    def criar_tensao(self):
        print(f"Tensão crescente no filme de {self.genero}!")

# Exemplo de uso
filme_acao = Acao("Duro de Matar", "2h 12min")
filme_drama = Drama("A Procura da Felicidade", "1h 57min")
filme_suspense = Suspense("O Silêncio dos Inocentes", "1h 58min")

print("--- Filme de Ação ---")
filme_acao.play()
filme_acao.explodir()

print("\n--- Filme de Drama ---")
filme_drama.play()
filme_drama.emocionar()

print("\n--- Filme de Suspense ---")
filme_suspense.play()
filme_suspense.criar_tensao()