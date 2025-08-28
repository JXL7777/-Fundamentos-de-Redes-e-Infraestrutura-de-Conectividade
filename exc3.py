def converter_para_segundos(horas, minutos, segundos):
    """
    Converte horas, minutos e segundos para o total em segundos.
    """
    total_segundos = (horas * 3600) + (minutos * 60) + segundos
    return total_segundos

# Exemplo de uso:
try:
    horas = int(input("Digite as horas: "))
    minutos = int(input("Digite os minutos: "))
    segundos = int(input("Digite os segundos: "))
    
    total = converter_para_segundos(horas, minutos, segundos)
    print(f"\nO total em segundos é: {total}")

except ValueError:
    print("Entrada inválida. Por favor, digite números inteiros.")