Algoritmo calculoDescuento
	definir tipoarticulo como cadena 
	Definir descuento,precio,valordefinal Como Real
	Escribir "ingrese  su tipo de articulo (textil,electrodomestico,elementos de cocina ,videojuegos)"
	Leer tipoarticulo
	Escribir "ingrese el valor de su articulo"
	leer precio
	Segun tipoarticulo Hacer
			"textil":
			descuento=precio*0
			
		"electrodomestico":
			descuento=precio*0.37
			
		"elementos de cocina":
			descuento=precio*0.42
			
		"videojuegos":
			descuento=precio*0.78
			
		De Otro Modo:
			Escribir "tipo de articulo no valido "
			
	FinSegun
	valordefinal= precio - descuento
	Escribir "precio original " "$" precio
	Escribir "su descuento es de " "$" descuento
	Escribir "su precio final es de " "$" valordefinal 
FinAlgoritmo
