def calcular_consumo_kwh(potencia_watts, tempo_horas):
    consumo = (potencia_watts * tempo_horas) / 1000
    return consumo

def calcular_conta_energia(consumo_kwh, valor_kwh):
    conta = consumo_kwh * valor_kwh
    return conta

try:
    potencia = float(input("Digite a potência do aparelho em Watts: "))
    tempo = float(input("Digite o tempo que o aparelho ficou ligado em horas: "))
    valor_kwh = float(input("Digite o valor de 1 KWh: R$ "))
    
    consumo_total = calcular_consumo_kwh(potencia, tempo)
    valor_conta = calcular_conta_energia(consumo_total, valor_kwh)
    
    print(f"\nO consumo total foi de: {consumo_total:.2f} KWh")
    print(f"O valor total da conta de energia é: R$ {valor_conta:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos.")