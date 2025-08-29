class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    
    def calcularPerimetro(self):
        return self.ladoA + self.ladoB + self.ladoC
        
    def getMaiorLado(self):
        return max(self.ladoA, self.ladoB, self.ladoC)

    def e_equilatero(self):
        return self.ladoA == self.ladoB == self.ladoC

    def e_isoceles(self):
        return (self.ladoA == self.ladoB != self.ladoC) or \
               (self.ladoA == self.ladoC != self.ladoB) or \
               (self.ladoB == self.ladoC != self.ladoA)

    def e_escaleno(self):
        return self.ladoA != self.ladoB and self.ladoA != self.ladoC and self.ladoB != self.ladoC

try:
    a = float(input("Digite o comprimento do Lado A: "))
    b = float(input("Digite o comprimento do Lado B: "))
    c = float(input("Digite o comprimento do Lado C: "))

    if a + b > c and a + c > b and b + c > a:
        triangulo1 = Triangulo(a, b, c)

        print(f"\nPerímetro: {triangulo1.calcularPerimetro()}")
        print(f"Maior lado: {triangulo1.getMaiorLado()}")
        
        if triangulo1.e_equilatero():
            print("Classificação: Triângulo Equilátero")
        elif triangulo1.e_isoceles():
            print("Classificação: Triângulo Isósceles")
        elif triangulo1.e_escaleno():
            print("Classificação: Triângulo Escaleno")
            
    else:
        print("Os comprimentos informados não formam um triângulo válido.")

except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos.")