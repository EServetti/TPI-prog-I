import random
import math

def buscaminas():
    # Inicializar variables locales para filas, columnas y cantidad de minas
    filas = 0
    columnas = 0
    cantminas = 0

    # Función para ubicar minas en la matriz
    def ubicarminas():
        matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
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
    
    # Definir filas y columnas
    filas = int(input('⭑ Ingrese la cantidad de filas: '))
    if filas > 2:
        columnas = round((filas * 16) / 9)
    
    # Calcular cantidad de minas
    cantminas = math.ceil(filas * 2)
    print("\n⭑ Cantidad de minas generadas: ", cantminas)

    # Generar la matriz con minas
    k = ubicarminas()
    print("\nCarga completa! MODO DESACTIVACIÓN")
    
    # Definir el estado inicial del juego
    suma = sum([sum(fila) for fila in k])  # Total de minas sin desactivar
    matrizmostrar = [["☐" for _ in range(columnas)] for _ in range(filas)]
    
    # Bucle principal del juego
    while suma > 0:
        print("\n--- • Tablero {}x{} • ---".format(columnas, filas))
        for fila in matrizmostrar:
            print(" ".join(fila))
        
        # Solicitar coordenadas
        ubicacion_ataque = int(input("► Ingrese coordenadas de desactivación (ej. 123): "))
        
        # Extraer las coordenadas de entrada
        y = (ubicacion_ataque // 100) - 1
        x = ((ubicacion_ataque // 10) % 10) - 1
        t = ubicacion_ataque % 10
        
        # Verificar si la ubicación ya fue ingresada
        if ubicacion_ataque in ubic_ataque:
            print("↻ Ubicación ya ingresada.")
            continue
        
        ubic_ataque.append(ubicacion_ataque)
        
        # Si es una mina y se ha ingresado correctamente
        if k[x][y] == 1 and t == 1:
            print("✓ DESACTIVADA.")
            matrizmostrar[x][y] = "☒"
            suma -= 1
            print("╌ Minas sin desactivar: ", suma)
        else:
            print("✗ No hay mina en esta ubicación o el número de acción es incorrecto.")
    
    print("¡Felicidades, todas las minas han sido desactivadas!")

