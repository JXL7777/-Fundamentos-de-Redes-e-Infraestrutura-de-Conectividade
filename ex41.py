def calcular_diferenca():
    soma_dos_quadrados = 0
    soma_dos_numeros = 0
    
    # Loop para os primeiros 100 números naturais
    for i in range(1, 101):
        # Soma dos quadrados
        soma_dos_quadrados += i**2
        
        # Soma dos números
        soma_dos_numeros += i
        
    # Quadrado da soma
    quadrado_da_soma = soma_dos_numeros**2
    
    # Diferença
    diferenca = quadrado_da_soma - soma_dos_quadrados
    
    print(f"A soma dos quadrados dos primeiros 100 números naturais é: {soma_dos_quadrados}")
    print(f"O quadrado da soma dos primeiros 100 números naturais é: {quadrado_da_soma}")
    print(f"A diferença é: {diferenca}")

calcular_diferenca()