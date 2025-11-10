import math

def hipotenusa():
    cateto1 = float(input('Ingrese el valor del primer cateto: '))
    cateto2 = float(input('Ingrese el valor del segundo cateto: '))
    hipotenus = math.sqrt((cateto1**2) + (cateto2**2))
    print(f'La hipotenusa del triangulo es de {hipotenus}')

# Ejecutar función
hipotenusa()