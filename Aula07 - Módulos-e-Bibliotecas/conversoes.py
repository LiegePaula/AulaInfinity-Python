# conversoes.py

# --- Comprimento ---
def metros_para_pes(metros: float) -> float:
    # 1 metro = 3.28084 pés
    return metros * 3.28084


def pes_para_metros(pes: float) -> float:
    return pes / 3.28084


# --- Peso ---
def kg_para_libras(kg: float) -> float:
    # 1 kg = 2.20462 libras
    return kg * 2.20462


def libras_para_kg(libras: float) -> float:
    return libras / 2.20462


# --- Temperatura ---
def celsius_para_fahrenheit(c: float) -> float:
    return (c * 9/5) + 32


def fahrenheit_para_celsius(f: float) -> float:
    return (f - 32) * 5/9
