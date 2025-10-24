Algoritmo CalificacionEstudiante
    Definir trabajo1, trabajo2, trabajo3, trabajo4, trabajo5 Como Real
    Definir notaFinal Como Real
    
    Escribir "INGRESE LAS NOTAS DE LOS 5 TRABAJOS (0.0 - 5.0):"
    
    Escribir "Nota trabajo 1:"
    Leer trabajo1
    Escribir "Nota trabajo 2:"
    Leer trabajo2
    Escribir "Nota trabajo 3:"
    Leer trabajo3
    Escribir "Nota trabajo 4:"
    Leer trabajo4
    Escribir "Nota trabajo 5:"
    Leer trabajo5
    
    
    notaFinal = (trabajo1 + trabajo2 + trabajo3 + trabajo4 + trabajo5) / 5
    
    Escribir "Nota final: ", notaFinal
    
    Si notaFinal > 3.5 Entonces
        Escribir "RESULTADO: GANÓ EL CURSO"
    Sino
        Escribir "RESULTADO: PERDIÓ EL CURSO"
    FinSi
FinAlgoritmo