#Programa de piedra papel o tijera
import random


def piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    puntuacion_usuario = 0
    puntuacion_computadora = 0

    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    print("Escribe 'salir' para terminar el juego.")

    while True:
        eleccion_usuario = input("Elige piedra, papel o tijera: ").lower()

        if eleccion_usuario == "salir":
            print("Gracias por jugar. ¡Hasta luego!")
            break

        if eleccion_usuario not in opciones:
            print("Opción no válida. Intenta de nuevo.")
            continue

        eleccion_computadora = random.choice(opciones)
        print(f"La computadora eligió: {eleccion_computadora}")

        if eleccion_usuario == eleccion_computadora:
            print("¡Es un empate!")
        elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
             (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
             (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
            print("¡Ganaste esta ronda!")
            puntuacion_usuario += 1
        else:
            print("¡Perdiste esta ronda!")
            puntuacion_computadora += 1

        print(f"Puntuación - Tú: {puntuacion_usuario}, Computadora: {puntuacion_computadora}")
        print("-" * 30)
    print("¡Gracias por jugar! Aquí está el resultado final:")
    print(f"Puntuación final - Tú: {puntuacion_usuario}, Computadora: {puntuacion_computadora}")
# Llamar a la función para iniciar el juego
piedra_papel_tijera()
# Este código es un juego interactivo de Piedra, Papel o Tijera entre el usuario y la computadora.
# El usuario puede elegir entre las tres opciones y la computadora selecciona aleatoriamente una de ellas.
# El juego continúa hasta que el usuario decide salir escribiendo 'salir'.
# El programa lleva un registro de la puntuación del usuario y de la computadora, mostrando el resultado después de cada ronda.
# Al final, se muestra la puntuación final del usuario y de la computadora.
# El código utiliza la biblioteca random para generar la elección de la computadora y maneja entradas no válidas de manera efectiva.
# El juego es simple pero entretenido, y puede ser una buena manera de practicar la lógica de programación y el manejo de entradas del usuario.