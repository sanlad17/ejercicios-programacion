import random

def numero_aleatorio_disminuido():
    num = random.randint(10, 50)
    print(f'El numero generado es {num}')
    disminucion = num * 0.15
    resultado = num - disminucion
    print(f'El numero disminuido en un 15% es {resultado}')

# Ejecutar función
numero_aleatorio_disminuido()