def pot(base, expoente):
    """
    Calcula e exibe a potência de um número.
    """
    for i in range(1, expoente + 1):
        resultado = base ** i
        print(f"{base} ** {i} = {resultado}")

# Exemplo de uso:
pot(2, 3)