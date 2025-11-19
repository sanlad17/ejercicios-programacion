def maximo_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(f"Máximo de 3, 7, 2: {maximo_de_tres(3, 7, 2)}")