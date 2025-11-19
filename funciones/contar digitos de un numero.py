def contar_digitos(n):
    if n == 0:
        return 1
    if n < 0:
        n = -n
    contador = 0
    while n > 0:
        contador = contador + 1
        n = n // 10
    return contador
numero = 12345
print(f"Dígitos en {numero}: {contar_digitos(numero)}")