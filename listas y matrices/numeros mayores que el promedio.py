def mayores_que_promedio():
    numeros = list(map(int, input('ingrese numeros separados por espacios: ').split()))
    promedio = sum(numeros) / len(numeros)
    mayores = [num for num in numeros if num > promedio]
    print(f'promedio: {promedio}')
    print(f'mayores que el promedio: {sorted(mayores)}')
mayores_que_promedio()
