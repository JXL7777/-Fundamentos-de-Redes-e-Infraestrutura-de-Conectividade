class Aluno_Academia:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self._mensalidade_base = 120.00

    def Calcular_IMC(self):
        return self.peso / (self.altura ** 2)

    def Obter_valor_mensalidade(self):
        if self.idade < 18:
            return self._mensalidade_base * 0.8  # Desconto de 20% para menores
        else:
            return self._mensalidade_base

# Exemplo de uso
aluno1 = Aluno_Academia("Pedro", 16, 65, 1.70)
aluno2 = Aluno_Academia("Ana", 25, 75, 1.65)

print("--- Dados de Pedro (menor de idade) ---")
print(f"Nome: {aluno1.nome}")
print(f"IMC: {aluno1.Calcular_IMC():.2f}")
print(f"Mensalidade: R$ {aluno1.Obter_valor_mensalidade():.2f}")

print("\n--- Dados de Ana (maior de idade) ---")
print(f"Nome: {aluno2.nome}")
print(f"IMC: {aluno2.Calcular_IMC():.2f}")
print(f"Mensalidade: R$ {aluno2.Obter_valor_mensalidade():.2f}")