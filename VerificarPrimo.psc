Algoritmo VerificarPrimo
		Definir numero Como Entero
		Definir esPrimo Como Logico
		
		Escribir "Ingrese un número entre 0 y 20:"
		Leer numero
		
		
		Si numero < 0 O numero > 20 Entonces
			Escribir "Error: El número debe estar entre 0 y 20"
		Sino
			
			Segun numero Hacer
				2,3,5,7,11,13,17,19:
					esPrimo = Verdadero
				De Otro Modo:
					esPrimo = Falso
			FinSegun
			
			Si esPrimo Entonces
				Escribir numero, " es un número primo"
			Sino
				Escribir numero, " NO es un número primo"
			FinSi
		FinSi
FinAlgoritmo
