// Algorytm iteracyjny obliczania największego wspólnego dzielnika (NWD)
int NWD_iter(int a, int b){
    while(a != b){
        if(a > b)
            a -= b; // Jeśli a > b, odejmujemy b od a
        else
            b -= a; // W przeciwnym razie odejmujemy a od b
    }
    return a; // Zwracamy a (które jest NWD)
}

// Algorytm rekurencyjny obliczania największego wspólnego dzielnika (NWD)
int NWD_rek(int a, int b){
    if(b == 0)
        return a; // Jeśli b jest zerem, zwracamy a (ostatnie niezerowe a)
    else
        return NWD_rek(b, a % b); // W przeciwnym razie wywołujemy rekurencyjnie dla (b, a % b)
}

// Funkcja obliczająca najmniejszą wspólną wielokrotność (NWW)
int NWW(int a, int b){
    return a * b / NWD_iter(a, b); // Obliczamy NWW za pomocą iteracyjnie lub rekurencyjnie obliczonego NWD
}