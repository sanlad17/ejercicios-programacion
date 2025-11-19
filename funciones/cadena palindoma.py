def es_palindromo(cadena):
    cadena_limpia = ""
    for caracter in cadena:
        if caracter != " ":
            cadena_limpia = cadena_limpia + caracter.lower()
    return cadena_limpia == (cadena_limpia)
palabra = "Anita lava la tina"
print(f"¿'{palabra}' es palíndromo? {es_palindromo(palabra)}")