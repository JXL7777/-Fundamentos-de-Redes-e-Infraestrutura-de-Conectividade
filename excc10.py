class Nota_Fiscal:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, icms, frete, ipi):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_total = 0.0

    def obterNumero(self):
        return self.numero

    def obterDataEmissao(self):
        return self.data

    def alterarRazaoSocial(self, nova_razao_social):
        self.razao_social = nova_razao_social

    def calcularValorTotal(self, valor_produto):
        self.valor_total = valor_produto + self.frete + self.icms + self.ipi
        return self.valor_total

# Exemplo de uso
nf1 = Nota_Fiscal(
    numero=1001,
    tipo="Saída",
    serie=1,
    cnpj="11.222.333/0001-44",
    razao_social="Empresa A Ltda",
    data="28/08/2025",
    icms=25.50,
    frete=10.00,
    ipi=5.25
)

nf1.alterarRazaoSocial("Nova Empresa B S.A.")

print(f"Número da NF: {nf1.obterNumero()}")
print(f"Data de Emissão: {nf1.obterDataEmissao()}")
print(f"Nova Razão Social: {nf1.razao_social}")

valor_produto_exemplo = 500.00
valor_final = nf1.calcularValorTotal(valor_produto_exemplo)
print(f"Valor total da nota fiscal: R$ {valor_final:.2f}")