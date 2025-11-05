def rectangulo():
    base = float(input('Ingrese la base de su rectangulo: '))
    altura = float(input('Ingrese la altura del rectangulo: '))
    area = base * altura
    perimetro = 2 * (base + altura)
    print(f'El area de su rectangulo es de {area}')
    print(f'El perimetro del rectangulo es {perimetro}')

# Ejecutar función
rectangulo()