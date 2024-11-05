Algoritmo Restaurant
	Definir valoraciones, i, cant, suma Como Entero;
	
	Definir prom Como Real;
	
	suma = 0
	
	Dimension valoraciones[15]
	Dimension cant[10]
	
	Para i<-0 Hasta 14 Con Paso 1 Hacer //le suma una posicion a la "i"
		Escribir "Ingrese la valoracion "
		leer valoraciones[i] //lo que se lee se le asigna a la posicion en la que esta en ese momento en "i"
		cant[valoraciones[i] - 1] = cant[valoraciones[i] -1] +1
		suma = suma + valoraciones[i]
	FinPara
	
	prom = suma / 15
	
	Escribir "El promedio de valoracion es: " + ConvertirATexto(prom)
	Escribir "La cantidad de empleados que votaron 1 es: " + ConvertirATexto(cant[0])
	Escribir "La cantidad de empleados que votaron 2 es: " + ConvertirATexto(cant[1])
	Escribir "La cantidad de empleados que votaron 3 es: " + ConvertirATexto(cant[2])
	Escribir "La cantidad de empleados que votaron 4 es: "+ ConvertirATexto(cant[3])
	Escribir "La cantidad de empleados que votaron 5 es: "+ ConvertirATexto(cant[4])
	Escribir "La cantidad de empleados que votaron 6 es: "+ ConvertirATexto(cant[5])
	Escribir "La cantidad de empleados que votaron 7 es: "+ ConvertirATexto(cant[6])
	Escribir "La cantidad de empleados que votaron 8 es: "+ ConvertirATexto(cant[7])
	Escribir "La cantidad de empleados que votaron 9 es: "+ ConvertirATexto(cant[8])
	Escribir "La cantidad de empleados que votaron 10 es: "+ ConvertirATexto(cant[9])
	
FinAlgoritmo
