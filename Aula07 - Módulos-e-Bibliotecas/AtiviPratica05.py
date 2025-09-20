import conversoes

def menu():
    print("\n=== Conversor de Unidades ===")
    print("1 - Metros -> Pés")
    print("2 - Pés -> Metros")
    print("3 - Quilogramas -> Libras")
    print("4 - Libras -> Quilogramas")
    print("5 - Celsius -> Fahrenheit")
    print("6 - Fahrenheit -> Celsius")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando...")
        break

    try:
        valor = float(input("Digite o valor a converter: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if opcao == "1":
        print(f"{valor} m = {conversoes.metros_para_pes(valor):.2f} pés")
    elif opcao == "2":
        print(f"{valor} pés = {conversoes.pes_para_metros(valor):.2f} m")
    elif opcao == "3":
        print(f"{valor} kg = {conversoes.kg_para_libras(valor):.2f} lb")
    elif opcao == "4":
        print(f"{valor} lb = {conversoes.libras_para_kg(valor):.2f} kg")
    elif opcao == "5":
        print(f"{valor} °C = {conversoes.celsius_para_fahrenheit(valor):.2f} °F")
    elif opcao == "6":
        print(f"{valor} °F = {conversoes.fahrenheit_para_celsius(valor):.2f} °C")
    else:
        print("Opção inválida.")

