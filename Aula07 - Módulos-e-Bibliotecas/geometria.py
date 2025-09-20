import math

def area_quadrado(lado: float) -> float:
    return lado ** 2

def perimetro_quadrado(lado: float) -> float:
    return 4 * lado


def area_retangulo(base: float, altura: float) -> float:
    return base * altura

def perimetro_retangulo(base: float, altura: float) -> float:
    return 2 * (base + altura)


def area_circulo(raio: float) -> float:
    # Usa math.pi para o valor de π
    return math.pi * (raio ** 2)

def perimetro_circulo(raio: float) -> float:
    # Circunferência = 2 * π * r
    return 2 * math.pi * raio