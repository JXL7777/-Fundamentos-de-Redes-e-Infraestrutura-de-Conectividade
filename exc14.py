def calcular_potencia(x, z):
    if z < 0:
        print("O expoente deve ser um número inteiro não negativo.")
        return None
    
    if z == 0:
        return 1
    
    resultado = 1
    for _ in range(z):
        resultado *= x
    return resultado

try:
    base = float(input("Digite o valor de X (a base): "))
    expoente = int(input("Digite o valor de Z (o expoente, inteiro e não negativo): "))
    
    potencia = calcular_potencia(base, expoente)
    
    if potencia is not None:
        print(f"\nO resultado de {base} elevado a {expoente} é: {potencia:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite um número para a base e um número inteiro para o expoente.")