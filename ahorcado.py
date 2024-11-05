import random
# Lista de posibles palabras.
palabras = ["programacion","codigo","universidad","estudio","algoritmo"]
# Sortea una palabra de la lista para usar en el juego.
palabra = palabras[random.randint(0, len(palabras) -1)]
def ahorcado(palabra):
    incognita = []
    letras = []
    for l in palabra:
        incognita.append("_")
    vidas = 6
    ahorcado_dibujos = [
    r"""
       ___
      |   |
          |
          |
          |
          |
    ---------
    """,
    r"""
       ___
      |   |
      O   |
          |
          |
          |
    ---------
    """,
    r"""
       ___
      |   |
      O   |
      |   |
          |
          |
    ---------
    """,
    r"""
       ___
      |   |
      O   |
     /|   |
          |
          |
    ---------
    """,
    r"""
       ___
      |   |
      O   |
     /|\  |
          |
          |
    ---------
    """,
    r"""
       ___
      |   |
      O   |
     /|\  |
     /    |
          |
    ---------
    """,
    r"""
       ___
      |   |
      O   |
     /|\  |
     / \  |
          |
    ---------
    """
    ]
    while vidas > 0:
      if vidas == 6:
        dibujo = ahorcado_dibujos[0]
      elif vidas == 5:
        dibujo = ahorcado_dibujos[1]
      elif vidas == 4:
        dibujo = ahorcado_dibujos[2]
      elif vidas == 3:
        dibujo = ahorcado_dibujos[3]
      elif vidas == 2:
        dibujo = ahorcado_dibujos[4]
      elif vidas == 1:
        dibujo = ahorcado_dibujos[5]
      else:
        dibujo = ahorcado_dibujos[6]
      if not "_" in incognita:
         print("Felicitaciones, ganaste!")
         break
      else: 
        print(dibujo + " ".join(incognita) + "   Letras usadas: " + ", ".join(letras))
        letra = input("Ingrese la siguiente letra: ")
        
        if not letra.isalpha():
           print("Debes ingresar una letra!")
        elif letra in letras: 
           print("Ya usaste esta letra!")
        else:
          letras.append(letra)
          if letra in palabra:
              contador = 0
              for l in palabra:
                  if l == letra:
                      incognita[contador] = letra
                  contador = contador + 1
          else:
              vidas = vidas - 1
              print("La letra "+ letra+ " no está en la palabra.")
    if vidas == 0:
      print(ahorcado_dibujos[6], "Juego terminado, perdiste.")
                            
ahorcado(palabra)
