def contador_palabras():
    frase = "hola mundo hola"
    palabras = frase.split()
    contador = {}
    for palabra in palabras:
        contador[palabra] = contador.get(palabra, 0) + 1
    print(contador)
contador_palabras()