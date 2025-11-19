def invertir(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return cadena[-1] + invertir(cadena[:-1])
texto = "hola"
print(f"'{texto}' invertido: '{invertir(texto)}'")