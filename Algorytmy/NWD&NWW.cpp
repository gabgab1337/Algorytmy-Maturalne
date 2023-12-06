int NWD_iter(int a, int b){
    while(a != b){
        if(a > b)
            a -= b;
        else
            b -= a;
    }
    return a;
}

int NWD_rek(int a, int b){
    if(b == 0)
        return a;
    else
        return NWD_rek(b, a % b);
}

int NWW(int a, int b){
    return a * b / NWD_iter(a, b);
}