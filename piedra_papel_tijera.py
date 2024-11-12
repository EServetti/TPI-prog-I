import random
def jugar_piedra_papel_tijera():
    # Las opciones para jugar.
    opciones = ["piedra", "papel", "tijera"]
    # Ahora le pedimos al usuario su eleccion.
    print("Eleji entre: piedra, papel o tijera")
    jugador = input("Que vas a elegir?: ").lower()
    # Lo que hago aca es verificar que lo que eligio el jugador entre en la variable de las opciones.
    if jugador not in opciones:
        print("Opcion no valida. Tenes que elegir piedra, papel o tijera.")
        jugar_piedra_papel_tijera()
    else:
        # Aca basicamente hacemos que la computadora elija una opcion aleatoria entre piedra, papel y tijera.
        computadora = random.choice(opciones)
        print(f"La computadora eligio: {computadora}")
        # Ahora verificamos quien gano, si la computadora o el usuario.
        if jugador == computadora:
            print("Los dos eligieron lo mismo, empataron!")
        elif (jugador == "piedra" and computadora == "tijera") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijera" and computadora == "papel"):
            print("Le ganaste a la computadora!")
        else:
            print("La computadora te gano!")
        
        # Mediante est un while, le preguntamos al usuario si quiere jugar de nuevo, si escribe "no", lo saca automaticamente, si dice "si", el juego prosigue.
        repetir = input("Desea jugar de nuevo? (si/no): ").lower()
        while repetir not in ["si", "no"]:
            repetir = input("Por favor eliga entre si o no: ").lower()
        
        if repetir == "si":
            jugar_piedra_papel_tijera()
        else:
            print("Gracias por jugar!")

