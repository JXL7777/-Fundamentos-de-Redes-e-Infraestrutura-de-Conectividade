import math

try:
    numero = float(input("Digite um número: "))
    
    if numero > 0:
        quadrado = numero ** 2
        raiz_quadrada = math.sqrt(numero)
        
        print(f"\nO número digitado ao quadrado é: {quadrado}")
        print(f"A raiz quadrada do número digitado é: {raiz_quadrada:.2f}")
    else:
        print("O número não é positivo, portanto, os cálculos não serão realizados.")

except ValueError:
    print("Entrada inválida. Por favor, digite um valor numérico.")