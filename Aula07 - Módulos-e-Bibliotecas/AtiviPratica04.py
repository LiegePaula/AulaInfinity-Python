import random

def jogo():
    print("=== Jogo de Adivinhação ===")
    print("Estou pensando em um número entre 1 e 100.")
    
    numero_secreto = random.randint(1, 100)  # sorteia um inteiro de 1 a 100
    tentativas = 0

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Por favor, digite apenas números inteiros.")
            continue

        tentativas += 1

        if palpite < numero_secreto:
            print("Tente um número MAIOR.")
        elif palpite > numero_secreto:
            print("Tente um número MENOR.")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativa(s).")
            break

if __name__ == "__main__":
    jogo()
