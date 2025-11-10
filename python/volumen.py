import math

def volumen():
    radio = float(input('Ingrese el radio de su figura: '))
    altura = float(input('Ingrese la altura del cilindro: '))
    volume = math.pi * radio**2 * altura
    print(f'El volumen del cilindro es de {volume}')

# Ejecutar función
volumen()