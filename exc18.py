def imprimir_lista_numerada(lista):
    for indice, elemento in enumerate(lista, 1):
        print(f"{indice}, {elemento}")

# Exemplo de uso:
frutas = ["Pera", "Uva", "Maçã", "Salada mista"]
imprimir_lista_numerada(frutas)

print("\n--- Outro exemplo ---")
numeros = [10, "vinte", 30.5, True]
imprimir_lista_numerada(numeros)