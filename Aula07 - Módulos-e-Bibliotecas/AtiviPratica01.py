""" 
Crie um programa que será uma calculadora.

Nesta calculadora você deverá ter um módulo para as
operações matemáticas, o arquivo principal deverá
conter apenas um menu de escolha para o usuário

(soma, subtração, multiplicação e divisão). """

# calculadora.py
import operacoes

def menu():
    print("==== CALCULADORA ====")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Saindo...")
        break

    if opcao in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            continue

        if opcao == "1":
            print("Resultado:", operacoes.soma(num1, num2))
        elif opcao == "2":
            print("Resultado:", operacoes.subtracao(num1, num2))
        elif opcao == "3":
            print("Resultado:", operacoes.multiplicacao(num1, num2))
        elif opcao == "4":
            print("Resultado:", operacoes.divisao(num1, num2))
    else:
        print("Opção inválida! Tente novamente.")
