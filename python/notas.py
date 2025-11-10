def nota_asignatura():
    nota1 = float(input('Ingrese el primer valor: '))
    nota2 = float(input('Ingrese el segundo valor: '))
    nota3 = float(input('Ingrese el tercer valor: '))
    nota4 = float(input('Ingrese su cuarto valor: '))
    definitiva = (nota1 + nota2 + nota3 + nota4) / 4
    print(f'Su definitiva es {definitiva}')

# Ejecutar función
nota_asignatura()