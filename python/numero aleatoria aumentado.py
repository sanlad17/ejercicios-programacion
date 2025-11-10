import random

def numero_aleatorio_aumentado():
    num = random.randint(0, 200)
    print(f'El numero generado es {num}')
    aumento = num * 0.30
    resultado = num + aumento
    print(f'El numero aumentado en un 30% es {resultado}')

# Ejecutar función
numero_aleatorio_aumentado()