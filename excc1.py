class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def getNome(self):
        return self.nome
        
    def setIdade(self, nova_idade):
        self.idade = nova_idade
        
    def imprimeEndereco(self):
        print(self.endereco)

# Exemplo de uso
pessoa1 = Pessoa("João Silva", 30, "Rua das Flores, 123")

print(f"Nome da pessoa: {pessoa1.getNome()}")

pessoa1.setIdade(31)
print(f"Nova idade da pessoa: {pessoa1.idade}")

print("Endereço da pessoa:")
pessoa1.imprimeEndereco()