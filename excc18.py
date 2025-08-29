class Imovel:
    def __init__(self, inscricao_municipal, valor_aluguel, iptu):
        self.inscricao_municipal = inscricao_municipal
        self.valor_aluguel = valor_aluguel
        self.iptu = iptu
    
    def obter_parcela_IPTU(self):
        return self.iptu / 12

    def set_valor_aluguel(self, novo_valor):
        self.valor_aluguel = novo_valor

class Casa(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, quartos, piscina, churrasqueira):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.quartos = quartos
        self.piscina = piscina
        self.churrasqueira = churrasqueira

class Apartamento(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, quartos, elevador, area_de_lazer):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.quartos = quartos
        self.elevador = elevador
        self.area_de_lazer = area_de_lazer

class Terreno(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, area_m2):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.area_m2 = area_m2
        
class Chacara(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, area_m2, piscina, churrasqueira):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.area_m2 = area_m2
        self.piscina = piscina
        self.churrasqueira = churrasqueira

# Exemplo de uso
imovel_casa = Casa("123456", 2500.00, 1200.00, 3, True, True)
imovel_apartamento = Apartamento("789101", 1800.00, 960.00, 2, True, True)

print("--- Dados da Casa ---")
print(f"Valor do aluguel: R$ {imovel_casa.valor_aluguel:.2f}")
print(f"Parcela mensal do IPTU: R$ {imovel_casa.obter_parcela_IPTU():.2f}")
print(f"Possui piscina? {'Sim' if imovel_casa.piscina else 'Não'}")

print("\n--- Dados do Apartamento ---")
imovel_apartamento.set_valor_aluguel(1950.00)
print(f"Novo valor do aluguel: R$ {imovel_apartamento.valor_aluguel:.2f}")
print(f"Possui elevador? {'Sim' if imovel_apartamento.elevador else 'Não'}")