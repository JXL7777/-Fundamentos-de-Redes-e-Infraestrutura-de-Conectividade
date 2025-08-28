import math

def calcular_tempo(minutos_utilizados):
    if minutos_utilizados < 15:
        return 0.0
    
    # Preço da primeira hora
    valor_total = 9.00
    
    # Se o tempo for maior que uma hora (60 minutos)
    if minutos_utilizados > 60:
        minutos_adicionais = minutos_utilizados - 60
        horas_adicionais = math.ceil(minutos_adicionais / 60)
        valor_total += horas_adicionais * 1.50
        
    return valor_total

try:
    tempo_em_minutos = int(input("Digite o tempo de permanência em minutos: "))
    
    if tempo_em_minutos >= 0:
        custo_estacionamento = calcular_tempo(tempo_em_minutos)
        print(f"\nO valor total a ser pago é: R$ {custo_estacionamento:.2f}")
    else:
        print("Tempo inválido. Por favor, digite um valor não negativo.")
        
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro para o tempo.")