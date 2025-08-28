try:
    preco_antigo = float(input("Digite o preço antigo do produto: R$ "))
    
    if preco_antigo <= 50:
        aumento = preco_antigo * 0.05
    elif preco_antigo <= 100:
        aumento = preco_antigo * 0.10
    else:
        aumento = preco_antigo * 0.15
        
    preco_novo = preco_antigo + aumento
    
    print(f"\nO preço novo do produto é: R$ {preco_novo:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite um valor numérico.")