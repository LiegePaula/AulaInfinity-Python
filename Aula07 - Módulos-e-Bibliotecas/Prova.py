""" [PYIA-A07] Crie uma função chamada lancar_dados que utilizará o módulo random para simular o lançamento de dois dados. Cada dado deve gerar um número aleatório entre 1 e 6. A função deve somar os resultados desses dois lançamentos e retornar o valor total. """

import random 

def lancar_dados():
    dado1 = random.randint(1, 6)  
    dado2 = random.randint(1, 6)  
    soma = dado1 + dado2
    return soma

resultado = lancar_dados()

print(f"O resultado do lançamento dos dados foi: {resultado}")