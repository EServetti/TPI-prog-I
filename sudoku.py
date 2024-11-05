import random
def sudoku ():
    class Sudoku:
        def __init__(self):
            self.tablero = [[0] * 9 for _ in range(9)]

        def mostrar(self):
            for fila in self.tablero:
                print(" ".join(str(num) if num != 0 else "." for num in fila))

        def es_valido(self, fila, col, num):
            # Comprobar fila
            if num in self.tablero[fila]:
                return False
            
            # Comprobar columna
            if num in [self.tablero[i][col] for i in range(9)]:
                return False
            
            # Comprobar cuadrante 3x3
            inicio_fila = (fila // 3) * 3
            inicio_col = (col // 3) * 3
            for i in range(inicio_fila, inicio_fila + 3):
                for j in range(inicio_col, inicio_col + 3):
                    if self.tablero[i][j] == num:
                        return False
            return True

        def resolver(self):
            for fila in range(9):
                for col in range(9):
                    if self.tablero[fila][col] == 0: 
                        for num in range(1, 10):  
                            if self.es_valido(fila, col, num):
                                self.tablero[fila][col] = num
                                if self.resolver():
                                    return True
                                self.tablero[fila][col] = 0
                        return False  
            return True 

        def generar(self):
            # Rellenar el tablero
            for i in range(9):
                for j in range(9):
                    num = random.randint(1, 9)
                    while not self.es_valido(i, j, num):
                        num = random.randint(1, 9)
                    self.tablero[i][j] = num

            # Remover algunos números para crear el Sudoku
            for _ in range(40):
                fila = random.randint(0, 8)
                col = random.randint(0, 8)
                while self.tablero[fila][col] == 0:
                    fila = random.randint(0, 8)
                    col = random.randint(0, 8)
                self.tablero[fila][col] = 0

    # Crear un Sudoku, mostrarlo y resolverlo
    sudoku = Sudoku()
    sudoku.generar()
    print("Sudoku generado:")
    sudoku.mostrar()

    if sudoku.resolver():
        print("\nSudoku resuelto:")
        sudoku.mostrar()
    else:
        print("\nNo se pudo resolver el Sudoku.")

sudoku()

        
        