class Carro:
    def __init__(self, marca, modelo, cor, ano, valor, consumo):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.consumo = consumo  # Consumo em Km/L
        self.nivel_combustivel = 0
    
    def abastecer(self, litros):
        self.nivel_combustivel += litros
        print(f"Abastecido com {litros} litros.")

    def andar(self, distancia_km):
        litros_necessarios = distancia_km / self.consumo
        if self.nivel_combustivel >= litros_necessarios:
            self.nivel_combustivel -= litros_necessarios
            print(f"O carro andou {distancia_km} km. Foram gastos {litros_necessarios:.2f} litros.")
        else:
            print("Nível de combustível insuficiente para esta viagem.")

    def verificar_nivel(self):
        print(f"Nível de combustível atual: {self.nivel_combustivel:.2f} litros.")

    def calcular_imposto(self):
        ipva = self.valor * 0.035
        print(f"O IPVA do carro é: R$ {ipva:.2f}")

# Exemplo de uso
meu_carro = Carro("Ford", "Ka", "Vermelho", 2020, 45000.00, 12.0)

meu_carro.verificar_nivel()
meu_carro.abastecer(15)
meu_carro.verificar_nivel()

meu_carro.andar(100)
meu_carro.verificar_nivel()

meu_carro.calcular_imposto()