Algoritmo descuentoArticulo
	definir costoArticulo, descuento, precioFinal Como Real
	Escribir 'ingrese el costo'
	leer costoArticulo
	si costoArticulo > 150000 Entonces
		descuento = costoArticulo * 0.05
		precioFinal = costoArticulo - descuento
		Escribir ' se aplica descuento del 5%: ' descuento
		Escribir ' precio final: ' precioFinal
	SiNo
		Escribir 'no aplica descuento,precio: ' costoArticulo
	FinSi
	
FinAlgoritmo
