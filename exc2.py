def verifica_numero(numero):
    """
    Verifica se um número é positivo, negativo ou zero e retorna um valor correspondente.
    """
    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    else:
        return 0

# Exemplo de uso:
try:
    valor = float(input("Digite um número: "))
    resultado = verifica_numero(valor)
    
    if resultado == 1:
        print("O número é positivo.")
    elif resultado == -1:
        print("O número é negativo.")
    else:
        print("O número é zero.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número.")