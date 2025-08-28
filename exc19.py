def avaliar_consumo_carro(distancia, litros):
    if litros <= 0:
        return None, "A quantidade de litros deve ser maior que zero."
    
    consumo = distancia / litros
    
    if consumo < 8:
        mensagem = "Gasta muito!"
    elif 8 <= consumo <= 15:
        mensagem = "Econômico!"
    else:
        mensagem = "Super econômico!"
        
    return consumo, mensagem

try:
    distancia_km = float(input("Digite a distância percorrida em Km: "))
    litros_consumidos = float(input("Digite a quantidade de litros consumidos: "))
    
    consumo_calculado, mensagem_consumo = avaliar_consumo_carro(distancia_km, litros_consumidos)

    if consumo_calculado is not None:
        print(f"\nO consumo do seu carro é: {consumo_calculado:.2f} Km/l")
        print(f"Mensagem: {mensagem_consumo}")
    else:
        print(f"\n{mensagem_consumo}")
        
except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos.")