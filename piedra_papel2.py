import random

movimientos = ["piedra", "papel", "tijera"]

computadora = random.choice(movimientos)
usuario = input("Ingrese piedra papel o tijera: ").lower()

puntos_comp = 0
puntos_user = 0

while puntos_comp < 3 and puntos_user < 3:
    if usuario not in movimientos:
        print("Valor invalido")

    else :
        if computadora == "papel" and usuario == "tijera":
            print("Felicidades le has ganado a la computadora")
            puntos_user += 1

        elif computadora == "tijera" and usuario == "papel":
            print(f"Perdiste la computadora saco {computadora} y tu sacaste {usuario}")
            puntos_comp += 1
            
        elif computadora == "piedra" and usuario == "tijera":
            print(f"Perdiste la computadora saco {computadora} y tu sacaste {usuario}")
            puntos_comp += 1

        elif computadora == "tijera" and usuario == "piedra":
            print("Felicidades le has ganado a la computadora")
            puntos_user += 1

        elif computadora == "piedra" and usuario == "papel":
            print("Felicidades le has ganado a la computadora")
            puntos_user += 1

        elif computadora == "papel" and usuario == "piedra":
            print(f"Perdiste la computadora saco {computadora} y tu sacaste {usuario}")
            puntos_comp += 1
            
        else:
            print("empate")
            
    computadora = random.choice(movimientos)
    usuario = input("Ingrese piedra papel o tijera: ").lower()
print("Fin del juego")
print("Puntuacion final")
print("Computadora: ", puntos_comp)
print("Usuario: ", puntos_user)



print(computadora)
print(usuario)

