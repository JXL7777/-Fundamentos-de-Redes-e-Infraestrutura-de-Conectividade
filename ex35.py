try:
    custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))
    
    comissao_distribuidor = 0.0
    impostos = 0.0
    
    if custo_fabrica <= 12000.00:
        comissao_distribuidor = custo_fabrica * 0.05
    elif custo_fabrica <= 25000.00:
        comissao_distribuidor = custo_fabrica * 0.10
        impostos = custo_fabrica * 0.15
    else:
        comissao_distribuidor = custo_fabrica * 0.15
        impostos = custo_fabrica * 0.20
        
    custo_consumidor = custo_fabrica + comissao_distribuidor + impostos
    
    print(f"\nO custo ao consumidor do carro é: R$ {custo_consumidor:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite um valor numérico.")