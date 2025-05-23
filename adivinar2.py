import random

minimo = 1
maximo = 10

numero_secreto = random.randint(minimo, maximo)
intentos = 5

while True:
    intento_usuario = input(f"Adivina el número entre {minimo} y {maximo}: ")
    if numero_secreto != intento_usuario:
        print("Incorrecto, intenta de nuevo.")
        intentos -= 1
        if intentos == 0:
            print(f"Lo siento, has agotado tus intentos. El número era {numero_secreto}.")
            break
    else:
        print(f"¡Felicidades! Has adivinado el número {numero_secreto} correctamente.")
        break
# Este código es un juego simple de adivinanza de números. El usuario tiene 5 intentos para adivinar un número aleatorio entre 1 y 10.