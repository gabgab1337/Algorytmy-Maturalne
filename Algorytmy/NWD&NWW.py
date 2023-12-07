# Iteracyjny algorytm obliczania największego wspólnego dzielnika (NWD)
def NWD_iter(a, b):
    while b != 0:
        a, b = b, a % b  # Zastępuje a przez b, a b przez resztę z dzielenia a przez b
    return a  # Zwraca a (które jest NWD)

# Rekurencyjny algorytm obliczania największego wspólnego dzielnika (NWD)
def NWD_rek(a, b):
    if b == 0:
        return a  # Jeśli b jest zerem, zwraca a (ostatnie niezerowe a)
    else:
        return NWD_rek(b, a % b)  # W przeciwnym razie wywołuje rekurencyjnie dla (b, a % b)

# Funkcja obliczająca najmniejszą wspólną wielokrotność (NWW)
def NWW(a, b):
    return a * b / NWD_iter(a, b)  # Oblicza NWW za pomocą iteracyjnie lub rekurencyjnie obliczonego NWD