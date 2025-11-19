def mcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
def mcm(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    return (a * b) // mcd(a, b)
a, b = 12, 18
print(f"MCD de {a} y {b}: {mcd(a, b)}")
print(f"MCM de {a} y {b}: {mcm(a, b)}")