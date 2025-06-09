'''
Ejercicio 1: Suma interactiva hasta que el usuario diga 'salir'

Escribe un programa que pida al usuario que ingrese números repetidamente y los sume. El programa debe detenerse cuando el usuario escriba la palabra "salir".

'''
# Inicializar la suma
suma = 0
while True:
    entrada = input("Ingrese un número para sumar (o 'salir' para terminar): ")
    
    if entrada.lower() == 'salir':
        break  # Salir del bucle si el usuario escribe 'salir'
    
    try:
        numero = int(entrada)  # Convertir la entrada a un número
        suma += numero  # Sumar el número a la suma total
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número o 'salir'.")
# Imprimir el resultado final
print(f"La suma total es: {suma}")
# Este código es un ejemplo de cómo usar un bucle while en Python para realizar una tarea interactiva.