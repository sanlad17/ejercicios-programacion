Algoritmo DentroFueraTresIntervalosAbiertos
    Definir min1, max1, min2, max2, min3, max3, x Como Entero
    Definir dentro Como Logico
    
    Escribir "PRIMER INTERVALO ABIERTO "
    Escribir "Ingrese límite inferior:"
    Leer min1
    Escribir "Ingrese límite superior:"
    Leer max1
    
    Escribir "SEGUNDO INTERVALO ABIERTO "
    Escribir "Ingrese límite inferior:"
    Leer min2
    Escribir "Ingrese límite superior:"
    Leer max2
    
    Escribir "TERCER INTERVALO ABIERTO"
    Escribir "Ingrese límite inferior:"
    Leer min3
    Escribir "Ingrese límite superior:"
    Leer max3
    
    Escribir "Ingrese el valor x a verificar:"
    Leer x
    
    
    dentro = (x > min1 Y x < max1) O (x > min2 Y x < max2) O (x > min3 Y x < max3)
    
    Si dentro Entonces
        Escribir "El valor ", x, " está DENTRO de al menos uno de los intervalos abiertos"
    Sino
        Escribir "El valor ", x, " está FUERA de todos los intervalos abiertos"
    FinSi
FinAlgoritmo