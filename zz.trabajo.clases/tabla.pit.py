matriz = [10, 10]
for i in range (9):
    tabla = i + 1 
    for j in range (9): 
        multiplo = j + 1
        multiplicacion = tabla*multiplo
        matriz[i,j] = multiplicacion
print(matriz)