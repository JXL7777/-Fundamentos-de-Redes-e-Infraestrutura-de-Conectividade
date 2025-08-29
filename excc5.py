class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
    
    def nomeCompleto(self):
        print(f"Nome completo: {self.nome} {self.sobrenome}")
        
    def calcularSalario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        print(f"O salário do mês é: R$ {salario:.2f}")
        
    def incrementarHoras(self, horas_adicionais):
        self.horas_trabalhadas += horas_adicionais
        print(f"Horas trabalhadas atualizadas: {self.horas_trabalhadas}")

# Exemplo de uso
funcionario1 = Funcionario("Maria", "Souza", 160, 25.0)

funcionario1.nomeCompleto()
funcionario1.calcularSalario()

funcionario1.incrementarHoras(20)
funcionario1.calcularSalario()