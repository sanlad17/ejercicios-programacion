def temperatura():
    grados_celsius = float(input('Ingrese la temperatura en grados celsius: '))
    fahrenheit = 9/5 * grados_celsius + 32
    print(f'Su temperatura es de {fahrenheit}')

# Ejecutar función
temperatura()