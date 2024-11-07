
def cuestionario_prog():
    nombre_usuario = input("Ingrese su nombre: ")
    preguntas = {
        "¿Cuál es la capital de Francia?": "3",
        "¿Cuántos continentes hay en el mundo?": "2",
        "¿Cuál de estos es un lenguaje de programación?": "2",
        "¿Para que sirve print en python?": "3",
        "¿Que jugador marco goles en el mundial de 2022?": "4"
    }

   #preguntas y opciones.
    opciones = {
        "¿Cuál es la capital de Francia?": ["1) Berlín", "2) Madrid", "3) París", "4) Ninguna es correcta"],
        "¿Cuántos continentes hay en el mundo?": ["1) 5", "2) 7", "3) 6"],
        "¿Cuál de estos es un lenguaje de programación?": ["1) HTML", "2) Python", "3) CSS"],
        "¿Para que sirve print en python?": ["1) Definir una variable", "2) Guardar un archivo", "3) Mostrar un mensaje en consola"],
        "¿Que jugador marco goles en el mundial de 2022?": ["1) L. Messi", "2) A. Gomez", "3) J. Alvarez", "4) 1 y 3"]
    }
#puntuacion con la que arranca.
    puntuacion = 0

    print(nombre_usuario+ " bienvenido a este mini-cuestionario de preguntas faciles")
    
    for pregunta in preguntas: #es un conjunto que representan las claves del conjunto
        print("\n" + pregunta)
        for opcion in opciones[pregunta]:
            print(opcion)

        respuesta = input(nombre_usuario+ " seleccione la respuesta correcta: ").lower()
        
        if respuesta == preguntas[pregunta]:
            #si la opcion es igual a la que indicaba arriba muestra: 
            print("¡Correcto!")
            puntuacion += 1
        else:
            print("Incorrecto. La respuesta correcta era la opcion: {}".format(preguntas[pregunta]))
    print(nombre_usuario+ " tu puntuacion final es: " + str(puntuacion)+"/"+str(len(preguntas)))

