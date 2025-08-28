try:
    preco_aquisicao = float(input("Digite o preço de aquisição do produto: R$ "))

    if preco_aquisicao < 50.00:
        valor_venda = preco_aquisicao * 1.45
    else:
        valor_venda = preco_aquisicao * 1.30
    
    print(f"O valor de venda do produto é: R$ {valor_venda:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite um valor numérico válido.")