""" Crie um programa que permite ao usuário calcular a
área e operímetro de formas geométricas simples,
como quadrados, retângulos e círculos. Use funções
matemáticas do módulo math para realizar os cálculos. """

import math
import geometria

def menu():
    print("\n=== Cálculo de Área e Perímetro ===")
    print("1 - Quadrado")
    print("2 - Retângulo")
    print("3 - Círculo")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma forma geométrica: ")

    if opcao == "0":
        print("Encerrando...")
        break

    try:
        if opcao == "1":  # Quadrado
            lado = float(input("Digite o lado do quadrado: "))
            print(f"Área: {geometria.area_quadrado(lado):.2f}")
            print(f"Perímetro: {geometria.perimetro_quadrado(lado):.2f}")

        elif opcao == "2":  # Retângulo
            base = float(input("Digite a base do retângulo: "))
            altura = float(input("Digite a altura do retângulo: "))
            print(f"Área: {geometria.area_retangulo(base, altura):.2f}")
            print(f"Perímetro: {geometria.perimetro_retangulo(base, altura):.2f}")

        elif opcao == "3":  # Círculo
            raio = float(input("Digite o raio do círculo: "))
            print(f"Área: {geometria.area_circulo(raio):.2f}")
            print(f"Perímetro (circunferência): {geometria.perimetro_circulo(raio):.2f}")

        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
