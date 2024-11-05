Algoritmo Numeros
	Definir edades, suma, i Como Entero;
	
	Definir prom Como Real;
	
	Dimension edades[5];
	
	Para i<-0 Hasta 4 Con Paso 1 Hacer 
		Leer edades[i];
	Fin Para
	
	
	Para i<-0 Hasta 4 Con Paso 1 Hacer 
		suma <- suma + edades[i];
	Fin Para
	
	promedio <- suma /5;
	Escribir promedio;
FinAlgoritmo
