def conversion_de_centimetros():
    cm = float(input("Ingrese la cantidad en centímetros: "))
    
    metros = cm / 100
    yardas = cm / 91.44
    pies = cm / 30.48
    pulgadas = cm / 2.54
    
    print("Equivale a:")
    print(f"{metros} metros")
    print(f"{yardas} yardas")
    print(f"{pies} pies")
    print(f"{pulgadas} pulgadas")

# Ejecutar función
conversion_de_centimetros()