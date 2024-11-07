import random

# Definir los niveles de juego
LEVELS = {
    1: {'size': 6, 'ships': [5, 4, 3]},
    2: {'size': 7, 'ships': [5, 4]},
    3: {'size': 8, 'ships': [5, 4, 3]},
    4: {'size': 9, 'ships': [5, 4, 3, 2]}
}

# Definir los símbolos de los barcos
SHIP_SYMBOLS = ['P', 'B', 'D', 'S', 'R']

# Crear el tablero vacío
def create_board(size):
    return [['O' for _ in range(size)] for _ in range(size)]

# Colocar los barcos de forma aleatoria en el tablero de la computadora
def place_ships(board, ship_sizes, ship_symbols):
    ship_positions = []
    for size, symbol in zip(ship_sizes, ship_symbols):
        for _ in range(size):
            x = random.randint(0, len(board) - 1)
            y = random.randint(0, len(board) - 1)
            while (x, y) in ship_positions:
                x = random.randint(0, len(board) - 1)
                y = random.randint(0, len(board) - 1)
            board[x][y] = symbol
            ship_positions.append((x, y))
    return board

# Mostrar el tablero del jugador
def display_player_board(board):
    print("Tu tablero:")
    for row in board:
        print(' '.join(row))
    print()

# Obtener la entrada del jugador
def get_player_shot(board):
    while True:
        try:
            x = int(input("Ingresa la fila (0-9): "))
            y = int(input("Ingresa la columna (0-9): "))
            if 0 <= x < len(board) and 0 <= y < len(board):
                return x, y
            else:
                print("Coordenadas inválidas. Intenta de nuevo.")
        except ValueError:
            print("Ingresa un número válido. Intenta de nuevo.")

# Actualizar el tablero del jugador después de un disparo
def update_player_board(board, x, y, result):
    board[x][y] = result
    return board

# Juego principal
def play_game():
    print("Niveles de juego:")
    for level, info in LEVELS.items():
        print(f"Nivel {level}: Tablero de {info['size']}x{info['size']} y barcos de tamaños {', '.join(map(str, info['ships']))}")
    print(f"Barcos disponibles: {', '.join(SHIP_SYMBOLS)}")

    level = int(input("Elige el nivel de juego (1-4): "))
    if level not in LEVELS:
        print("Nivel inválido. Intenta de nuevo.")
        return

    board_size = LEVELS[level]['size']
    ship_sizes = LEVELS[level]['ships']
    player_board = create_board(board_size)
    computer_board = place_ships(create_board(board_size), ship_sizes, SHIP_SYMBOLS[:len(ship_sizes)])
    player_score = 0
    ships_left = sum(ship_sizes)

    while ships_left > 0 and player_score < 100:
        display_player_board(player_board)
        print(f"Puntuación: {player_score}")

        player_shot_x, player_shot_y = get_player_shot(player_board)
        if any(computer_board[player_shot_x][player_shot_y] == symbol for symbol in SHIP_SYMBOLS):
            print("¡Impacto! Has hundido un barco.")
            player_score -= 20
            for symbol in SHIP_SYMBOLS:
                if computer_board[player_shot_x][player_shot_y] == symbol:
                    computer_board[player_shot_x][player_shot_y] = 'X'
                    ships_left -= 1
                    break
            player_board = update_player_board(player_board, player_shot_x, player_shot_y, 'X')
        else:
            print("Fallaste. Intenta de nuevo.")
            player_score += 5
            player_board = update_player_board(player_board, player_shot_x, player_shot_y, 'M')

    if player_score >= 100:
        print("¡Felicidades, has ganado el juego!")
    else:
        print("¡Has perdido el juego!")
    print(f"Tu puntuación final es: {player_score}")


