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

def kuadrat(a):
    return a * a

def bagi_bulat(a, b):
    if b == 0:
        raise ValueError("pembagi nol")
    return a // b

def modulo(a, b):
    if b == 0:
        raise ValueError("pembagi nol")
    return a % b

def rata_rata(daftar):
    if not daftar:
        raise ValueError("daftar kosong")
    return sum(daftar) / len(daftar)

def faktorial(n):
    if n < 0:
        raise ValueError("n negatif")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
