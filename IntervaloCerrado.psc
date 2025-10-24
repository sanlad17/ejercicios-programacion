Algoritmo IntervaloCerradoCerrado
    Definir x, minimoValor, maximoValor Como Entero
    
    Escribir "VERIFICAR NÚMERO EN INTERVALO CERRADO-CERRADO [min, max]"
    Escribir "Ingrese el valor mínimo del intervalo:"
    Leer minimoValor
    
    Escribir "Ingrese el valor máximo del intervalo:"
    Leer maximoValor
    
    Escribir "Ingrese el número a verificar:"
    Leer x
    
    
    Si minimoValor > maximoValor Entonces
        Escribir "ERROR: El valor mínimo no puede ser mayor al máximo"
    Sino
        
        Si x >= minimoValor Y x <= maximoValor Entonces
            Escribir "El número ", x, " está DENTRO del intervalo [", minimoValor, ", ", maximoValor, "]"
        Sino
            Escribir "El número ", x, " está FUERA del intervalo [", minimoValor, ", ", maximoValor, "]"
        FinSi
    FinSi
	
FinAlgoritmo