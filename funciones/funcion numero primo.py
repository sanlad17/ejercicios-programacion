def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor = divisor + 2
    return True
numero = 17
print(f"¿{numero} es primo? {es_primo(numero)}")