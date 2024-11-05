import random
import math
# Inicializar variables globales para filas, columnas y cantidad de minas
filas = 0
columnas = 0
cantminas = 0
# Función para ubicar minas en la matriz
def ubicarminas():
    # Crear la matriz vacía
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    # Colocar minas aleatoriamente
    for _ in range(cantminas):
        mina_colocada = False
        while not mina_colocada:
            a = random.randint(0, filas - 1)
            b = random.randint(0, columnas - 1)
            if matriz[a][b] != 1:  # Verificar si no hay mina
                matriz[a][b] = 1   # Colocar mina
                mina_colocada = True
    return matriz
# Inicializar juego
ubic_ataque = []
print("╌╌╌ • BUSCAMINAS • ╌╌╌")
filas = int(input('⭑ Ingrese la cantidad de filas: '))
if filas > 2:
    columnas = round((filas * 16) / 9)
# Definir el estado inicial del juego
minasdesactivadas = True
cantdesac = 0
matrizmostrar = [["☐" for _ in range(columnas)] for _ in range(filas)]
# Calcular la cantidad de minas
cantminas = math.ceil(filas * 2)
print("\n⭑ Cantidad de minas generadas: ", cantminas)
# Generar la matriz con minas
k = ubicarminas()
print("\nCarga completa! MODO DESACTIVACIÓN")
# Calcular el total de minas sin desactivar
suma = sum([sum(fila) for fila in k])
# Bucle principal del juego
while suma > 0:
    print("\n--- • Tablero {}x{} • ---".format(columnas, filas))
    for fila in matrizmostrar:
        print(" ".join(fila))
    
    ubicacion_ataque = int(input("► Ingrese coordenadas de desactivación (ej. 123): "))
    # Extraer las coordenadas a partir de la entrada
    y = (ubicacion_ataque // 100) - 1
    x = ((ubicacion_ataque // 10) % 10) - 1
    t = ubicacion_ataque % 10
    # Verificar si ya se ha ingresado esta ubicación
    if ubicacion_ataque in ubic_ataque:
        print("↻ Ubicación ya ingresada.")
        continue
    ubic_ataque.append(ubicacion_ataque)
    # Si la ubicación es de desactivación de mina y hay una mina
    if k[x][y] == 1 and t == 1:
        print("✓ DESACTIVADA.")
        matrizmostrar[x][y] = "☒"
        suma -= 1
        print("╌ Minas sin desactivar: ", suma)