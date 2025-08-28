
try:
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    num3 = float(input("Digite o terceiro número real: "))
    

    produto = num1 * (num2 / 2)
    

    soma = (num1 * 3) + num3
    
 
    cubo = num3 ** 3 
    
    print(f"\nResultados:")
    print(f"a) O produto do primeiro com a metade do segundo é: {produto}")
    print(f"b) A soma do triplo do primeiro com o terceiro é: {soma}")
    print(f"c) O terceiro número ao cubo é: {cubo}")

except ValueError:
    print("Entrada inválida. Por favor, digite números conforme solicitado.")