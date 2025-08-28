def calcular_volume_cilindro(raio, altura):
    pi = 3.141592
    volume = pi * (raio ** 2) * altura
    return volume

try:
    raio_cilindro = float(input("Digite o raio do cilindro: "))
    altura_cilindro = float(input("Digite a altura do cilindro: "))

    if raio_cilindro >= 0 and altura_cilindro >= 0:
        volume_cilindro = calcular_volume_cilindro(raio_cilindro, altura_cilindro)
        print(f"\nO volume do cilindro é: {volume_cilindro:.2f}")
    else:
        print("O raio e a altura devem ser valores não negativos.")
        
except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos.")