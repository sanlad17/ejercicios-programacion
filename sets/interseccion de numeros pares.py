def interseccion_pares():
    A = [2, 4, 6, 8]
    B = [4, 5, 6, 9]
    pares_A = {num for num in A if num % 2 == 0}
    pares_B = {num for num in B if num % 2 == 0}
    interseccion = pares_A & pares_B
    print(interseccion)
interseccion_pares()