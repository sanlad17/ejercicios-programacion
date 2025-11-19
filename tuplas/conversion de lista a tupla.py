def lista_a_tupla_sin_duplicados():
    lista = input('ingrese elementos separados por espacios: ').split()
    tupla_sin_duplicados = tuple(set(lista))
    print(tupla_sin_duplicados)
lista_a_tupla_sin_duplicados()