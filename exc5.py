def reverter_numero(numero_original):
    """
    Retorna o reverso de um número inteiro.
    """
    # Converte o número para string para facilitar a inversão
    numero_str = str(numero_original)
    
    # Verifica se o número é negativo e lida com o sinal
    if numero_str[0] == '-':
        reverso_str = '-' + numero_str[1:][::-1]
    else:
        reverso_str = numero_str[::-1]
    
    # Converte a string invertida de volta para um número inteiro
    numero_reverso = int(reverso_str)
    
    return numero_reverso

# Exemplo de uso:
try:
    valor = int(input("Digite um número inteiro: "))
    reverso = reverter_numero(valor)
    print(f"\nO reverso de {valor} é: {reverso}")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")