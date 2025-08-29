class Funcionario:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.pontos_batidos = []
    
    def bater_ponto(self):
        self.pontos_batidos.append(True)
        print(f"{self.nome} bateu o ponto. Pontos registrados: {len(self.pontos_batidos)}")

class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao
    
    def bater_meta(self):
        print(f"O vendedor {self.nome} bateu a meta e recebeu uma comissão de R$ {self.comissao:.2f}.")

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha
        
    def acessar_sistema(self, senha_digitada):
        if self.senha == senha_digitada:
            print(f"O gerente {self.nome} acessou o sistema com sucesso.")
        else:
            print("Senha incorreta.")

# Exemplo de uso
vendedor1 = Vendedor("Carlos", "V101", 2500.00, 500.00)
gerente1 = Gerente("Fernanda", "G202", 8000.00, "senha123")

print("--- Dados do Vendedor ---")
vendedor1.bater_ponto()
vendedor1.bater_meta()

print("\n--- Dados do Gerente ---")
gerente1.bater_ponto()
gerente1.acessar_sistema("senha123")
gerente1.acessar_sistema("senhaerrada")