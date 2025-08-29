class Pessoa:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self):
        print(f"Iniciando negociação com {self.nome}...")

class PessoaFisica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf
    
    def exibir_cpf(self):
        print(f"CPF da pessoa física: {self.cpf}")

class PessoaJuridica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj

    def exibir_cnpj(self):
        print(f"CNPJ da pessoa jurídica: {self.cnpj}")

# Exemplo de uso
pessoa_fisica = PessoaFisica("Ana Paula", "9999-8888", "ana@email.com", "Rua A, 1", "123.456.789-00")
pessoa_juridica = PessoaJuridica("Empresa XYZ", "3333-2222", "contato@xyz.com", "Av. B, 2", "11.222.333/0001-44")

print("--- Pessoa Física ---")
pessoa_fisica.negociar()
pessoa_fisica.exibir_cpf()

print("\n--- Pessoa Jurídica ---")
pessoa_juridica.negociar()
pessoa_juridica.exibir_cnpj()