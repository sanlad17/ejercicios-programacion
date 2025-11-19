def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado
numero = 5
print(f"Factorial de {numero}: {factorial(numero)}")