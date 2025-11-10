import math

def uso_funciones():
    num = float(input('Ingrese su numero: '))
    seno = math.sin(num)
    coseno = math.cos(num)
    tangente = math.tan(num)
    raizc = math.sqrt(num)
    logaritmo_natural = math.log(num)
    
    print(f'El seno de su numero es {seno}')
    print(f'El coseno de su numero es {coseno}')
    print(f'La tangente de su numero es {tangente}')
    print(f'La raiz de su numero es {raizc}')
    print(f'El logaritmo de su numero es {logaritmo_natural}')

# Ejecutar función
uso_funciones()