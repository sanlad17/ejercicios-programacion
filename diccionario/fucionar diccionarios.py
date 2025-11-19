def fusionar_diccionarios():
    A = {'x': 1, 'y': 2}
    B = {'y': 10, 'z': 3}
    resultado = A.copy()
    resultado.update(B)
    print(resultado)

fusionar_diccionarios()