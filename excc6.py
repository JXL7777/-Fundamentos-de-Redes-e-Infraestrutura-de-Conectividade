import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def imprimir_raio(self):
        print(f"O valor do raio é: {self.raio}")
        
    def calcular_area(self):
        area = math.pi * (self.raio ** 2)
        print(f"A área do círculo é: {area:.2f}")
        
    def calcular_circunferencia(self):
        circunferencia = 2 * math.pi * self.raio
        print(f"A circunferência do círculo é: {circunferencia:.2f}")

# Exemplo de uso
circulo1 = Circulo(5)

circulo1.imprimir_raio()
circulo1.calcular_area()
circulo1.calcular_circunferencia()