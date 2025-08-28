try:
    valor_produto = float(input("Digite o valor do produto: R$ "))
    estado_destino = input("Digite a sigla do estado de destino (MG, SP, RJ ou MS): ").upper()

    impostos = {
        'MG': 0.07,
        'SP': 0.12,
        'RJ': 0.15,
        'MS': 0.08
    }

    if estado_destino in impostos:
        taxa_imposto = impostos[estado_destino]
        valor_final = valor_produto * (1 + taxa_imposto)
        print(f"O preço final do produto para o estado de {estado_destino} é: R$ {valor_final:.2f}")
    else:
        print("Erro: Estado inválido. Por favor, digite MG, SP, RJ ou MS.")

except ValueError:
    print("Entrada inválida. Por favor, digite um valor numérico para o produto.")