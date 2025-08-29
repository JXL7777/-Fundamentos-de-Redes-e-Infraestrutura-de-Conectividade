class ContaBancaria:
    def __init__(self, numero, titular, saldo):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")
            
    def imprimir_saldo(self):
        print(f"Saldo da conta de {self._titular}: R$ {self._saldo:.2f}")

class ContaCorrente(ContaBancaria):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo)
        
class ContaPoupanca(ContaBancaria):
    def __init__(self, numero, titular, saldo, taxa_juros):
        super().__init__(numero, titular, saldo)
        self._taxa_juros = taxa_juros

    def aplicar_juros(self):
        juros = self._saldo * (self._taxa_juros / 100)
        self._saldo += juros
        print(f"Juros de R$ {juros:.2f} aplicados. Novo saldo: R$ {self._saldo:.2f}")

class FundoDeAplicacao(ContaBancaria):
    def __init__(self, numero, titular, saldo, rendimento_anual):
        super().__init__(numero, titular, saldo)
        self._rendimento_anual = rendimento_anual

    def calcular_rendimento_anual(self):
        rendimento = self._saldo * (self._rendimento_anual / 100)
        print(f"O rendimento anual estimado é de R$ {rendimento:.2f}.")

# Exemplo de uso
conta_corrente = ContaCorrente(101, "Lucas", 1500.00)
conta_poupanca = ContaPoupanca(202, "Mariana", 5000.00, 0.5)
fundo_aplicacao = FundoDeAplicacao(303, "Fernanda", 10000.00, 7.5)

print("--- Conta Corrente ---")
conta_corrente.imprimir_saldo()
conta_corrente.depositar(200.00)
conta_corrente.sacar(100.00)
conta_corrente.imprimir_saldo()

print("\n--- Conta Poupança ---")
conta_poupanca.imprimir_saldo()
conta_poupanca.aplicar_juros()
conta_poupanca.imprimir_saldo()

print("\n--- Fundo de Aplicação ---")
fundo_aplicacao.imprimir_saldo()
fundo_aplicacao.sacar(1000.00)
fundo_aplicacao.calcular_rendimento_anual()
fundo_aplicacao.imprimir_saldo()