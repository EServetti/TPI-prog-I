from ahorcado import ahorcado
from buscaminas import buscaminas
from piedra_papel_tijera import jugar_piedra_papel_tijera
from quiz import cuestionario_prog
from sudoku import sudoku
from Tateti import jugar_tateti
from battleship2 import play_game


def menu():
    print("Bienvenido a nuestro sistema de juegos, seleccione el juego que desee jugar de la siguiente lista:")
    print("""
          1) Ahorcado
          2) Buscaminas
          3) Piedra Papel o Tijera
          4) Quiz
          5) Sudoku
          6) Ta-Te-Ti
          7) Batalla naval""")
    seguir_jugando = 1
    while seguir_jugando == 1:
        juego = int(input("Ingrese el juego que desea jugar (1/7) "))
        if juego not in range(1, 8):
            print("Debes ingresar un numero correspondiente a un juego (1/7)")
        elif juego == 1:
            ahorcado()
            seguir_jugando = int(input("Seguir jugando? 1: Si 0: No "))
        elif juego == 2:
            buscaminas()
            seguir_jugando = int(input("Seguir jugando? 1: Si 0: No "))
        elif juego == 3:
            jugar_piedra_papel_tijera()
            seguir_jugando = int(input("Seguir jugando? 1: Si 0: No "))
        elif juego == 4:
            cuestionario_prog()
            seguir_jugando = int(input("Seguir jugando? 1: Si 0: No "))
        elif juego == 5:
            sudoku()
            seguir_jugando = int(input("Seguir jugando? 1: Si 0: No "))
        elif juego == 6:
            jugar_tateti()
            seguir_jugando = int(input("Seguir jugando? 1: Si 0: No "))
        elif juego == 7:
            play_game()
            seguir_jugando = int(input("Seguir jugando? 1: Si 0: No "))
menu()