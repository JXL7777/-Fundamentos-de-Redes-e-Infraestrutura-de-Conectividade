import math

try:
    numero = float(input("Digite um número real: "))
    
    if numero >= 0:
        raiz_quadrada = math.sqrt(numero)
        print(f"A raiz quadrada de {numero} é: {raiz_quadrada:.2f}")
    else:
        numero_ao_quadrado = numero ** 2
        print(f"O número ao quadrado é: {numero_ao_quadrado}")
        
except ValueError:
    print("Entrada inválida. Por favor, digite um valor numérico.")