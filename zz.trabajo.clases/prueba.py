def adivina_la_palabra():
    print("¡Bienvenido al juego de adivina la palabra!")

    palabra_secreta = "gordo"
    letras_adivinadas = ["_"] * len(palabra_secreta)
    intentos = 6

    while intentos > 0 and "_" in letras_adivinadas:
        print("\nPalabra actual: " + " ".join(letras_adivinadas))
        letra = input("Adivina una letra: ").lower()

        if letra in palabra_secreta:
            for i in range(len(palabra_secreta)): 
                if palabra_secreta[i] == letra:
                    letras_adivinadas[i] = letra
            print(f"¡Correcto! La letra '{letra}' está en la palabra.")
        else:
            intentos -= 1
            print(f"Incorrecto. Te quedan {intentos} intentos.")

    if "_" not in letras_adivinadas:
        print(f"¡Felicidades! Adivinaste la palabra: {palabra_secreta}")
    else:
        print(f"Perdiste. La palabra era: {palabra_secreta}")

adivina_la_palabra()
