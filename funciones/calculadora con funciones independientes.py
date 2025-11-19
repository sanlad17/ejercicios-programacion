def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"
def calculadora():
    print("Calculadora")
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")
    if operacion == "+":
        resultado = sumar(a, b)
    elif operacion == "-":
        resultado = restar(a, b)
    elif operacion == "*":
        resultado = multiplicar(a, b)
    elif operacion == "/":
        resultado = dividir(a, b)
    else:
        resultado = "Operación no válida"
    print(f"Resultado: {resultado}")
calculadora()