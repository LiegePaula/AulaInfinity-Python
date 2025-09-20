# manipulacao_strings.py

def inverter(texto: str) -> str:
    """Retorna a string invertida."""
    return texto[::-1]


def contar_palavras(texto: str) -> int:
    """Conta quantas palavras existem na string."""
    # Divide por espaços, ignorando espaços extras
    return len(texto.split())


def eh_palindromo(texto: str) -> bool:
    """
    Verifica se a string é um palíndromo.
    Ignora maiúsculas, minúsculas e espaços.
    """
    texto_limpo = "".join(ch.lower() for ch in texto if ch.isalnum())
    return texto_limpo == texto_limpo[::-1]
