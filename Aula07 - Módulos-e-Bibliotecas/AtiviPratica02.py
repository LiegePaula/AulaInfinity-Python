""" Crie um módulo chamado manipulacao_strings que
contenha funções para realizar operações com strings,
como inverter uma string, contar o número de palavras
em uma string e verificar se uma string é um
palíndromo (lê-se igual de trás para frente). Crie
um programa principal que importe o módulo e use
essas funções com strings fornecidas pelo usuário. """

# programa_principal.py
import manipulacao_strings as ms

def menu():
    print("\n=== Manipulação de Strings ===")
    print("1 - Inverter string")
    print("2 - Contar palavras")
    print("3 - Verificar se é palíndromo")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando...")
        break

    texto = input("Digite a string: ")

    if opcao == "1":
        print("String invertida:", ms.inverter(texto))
    elif opcao == "2":
        print("Número de palavras:", ms.contar_palavras(texto))
    elif opcao == "3":
        if ms.eh_palindromo(texto):
            print("É um palíndromo!")
        else:
            print("Não é um palíndromo.")
    else:
        print("Opção inválida, tente novamente.")
