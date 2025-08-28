try:
    cardapio = {
        100: 1.20,
        101: 1.30,
        102: 1.50,
        103: 1.20,
        104: 17.00,
        105: 9.50,
        106: 6.00
    }
    
    codigo = int(input("Digite o código do produto: "))
    
    if codigo in cardapio:
        quantidade = int(input("Digite a quantidade: "))
        if quantidade > 0:
            preco_total = cardapio[codigo] * quantidade
            print(f"\nValor a ser pago: R$ {preco_total:.2f}")
        else:
            print("Quantidade inválida. A quantidade deve ser maior que zero.")
    else:
        print("Código de produto inválido.")

except ValueError:
    print("Entrada inválida. Por favor, digite números inteiros para o código e a quantidade.")