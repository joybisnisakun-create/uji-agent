def bagi(a, b):
    if b == 0:
        raise ValueError("pembagi nol")
    return a / b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def pangkat(a, b):
    return a ** b

def bagi_bulat(a, b):
    if b == 0:
        raise ValueError("pembagi nol")
    return a // b

def modulo(a, b):
    if b == 0:
        raise ValueError("pembagi nol")
    return a % b
