""" Crie uma hierarquia de classes representando formas geométricas. Comece com uma classe base chamada "Forma" e, em seguida, crie classes derivadas como
"Círculo " e "Retângulo" que herdem da classe base.
Adicione métodos para calcular área e perímetro em 
cada classe derivada. """

import math

class Forma:
    def area(self):
        return 0
    
    def perimetro(self):
        return 0

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.raio
        
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)
    
circulo = Circulo(5)
retangulo = Retangulo(4,6)

print("Círculo:")
print(f"Área: {circulo.area():.2f}")
print(f"Perímetro: {circulo.perimetro():.2f}")

print("\nRetângulo:")
print(f"Área: {retangulo.area()}")
print(f"Perímetro: {retangulo.perimetro()}")