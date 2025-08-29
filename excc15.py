class Passagem:
    def __init__(self, preco, assento):
        self.preco = preco
        self.assento = assento
    
    def alterar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"O preço do assento {self.assento} foi alterado para R$ {self.preco:.2f}.")
        
    def escolher_assento(self, novo_assento):
        self.assento = novo_assento
        print(f"O assento foi alterado para {self.assento}.")

class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito
    
    def abastecer(self):
        print(f"O ônibus de placa {self.placa} está abastecendo.")

class PassagemAviao(Passagem):
    def __init__(self, preco, assento, portao_de_embarque, checkin):
        super().__init__(preco, assento)
        self.portao_de_embarque = portao_de_embarque
        self.checkin = checkin

    def decolar(self):
        print("Autorizado para decolagem. Tenha uma boa viagem!")

# Exemplo de uso
passagem_onibus = PassagemBus(150.00, "25B", "ABC-1234", True)
passagem_aviao = PassagemAviao(800.00, "15A", "B05", True)

print("--- Passagem de Ônibus ---")
passagem_onibus.escolher_assento("30A")
passagem_onibus.abastecer()

print("\n--- Passagem de Avião ---")
passagem_aviao.alterar_preco(850.50)
print(f"Portão de Embarque: {passagem_aviao.portao_de_embarque}")
passagem_aviao.decolar()
