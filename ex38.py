import math

try:
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    if a == 0:
        print("Não é equação de segundo grau.")
    else:
        delta = b**2 - 4 * a * c
        
        print(f"\nO valor de delta é: {delta:.2f}")

        if delta < 0:
            print("Não existe raiz real.")
        elif delta == 0:
            raiz_unica = -b / (2 * a)
            print("Existe uma raiz real.")
            print(f"Raiz única: {raiz_unica:.2f}")
        else:
            raiz1 = (-b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-b - math.sqrt(delta)) / (2 * a)
            print("Existem duas raízes reais.")
            print(f"Raiz 1: {raiz1:.2f}")
            print(f"Raiz 2: {raiz2:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos para a, b e c.")
    