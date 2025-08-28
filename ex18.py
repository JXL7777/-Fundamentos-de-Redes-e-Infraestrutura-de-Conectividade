try:
    numero = int(input("Digite um número inteiro maior que zero: "))
    
    if numero <= 0:
        print("Número inválido.")
    else:
        soma_algarismos = 0
        numero_temp = numero
        
        while numero_temp > 0:
            soma_algarismos += numero_temp % 10
            numero_temp //= 10
            
        print(f"A soma dos algarismos de {numero} é: {soma_algarismos}")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")