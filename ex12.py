try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if num1 > num2:
        diferenca = num1 - num2
        print(f"O maior número é: {num1}")
        print(f"A diferença entre os dois números é: {diferenca}")
    elif num2 > num1:
        diferenca = num2 - num1
        print(f"O maior número é: {num2}")
        print(f"A diferença entre os dois números é: {diferenca}")
    else:
        print("Números iguais.")
        
except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos.")