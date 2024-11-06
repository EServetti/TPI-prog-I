import random
def sudoku():
    def print_board(board):
        for row in board:
            print(" ".join(str(num) if num != 0 else "." for num in row))

    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def fill_board(board):
        for _ in range(20):
            row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
            while not is_valid(board, row, col, num) or board[row][col] != 0:
                row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
            board[row][col] = num

    def play_sudoku():
        # Crear un tablero vacío
        board = [[0 for _ in range(9)] for _ in range(9)]
        fill_board(board)

        while True:
            print("\nTablero actual:")
            print_board(board)

            try:
                move = input("Ingrese su jugada en formato 'fila(0-8) col(0-8) num(1-9)' (o 'salir' para terminar): ")
                if move.lower() == 'salir':
                    print("Gracias por jugar. ¡Hasta luego!")
                    break
                
                row, col, num = map(int, move.split())
                if is_valid(board, row, col, num):
                    board[row][col] = num
                else:
                    print("Movimiento no válido. Intente de nuevo.")
            
                if all(all(cell != 0 for cell in row) for row in board):
                    print("\n¡Felicidades! Has resuelto el Sudoku:")
                    print_board(board)
                    break

            except ValueError:
                print("Entrada no válida. Asegúrate de ingresar tres números separados por espacios.")

    # Permitir jugar múltiples partidas
    while True:
        play_sudoku()
        again = input("\n¿Quieres jugar otra vez? (si/no): ")
        if again.lower() != 'si':
            print("Gracias por jugar. ¡Hasta luego!")
            break
sudoku()        
