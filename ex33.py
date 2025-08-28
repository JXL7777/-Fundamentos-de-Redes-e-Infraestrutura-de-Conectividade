try:
    venda_mensal = float(input("Digite o valor da venda mensal: R$ "))
    
    comissao = 0.0
    
    if venda_mensal >= 100000.00:
        comissao = 700.00 + (venda_mensal * 0.16)
    elif venda_mensal >= 80000.00:
        comissao = 650.00 + (venda_mensal * 0.14)
    elif venda_mensal >= 60000.00:
        comissao = 600.00 + (venda_mensal * 0.14)
    elif venda_mensal >= 40000.00:
        comissao = 550.00 + (venda_mensal * 0.14)
    elif venda_mensal >= 20000.00:
        comissao = 500.00 + (venda_mensal * 0.14)
    else:
        comissao = 400.00 + (venda_mensal * 0.14)
        
    print(f"\nA comissão a ser paga é: R$ {comissao:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite um valor numérico para a venda.")