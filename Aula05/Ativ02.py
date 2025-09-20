""" Crie um programa que define uma função

calcular_area_retangulo que recebe dois argumentos,
comprimento e largura de um retângulo, e retorna a
área desse retângulo. Em seguida, o programa deve
solicitar ao usuário que insira o comprimento e a

largura e imprimir a área calculada. """

def calcular_area_retangulo(a,b):
    return a*b

comprimento = float(input("Digite o comprimento do retângulo: "))
largura = float(input("Digite a largura do retângulo: "))

area = calcular_area_retangulo(comprimento,largura)

print(f"A área do retangulo é: {area}")
    

