#Estructura del for en python
# for i in range(10):
#     print(i)
# Este codigo imprime los números del 0 al 9.


# for i in range(10, 0, -1):
#     print(i)
# Este código imprime los números del 10 al 1.

# for i in range(0, 10, 2):
#     print(i)
# Este código imprime los números del 0 al 8, de dos en dos.

# Ejemplo de uso de for con una lista
#numeros = [1, 2, 3, 4, 5]
#for numero in numeros:
#    print(numero)
# Este código imprime cada número de la lista "numeros".

# Ejemplo de uso de for con una cadena
#cadena = "Hola"
#for letra in cadena:
#    print(letra)
# Este código imprime cada letra de la cadena "Hola".

# Ejemplo de uso de for con un diccionario
#diccionario = {"a": 1, "b": 2, "c": 3}
#for clave, valor in diccionario.items():
#    print(f"{clave}: {valor}")
# Este código imprime cada clave y valor del diccionario "diccionario".
# Este código es un ejemplo de cómo usar el bucle for en Python para iterar sobre diferentes tipos de colecciones, como listas, cadenas y diccionarios.
# El bucle for es una herramienta poderosa en Python que permite recorrer elementos de manera eficiente y sencilla.

# Ejemplo de uso de for aplicado a un programa simple
# Programa simple que suma los números del 1 al 10
suma = 0
for i in range(1, 11):
    suma += i
print(f"La suma de los números del 1 al 10 es: {suma}")
# Este código es un ejemplo de cómo usar el bucle for en Python para realizar una tarea simple, como sumar los números del 1 al 10.


# Ejemplo de for con un programa mas complejo
# Programa que calcula la suma de los números pares del 1 al 20
suma_pares = 0
for i in range(1, 21):
    if i % 2 == 0:
        suma_pares += i
print(f"La suma de los números pares del 1 al 20 es: {suma_pares}")
# Este código es un ejemplo de cómo usar el bucle for en Python para realizar una tarea más compleja, como sumar los números pares del 1 al 20.