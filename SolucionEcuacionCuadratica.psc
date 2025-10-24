Algoritmo SolucionEcuacionCuadratica
    Definir a, b, c, discriminante Como Real
    
    Escribir "ECUACIÓN CUADRÁTICA: ax² + bx + c = 0"
    Escribir "Ingrese los coeficientes:"
    
    Escribir "a = "
    Leer a
    
    Escribir "b = "
    Leer b
    
    Escribir "c = "
    Leer c
    
    
    discriminante <- b^2 - 4*a*c
    
    
    Si a = 0 Entonces
        Escribir "NO es una ecuación cuadrática (a no puede ser cero)"
    Sino
        Si discriminante >= 0 Entonces
            Escribir "La ecuación cuadrática SÍ tiene solución real"
            Escribir "Discriminante: ", discriminante
        Sino
            Escribir "La ecuación cuadrática NO tiene solución real"
            Escribir "Discriminante negativo: ", discriminante
        FinSi
    FinSi
FinAlgoritmo