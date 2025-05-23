#Crear una calculadora simple en Python que realice operaciones básicas como suma, resta, multiplicación y división.

# Definición de la función calculadora
def calculadora():
    print("Bienvenido a la calculadora simple")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    while True:
        # Solicitar al usuario que elija una operación
        operacion = input("Elige una operación (1/2/3/4/5): ")

        if operacion == '5':
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break

        if operacion not in ['1', '2', '3', '4']:
            print("Operación no válida. Intenta de nuevo.")
            continue

        # Solicitar los números para la operación
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Entrada no válida. Por favor, ingresa números.")
            continue

        # Realizar la operación seleccionada
        if operacion == '1':
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif operacion == '2':
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif operacion == '3':
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif operacion == '4':
            if num2 == 0:
                print("Error: División por cero no permitida.")
                continue
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")
        print("-" * 30)
# Llamar a la función para iniciar la calculadora
calculadora()
# Este código es una calculadora simple en Python que permite al usuario realizar operaciones básicas como suma, resta, multiplicación y división.
# El usuario puede elegir la operación deseada y luego ingresar dos números para realizar el cálculo.
# El programa maneja entradas no válidas y errores como la división por cero de manera efectiva.
# La calculadora sigue funcionando hasta que el usuario decide salir escribiendo '5'.
# El código es fácil de entender y sigue una estructura clara, lo que lo hace accesible para principiantes en programación.
