class Conta:
    def __init__(self, nome, cpf, numero, saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo
    
    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self.saldo += valor_deposito
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor_saque):
        if self.saldo > 0 and valor_saque > 0 and valor_saque <= self.saldo:
            self.saldo -= valor_saque
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
        else:
            print("Não foi possível realizar o saque. Saldo insuficiente ou valor inválido.")

    def imprimir_saldo(self):
        print(f"Saldo atual da conta de {self.nome}: R$ {self.saldo:.2f}")

# Exemplo de uso
conta1 = Conta("João da Silva", "123.456.789-00", "54321-0", 1000.00)

conta1.imprimir_saldo()
conta1.depositar(250.00)
conta1.imprimir_saldo()
conta1.sacar(150.00)
conta1.imprimir_saldo()
conta1.sacar(1500.00)
conta1.imprimir_saldo()