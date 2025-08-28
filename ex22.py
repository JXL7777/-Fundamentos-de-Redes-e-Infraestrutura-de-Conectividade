try:
    base_maior = float(input("Digite o valor da base maior do trapézio: "))
    base_menor = float(input("Digite o valor da base menor do trapézio: "))
    altura = float(input("Digite o valor da altura do trapézio: "))
    
    if base_maior > 0 and base_menor > 0 and altura > 0:
        area = ((base_maior + base_menor) * altura) / 2
        print(f"\nA área do trapézio é: {area:.2f}")
    else:
        print("Valores inválidos. A base maior, a base menor e a altura devem ser maiores que zero.")

except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos.")