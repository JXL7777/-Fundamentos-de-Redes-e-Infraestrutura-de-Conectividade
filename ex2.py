try:
    numero = int(input("Digite um número inteiro: "))
    
    if numero > 10:
        print("É maior que 10")
    elif numero < 10:
        print("É menor que 10")
    else:
        print("É igual a 10")
        
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")