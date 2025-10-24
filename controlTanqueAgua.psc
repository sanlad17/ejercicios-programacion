Algoritmo controlTanqueAgua
	Definir nivelAgua Como Real
	Escribir 'ingrese el nivel actual de agua en litros'
	leer nivelAgua
	si nivelAgua >= 250 y nivelAgua <= 450 Entonces
		Escribir 'mantener llave cerrada'
	sino
		si nivelAgua < 250 Entonces
			Escribir 'abrir llave'
		SiNo
			Escribir 'cerrar llave'
		FinSi
	FinSi
	
	
FinAlgoritmo
