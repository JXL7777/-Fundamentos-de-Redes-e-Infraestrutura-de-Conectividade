try:
    distancia = float(input("Digite a distância percorrida em Km: "))
    litros = float(input("Digite a quantidade de litros de gasolina consumidos: "))
    
    if litros > 0:
        consumo = distancia / litros
        print(f"\nO consumo do carro é de {consumo:.2f} Km/l.")
        
        if consumo < 8:
            print("Venda o carro!")
        elif consumo >= 8 and consumo <= 14:
            print("Econômico!")
        elif consumo > 12:
            print("Super econômico!")
    else:
        print("A quantidade de litros de gasolina deve ser maior que zero.")

except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos.")