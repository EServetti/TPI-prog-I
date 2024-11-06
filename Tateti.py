import pygame
import time
import os

def jugar_tateti():
    pygame.init()
    pantalla = pygame.display.set_mode((450, 450))
    pygame.display.set_caption("Ta te ti")

    # Se cargan las imagenes para la interfaz
    fondo = pygame.image.load("imagenes/fondo.png")
    circle = pygame.image.load("imagenes/circle.png")
    equis = pygame.image.load("imagenes/x.png")
    fondo = pygame.transform.scale(fondo, (450, 450))
    circle = pygame.transform.scale(circle, (125, 125))
    equis = pygame.transform.scale(equis, (125, 125))

    # Coordenadas para mostrar "X" y "O"
    coor = [[(40, 50), (165, 50), (290, 50)],
            [(40, 175), (165, 175), (290, 175)],
            [(40, 300), (165, 300), (290, 300)]]

    # Tablero de juego
    tablero = [["", "", ""],
               ["", "", ""],
               ["", "", ""]]

    Turno = "X"
    juego_terminado = False
    clock = pygame.time.Clock()

    # Ruta del archivo
    contador_file = "contador_partidas.txt"

    # Se reinicia el contador de victorias y derrotas al abrir el juego
    with open(contador_file, "w") as f:
        f.write("X:0\nO:0\n")

    def actualizar_contador(ganador):
        # Se lee el archivo y se actualiza
        with open(contador_file, "r") as f:
            data = f.readlines()

        # Extrae las victorias de cada jugador
        victorias = {"X": int(data[0].split(":")[1]), "O": int(data[1].split(":")[1])}
        victorias[ganador] += 1

        # Guarda el nuevo contador en el archivo
        with open(contador_file, "w") as f:
            f.write(f"X:{victorias['X']}\nO:{victorias['O']}\n")

    def obtener_victorias():
        # Lee el archivo y se obtienen las victorias de cada jugador
        with open(contador_file, "r") as f:
            data = f.readlines()
        victorias = {"X": int(data[0].split(":")[1]), "O": int(data[1].split(":")[1])}
        return victorias

    def mostrar_victorias():
        # Se muestran las victorias de cada jugador
        victorias = obtener_victorias()
        fuente = pygame.font.Font(None, 36)  # Fuente utilizada para el contador
        
        # Se ajustan la posición del texto de los contadores
        texto_x = fuente.render(f"Victorias X: {victorias['X']}", True, (255, 0, 0))
        texto_o = fuente.render(f"Victorias O: {victorias['O']}", True, (0, 0, 255))
        
        # Se Posicionan ambos textos
        pantalla.blit(texto_x, (10, 10))  # Posición del texto de X
        pantalla.blit(texto_o, (220, 10))  # Posición del texto de O
    def mostrar_pregunta_volver_a_jugar():
        # Se muestra una ventana emergente para preguntar si desea volver a jugar
        fuente = pygame.font.Font(None, 36)
        texto_pregunta = fuente.render("¿Quieres volver a jugar?", True, (0, 0, 0))
        texto_si = fuente.render("Sí", True, (0, 255, 0))
        texto_no = fuente.render("No", True, (255, 0, 0))

        # Posiciones para el texto
        pantalla.fill((255, 255, 255))  # Fondo blanco
        pantalla.blit(texto_pregunta, (80, 150))
        pantalla.blit(texto_si, (150, 250))
        pantalla.blit(texto_no, (250, 250))
        pygame.display.update()

        # Espera la respuesta del usuario
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False  # Cerrar el juego
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 150 <= x <= 200 and 250 <= y <= 280:  # Opción "Sí"
                        return True
                    elif 250 <= x <= 300 and 250 <= y <= 280:  # Opción "No"
                        return False

    def graficar_board():
        pantalla.blit(fondo, (0, 0))
        for fila in range(3):
            for col in range(3):
                if tablero[fila][col] == "X":
                    dibujar_x(fila, col)
                elif tablero[fila][col] == "O":
                    dibujar_O(fila, col)
        mostrar_victorias()  # Mostrar victorias cada vez que se grafica el tablero

    def dibujar_x(fila, col):
        pantalla.blit(equis, coor[fila][col])

    def dibujar_O(fila, col):
        pantalla.blit(circle, coor[fila][col])

    def comprobar_ganador():
        for i in range(3):
            if tablero[i][0] == tablero[i][1] == tablero[i][2] != "":
                return True
            if tablero[0][i] == tablero[1][i] == tablero[2][i] != "":
                return True
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != "":
            return True
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != "":
            return True
        return False

    def comprobar_empate():
        for fila in tablero:
            if "" in fila:
                return False
        return True

    while True:
        juego_terminado = False
        while not juego_terminado:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = event.pos
                    if (mouseX >= 40 and mouseX < 415) and (mouseY >= 50 and mouseY < 425):
                        fila = (mouseY - 50) // 125
                        col = (mouseX - 40) // 125
                        if tablero[fila][col] == "":
                            tablero[fila][col] = Turno
                            fin_del_juego = comprobar_ganador()
                            empate = comprobar_empate()

                            if fin_del_juego:
                                print(f"El jugador {Turno} ha ganado")
                                actualizar_contador(Turno)  # Actualiza el contador de victorias
                                graficar_board()
                                pygame.display.update()
                                time.sleep(2)
                                juego_terminado = True
                            elif empate:
                                print("¡Empate! Reiniciando el juego...")
                                tablero = [["", "", ""],
                                           ["", "", ""],
                                           ["", "", ""]]
                                Turno = "X"
                            else:
                                Turno = "O" if Turno == "X" else "X"

            graficar_board()
            pygame.display.update()

        # Se pregunta si desea volver a jugar
        if not mostrar_pregunta_volver_a_jugar():
            break  # Sale del bucle principal y se cierra el juego

        # Reinicia el tablero y el turno si el usuario quiere volver a jugar
        tablero = [["", "", ""],
                   ["", "", ""],
                   ["", "", ""]]
        Turno = "X"

    pygame.quit()

jugar_tateti()
