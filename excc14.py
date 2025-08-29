class Ingresso:
    def __init__(self, preco, setor):
        self.preco = preco
        self.setor = setor
    
    def alterar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"Preço alterado para R$ {self.preco:.2f}")

    def mostrar_setor(self):
        print(f"Setor do ingresso: {self.setor}")

class IngressoVIP(Ingresso):
    def __init__(self, preco, setor, camarote, open_bar, open_food, estacionamento):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def pegar_bebida(self):
        if self.open_bar:
            print("Acesso ao open bar liberado. Aproveite sua bebida!")
        else:
            print("Desculpe, este ingresso não inclui open bar.")
            
    def acessar_camarote(self):
        if self.camarote:
            print("Acesso ao camarote liberado. Bem-vindo!")
        else:
            print("Desculpe, este ingresso não dá acesso ao camarote.")

# Exemplo de uso
ingresso_comum = Ingresso(50.00, "Arquibancada")
ingresso_vip = IngressoVIP(250.00, "VIP", True, True, True, False)

print("--- Ingresso Comum ---")
ingresso_comum.mostrar_setor()
ingresso_comum.alterar_preco(60.00)

print("\n--- Ingresso VIP ---")
ingresso_vip.mostrar_setor()
ingresso_vip.pegar_bebida()
ingresso_vip.acessar_camarote()
print(f"Estacionamento incluso? {'Sim' if ingresso_vip.estacionamento else 'Não'}")