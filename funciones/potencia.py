def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / potencia(base, -exponente)
    
    resultado = 1
    for i in range(exponente):
        resultado = resultado * base
    return resultado
print(f"2^5 = {potencia(2, 5)}")
print(f"3^-2 = {potencia(3, -2)}")