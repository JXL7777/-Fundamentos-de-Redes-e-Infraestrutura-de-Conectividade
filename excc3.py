class Aluno:
    def __init__(self, nome, ra, n1, n2, n3, n4):
        self.nome = nome
        self.ra = ra
        self.nota1 = n1
        self.nota2 = n2
        self.nota3 = n3
        self.nota4 = n4
    
    def Mostrar_situacao(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
        
        if media >= 7.0:
            return "APROVADO"
        elif media >= 5.0:
            return "EXAME"
        else:
            return "REPROVADO"

# Exemplo de uso
aluno1 = Aluno("Guilherme", "20231234", 8.5, 7.0, 9.0, 6.5)
aluno2 = Aluno("Isabela", "20234567", 6.0, 5.5, 4.0, 7.0)
aluno3 = Aluno("Lucas", "20238910", 3.0, 4.5, 2.0, 1.0)

print(f"O aluno {aluno1.nome} com RA {aluno1.ra} está: {aluno1.Mostrar_situacao()}")
print(f"O aluno {aluno2.nome} com RA {aluno2.ra} está: {aluno2.Mostrar_situacao()}")
print(f"O aluno {aluno3.nome} com RA {aluno3.ra} está: {aluno3.Mostrar_situacao()}")