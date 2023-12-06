def NWD_iter(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def NWD_rek(a, b):
    if b == 0:
        return a
    else:
        return NWD_rek(b, a % b)
    
def NWW(a, b):
    return a * b / NWD_iter(a, b)