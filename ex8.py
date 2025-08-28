import math

try:
    numero = float(input("Digite um número: "))
    
    if numero >= 0:
        raiz_quadrada = math.sqrt(numero)
        print(f"A raiz quadrada de {numero} é: {raiz_quadrada:.2f}")
    else:
        print("Número inválido. Por favor, digite um número positivo.")

except ValueError:
    print("Entrada inválida. Por favor, digite um valor numérico.")