print("Tipos de artículo:")
print("1. Textil")
print("2. Electrodoméstico")
print("3. Elementos de cocina")
print("4. Video juego")
tipo = int(input("Seleccione el tipo (1-4): "))
if tipo == 1:
    print("Descuento: 0%")
elif tipo == 2:
    print("Descuento: 3.7%")
elif tipo == 3:
    print("Descuento: 4.2%")
elif tipo == 4:
    print("Descuento: 7.8%")
else:
    print("Tipo no válido")