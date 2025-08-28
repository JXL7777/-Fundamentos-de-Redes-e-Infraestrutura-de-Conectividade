import math

def calcular_volume_esfera(raio):
    volume = (4/3) * math.pi * (raio ** 3)
    return volume

try:
    raio_esfera = float(input("Digite o raio da esfera: "))
    
    if raio_esfera >= 0:
        volume_esfera = calcular_volume_esfera(raio_esfera)
        print(f"\nO volume da esfera é: {volume_esfera:.2f}")
    else:
        print("O raio deve ser um valor não negativo.")
        
except ValueError:
    print("Entrada inválida. Por favor, digite um número para o raio.")