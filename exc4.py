def encontrar_maior(a, b, c):
    """
    Retorna o maior de três números.
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Exemplo de uso:
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    
    maior_numero = encontrar_maior(num1, num2, num3)
    print(f"\nO maior número é: {maior_numero}")

except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos.")