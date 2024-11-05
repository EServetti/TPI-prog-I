matriz = [[0 for columna in range(12)]for filas in range(6)] #en un rango de 12 columnas y 6 filas da valor a 0

for filas in range(6): #SIMPRE VA PRIMERO LA FILA Y DUESPUES LAS COLUMNAS
    for columnas in range(12): 
        matriz[filas][columnas] = str(filas) + str(columnas)
for filas in matriz: #cuando termina la fila, imprime otra debajo.
    print(filas)