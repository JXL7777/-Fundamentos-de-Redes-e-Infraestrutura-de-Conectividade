def criar_lista(quantidade, valor_padrao):
    return [valor_padrao] * quantidade

# Exemplo de uso 1:
lista_numerica = criar_lista(8, 1)
print(lista_numerica)

# Exemplo de uso 2:
lista_alfabetica = criar_lista(4, "A")
print(lista_alfabetica)