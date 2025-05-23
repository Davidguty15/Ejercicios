#Realizar un programa que adivine un número entre 1 y 100, el usuario tiene 10 intentos para adivinar el número.
import random

def adivinar():
    numero_secreto = random.randint(1, 100)
    intentos = 10
    print("Bienvenido al juego de adivinar el número!")
    print("He elegido un número entre 1 y 100. Tienes 10 intentos para adivinarlo.")

    while intentos > 0:
        try:
            adivina = int(input(f"Tienes {intentos} intentos restantes. ¿Cuál es tu adivinanza? "))
            if adivina < 1 or adivina > 100:
                print("Por favor, elige un número entre 1 y 100.")
                continue
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        if adivina < numero_secreto:
            print("Demasiado bajo.")
        elif adivina > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Felicidades! Has adivinado el número {numero_secreto} correctamente.")
            break

        intentos -= 1

    if intentos == 0:
        print(f"Lo siento, has agotado tus intentos. El número era {numero_secreto}.") 
        print("¡Gracias por jugar!")

adivinar()
# Este código es un juego simple de adivinanza de números. El usuario tiene 10 intentos para adivinar un número aleatorio entre 1 y 100.
# El programa proporciona pistas sobre si la adivinanza es demasiado alta o baja. Si el usuario adivina correctamente, se le felicita y se termina el juego.
# Si el usuario agota sus intentos, se le revela el número secreto y se termina el juego.
# El código maneja entradas no válidas y asegura que el número ingresado esté dentro del rango permitido.
# El programa utiliza la biblioteca random para generar un número aleatorio y la función input para recibir la entrada del usuario.
# El código es fácil de entender y sigue una estructura clara, lo que lo hace accesible para principiantes en programación.
# El uso de excepciones para manejar errores de entrada es una buena práctica que mejora la robustez del programa.
# El programa es interactivo y proporciona retroalimentación inmediata al usuario, lo que lo hace más atractivo.
# El juego es simple pero entretenido, y puede ser una buena manera de practicar la lógica de programación y el manejo de entradas del usuario.
# El código es un buen ejemplo de cómo crear un juego básico en Python, y puede ser ampliado o modificado para incluir más características o niveles de dificultad.
# El programa es un buen ejercicio para principiantes en programación y puede ser utilizado como base para proyectos más complejos.