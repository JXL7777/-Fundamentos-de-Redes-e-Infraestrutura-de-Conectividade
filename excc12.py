class Pessoa:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, notas=None):
        super().__init__(matricula, nome, idade)
        if notas is None:
            self.notas = []
        else:
            self.notas = notas
        self.media = 0.0

    def calcular_media(self):
        if self.notas:
            self.media = sum(self.notas) / len(self.notas)
        else:
            self.media = 0.0
        print(f"A média do aluno {self.nome} é: {self.media:.2f}")

    def estudar(self):
        print(f"O aluno {self.nome} está estudando.")

class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formacao, disciplina, carga_horaria, salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario
    
    def lecionar(self):
        print(f"O professor {self.nome} está lecionando a disciplina de {self.disciplina}.")

# Exemplo de uso
aluno1 = Aluno("A123", "Maria", 20, [8.5, 7.0, 9.5])
professor1 = Professor("P456", "Dr. Almeida", 45, "Doutorado", "Desenvolvimento", 40, 8000.00)

print("--- Dados do Aluno ---")
print(f"Nome: {aluno1.nome}")
aluno1.estudar()
aluno1.calcular_media()

print("\n--- Dados do Professor ---")
print(f"Nome: {professor1.nome}")
print(f"Salário: R$ {professor1.salario:.2f}")
professor1.lecionar()