try:
    a = float(input("Digite o valor do lado A: "))
    b = float(input("Digite o valor do lado B: "))
    c = float(input("Digite o valor do lado C: "))
    
    # Verifica se os valores podem formar um triângulo
    if a < b + c and b < a + c and c < a + b:
        print("Os valores podem formar um triângulo.")
        
        # Classifica o tipo de triângulo
        if a == b and b == c:
            print("É um triângulo Equilátero.")
        elif a == b or a == c or b == c:
            print("É um triângulo Isósceles.")
        else:
            print("É um triângulo Escaleno.")
    else:
        print("Os valores não podem formar um triângulo.")

except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos.")