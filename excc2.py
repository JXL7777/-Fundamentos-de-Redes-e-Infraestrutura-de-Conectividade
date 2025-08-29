class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas
    
    def Alterar_editora(self, nova_editora):
        self.editora = nova_editora
    
    def Listar_qtde_paginas(self):
        print(f"O livro '{self.nome}' possui {self.paginas} páginas.")

# Exemplo de uso
livro1 = Livro("A Batalha do Apocalipse", "Eduardo Spohr", "Verus Editora", 586)

print(f"Informações iniciais do livro:")
print(f"Nome: {livro1.nome}")
print(f"Autor: {livro1.autor}")
print(f"Editora: {livro1.editora}")
livro1.Listar_qtde_paginas()

livro1.Alterar_editora("Nova Editora Ltda.")
print("\nEditora alterada.")
print(f"Nova editora: {livro1.editora}")
livro1.Listar_qtde_paginas()