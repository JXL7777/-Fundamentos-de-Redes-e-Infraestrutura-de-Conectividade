class Compra:
    def __init__(self, numero, produto, valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0.0
    
    def calcular_valor_total(self):
        icms = self.valor * 0.17
        frete = self.valor * 0.05
        self.valor_total = self.valor + icms + frete
        return self.valor_total

class CompraAvista(Compra):
    def __init__(self, numero, produto, valor, desconto):
        super().__init__(numero, produto, valor)
        self.desconto = desconto
    
    def calcular_valor_total(self):
        valor_com_impostos = super().calcular_valor_total()
        valor_final = valor_com_impostos * (1 - self.desconto)
        return valor_final

    def get_desconto(self):
        return self.desconto

    def set_desconto(self, novo_desconto):
        self.desconto = novo_desconto

class CompraParcelada(Compra):
    def __init__(self, numero, produto, valor, numero_parcelas):
        super().__init__(numero, produto, valor)
        self.numero_parcelas = numero_parcelas

    def simular_numero_de_parcelas(self):
        valor_total_compra = self.calcular_valor_total()
        valor_parcela = valor_total_compra / self.numero_parcelas
        print(f"O valor total de R$ {valor_total_compra:.2f} será dividido em {self.numero_parcelas} parcelas de R$ {valor_parcela:.2f}.")

    def get_numero_parcelas(self):
        return self.numero_parcelas

    def set_numero_parcelas(self, novo_numero):
        self.numero_parcelas = novo_numero

# Exemplo de uso
compra_a_vista = CompraAvista(1, "Notebook", 3000.00, 0.10) # 10% de desconto
compra_parcelada = CompraParcelada(2, "Smartphone", 2000.00, 12) # 12 parcelas

print("--- Compra à Vista ---")
valor_final_a_vista = compra_a_vista.calcular_valor_total()
print(f"Valor final com desconto: R$ {valor_final_a_vista:.2f}")

print("\n--- Compra Parcelada ---")
compra_parcelada.simular_numero_de_parcelas()