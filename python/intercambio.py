def intercambio():
    A = input('Ingrese el valor de A: ')
    B = input('Ingrese el valor de B: ')
    temporal = A
    A = B
    B = temporal
    print('Despues del intercambio')
    print(f'El valor de A es {A}')
    print(f'El valor de B es {B}')

# Ejecutar función
intercambio()